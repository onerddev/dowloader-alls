import yt_dlp
import os
import json
from datetime import datetime

# Configurações
DOWNLOAD_HISTORY_FILE = 'download_history.json'
DOWNLOADS_DIR = 'downloads'

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# ===== FUNÇÕES UTILITÁRIAS =====

def load_download_history():
    """Carrega histórico de downloads"""
    if os.path.exists(DOWNLOAD_HISTORY_FILE):
        with open(DOWNLOAD_HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_download_history(history):
    """Salva histórico de downloads"""
    with open(DOWNLOAD_HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def add_to_history(url, title, platform, download_type):
    """Adiciona download ao histórico"""
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
    """Valida URL e detecta plataforma"""
    url_lower = url.lower()
    if any(d in url_lower for d in ['youtube.com', 'youtu.be']):
        return 'YouTube'
    elif 'instagram.com' in url_lower:
        return 'Instagram'
    elif any(d in url_lower for d in ['tiktok.com', 'vm.tiktok.com']):
        return 'TikTok'
    return None

def get_video_info(url):
    """Extrai informações do vídeo"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 30,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Unknown'),
                'view_count': info.get('view_count', 0)
            }
    except:
        return None

def download_video(url, quality='best', audio_only=False):
    """Faz download de vídeo com opções de qualidade"""
    platform = validate_url(url)
    if not platform:
        print("❌ Plataforma não suportada!")
        return False
    
    try:
        print(f"\n📺 Plataforma detectada: {platform}")
        
        format_opts = {
            'best': 'best',
            'high': 'best[height<=1080]',
            'medium': 'best[height<=720]',
            'low': 'best[height<=480]'
        }
        
        if audio_only:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
                'quiet': False,
                'socket_timeout': 30,
            }
            print("🎵 Modo: Apenas Áudio (MP3)")
        else:
            ydl_opts = {
                'format': format_opts.get(quality, 'best'),
                'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
                'quiet': False,
                'socket_timeout': 30,
            }
            print(f"📹 Modo: Vídeo ({quality.upper()})")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("⏳ Iniciando download...")
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'video')
            
            download_type = 'audio' if audio_only else 'video'
            add_to_history(url, title, platform, download_type)
            
            print(f"✅ Download concluído: {title}")
            return True
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

def show_video_info(url):
    """Mostra informações do vídeo"""
    info = get_video_info(url)
    if info:
        print(f"\n📋 Informações do Vídeo:")
        print(f"   Título: {info['title']}")
        print(f"   Duração: {info['duration']}s")
        print(f"   Canal: {info['uploader']}")
        print(f"   Visualizações: {info['view_count']:,}")
    else:
        print("❌ Não foi possível obter informações")

def show_history():
    """Mostra histórico de downloads"""
    history = load_download_history()
    if not history:
        print("\n📜 Histórico vazio!")
        return
    
    print("\n📜 Histórico de Downloads:")
    for i, item in enumerate(history[-10:], 1):  # Últimos 10
        print(f"{i}. {item['title']} ({item['platform']}) - {item['type']}")

def menu_principal():
    """Menu principal da aplicação"""
    print("\n" + "="*50)
    print("🎬 VIDEO DOWNLOADER - VERSÃO TERMINAL")
    print("="*50)
    print("\n1️⃣  Baixar Vídeo")
    print("2️⃣  Baixar Apenas Áudio (MP3)")
    print("3️⃣  Ver Informações do Vídeo")
    print("4️⃣  Ver Histórico")
    print("5️⃣  Sair")
    return input("\n👉 Escolha uma opção (1-5): ").strip()

def download_video_menu():
    """Menu para baixar vídeo"""
    print("\n" + "-"*50)
    url = input("Cole a URL do vídeo: ").strip()
    if not url:
        print("❌ URL não fornecida!")
        return
    
    print("\nQualidade:")
    print("1. best  (Melhor qualidade)")
    print("2. high  (Até 1080p)")
    print("3. medium (720p)")
    print("4. low   (480p)")
    quality = input("Escolha (1-4): ").strip()
    
    quality_map = {'1': 'best', '2': 'high', '3': 'medium', '4': 'low'}
    quality = quality_map.get(quality, 'best')
    
    download_video(url, quality, audio_only=False)

def download_audio_menu():
    """Menu para baixar áudio"""
    print("\n" + "-"*50)
    url = input("Cole a URL do vídeo: ").strip()
    if not url:
        print("❌ URL não fornecida!")
        return
    
    download_video(url, audio_only=True)

def info_menu():
    """Menu para ver informações"""
    print("\n" + "-"*50)
    url = input("Cole a URL do vídeo: ").strip()
    if not url:
        print("❌ URL não fornecida!")
        return
    
    show_video_info(url)

def main():
    """Loop principal"""
    while True:
        choice = menu_principal()
        
        if choice == '1':
            download_video_menu()
        elif choice == '2':
            download_audio_menu()
        elif choice == '3':
            info_menu()
        elif choice == '4':
            show_history()
        elif choice == '5':
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida!")
        
        input("\n⏎ Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
