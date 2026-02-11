from flask import Flask, render_template, request, send_file, after_this_request, jsonify
import yt_dlp
import os
import tempfile
import json
import shutil
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

# Configurações
DOWNLOAD_HISTORY_FILE = 'download_history.json'
MAX_FILE_SIZE_MB = 500
TEMP_DOWNLOADS_DIR = 'temp_downloads'

# Criar diretório de downloads temporários
os.makedirs(TEMP_DOWNLOADS_DIR, exist_ok=True)

# ===== FUNÇÕES UTILITÁRIAS =====

def load_download_history():
    """Carrega histórico de downloads do arquivo JSON"""
    if os.path.exists(DOWNLOAD_HISTORY_FILE):
        with open(DOWNLOAD_HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_download_history(history):
    """Salva histórico de downloads em arquivo JSON"""
    with open(DOWNLOAD_HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def add_to_history(url, title, platform, download_type):
    """Adiciona um download ao histórico"""
    history = load_download_history()
    history.append({
        'url': url,
        'title': title,
        'platform': platform,
        'type': download_type,
        'timestamp': datetime.now().isoformat()
    })
    save_download_history(history)

def validate_url(url):
    """Valida se a URL é de uma plataforma suportada"""
    url_lower = url.lower()
    platforms = {
        'youtube': ['youtube.com', 'youtu.be', 'youtube-nocookie.com'],
        'instagram': ['instagram.com'],
        'tiktok': ['tiktok.com', 'vm.tiktok.com', 'vt.tiktok.com']
    }
    
    for platform, domains in platforms.items():
        if any(domain in url_lower for domain in domains):
            return platform
    return None

def get_video_info(url):
    """Extrai informações do vídeo sem fazer download"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 30,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Unknown'),
                'upload_date': info.get('upload_date', 'Unknown'),
                'view_count': info.get('view_count', 0)
            }
    except Exception as e:
        return None

def cleanup_temp_files():
    """Remove arquivos temporários antigos"""
    try:
        for filename in os.listdir(TEMP_DOWNLOADS_DIR):
            file_path = os.path.join(TEMP_DOWNLOADS_DIR, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    except Exception:
        pass

# ===== ROTAS =====

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/validate-url', methods=['POST'])
def validate_url_route():
    """API para validar URL e obter informações"""
    data = request.json
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'valid': False, 'error': 'URL não fornecida'})
    
    platform = validate_url(url)
    if not platform:
        return jsonify({'valid': False, 'error': 'URL de plataforma não suportada'})
    
    info = get_video_info(url)
    if not info:
        return jsonify({'valid': False, 'error': 'Não foi possível obter informações do vídeo'})
    
    return jsonify({
        'valid': True,
        'platform': platform,
        'info': info
    })

@app.route('/download', methods=['POST'])
def download():
    """Download de vídeo completo"""
    video_url = request.form.get('url', '').strip()
    quality = request.form.get('quality', 'best')
    
    if not video_url:
        return "URL é obrigatória", 400
    
    platform = validate_url(video_url)
    if not platform:
        return "Plataforma não suportada. Use YouTube, Instagram ou TikTok", 400
    
    try:
        tmp_dir = tempfile.mkdtemp()
        
        # Configurações de qualidade
        format_opts = {
            'best': 'best',
            'high': 'best[ext=mp4]/best',
            'medium': 'best[height<=720]',
            'low': 'best[height<=480]'
        }
        
        ydl_opts = {
            'format': format_opts.get(quality, 'best'),
            'outtmpl': os.path.join(tmp_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 30,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            title = info.get('title', 'video')
        
        # Adicionar ao histórico
        add_to_history(video_url, title, platform, 'video')
        
        @after_this_request
        def cleanup(response):
            try:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            except Exception:
                pass
            return response
        
        return send_file(filename, as_attachment=True)
    
    except Exception as e:
        return f"Erro: {str(e)}", 500

@app.route('/download-audio', methods=['POST'])
def download_audio():
    """Download apenas de áudio em formato MP3"""
    video_url = request.form.get('url', '').strip()
    
    if not video_url:
        return "URL é obrigatória", 400
    
    platform = validate_url(video_url)
    if not platform:
        return "Plataforma não suportada", 400
    
    try:
        tmp_dir = tempfile.mkdtemp()
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(tmp_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 30,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            title = info.get('title', 'audio')
            audio_file = os.path.join(tmp_dir, f'{title}.mp3')
        
        # Adicionar ao histórico
        add_to_history(video_url, title, platform, 'audio')
        
        @after_this_request
        def cleanup(response):
            try:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            except Exception:
                pass
            return response
        
        return send_file(audio_file, as_attachment=True, mimetype='audio/mpeg')
    
    except Exception as e:
        return f"Erro: {str(e)}", 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Retorna histórico de downloads em JSON"""
    history = load_download_history()
    return jsonify(history)

@app.route('/api/history/clear', methods=['POST'])
def clear_history():
    """Limpa o histórico de downloads"""
    save_download_history([])
    return jsonify({'success': True, 'message': 'Histórico limpo'})

@app.route('/api/info', methods=['POST'])
def get_info():
    """Obtém informações do vídeo"""
    data = request.json
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'URL não fornecida'}), 400
    
    info = get_video_info(url)
    if not info:
        return jsonify({'error': 'Não foi possível obter informações'}), 400
    
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
