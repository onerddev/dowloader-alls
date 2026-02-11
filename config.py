"""
Arquivo de configuração da aplicação
"""

import os
from pathlib import Path

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent

# Configurações Flask
DEBUG = True
SECRET_KEY = 'sua-chave-secreta-aqui-mude-em-producao'
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'temp_downloads')
TEMP_DIR = os.path.join(BASE_DIR, 'temp_downloads')

# Configurações de Download
MAX_FILE_SIZE_MB = 500
DOWNLOAD_HISTORY_FILE = os.path.join(BASE_DIR, 'download_history.json')

# Criar diretórios se não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configurações yt-dlp
YDL_OPTIONS = {
    'quiet': True,
    'no_warnings': True,
    'socket_timeout': 30,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
}

# Plataformas suportadas
SUPPORTED_PLATFORMS = {
    'youtube': {
        'domains': ['youtube.com', 'youtu.be', 'youtube-nocookie.com'],
        'emoji': '🎥',
        'name': 'YouTube'
    },
    'instagram': {
        'domains': ['instagram.com'],
        'emoji': '📱',
        'name': 'Instagram'
    },
    'tiktok': {
        'domains': ['tiktok.com', 'vm.tiktok.com', 'vt.tiktok.com'],
        'emoji': '🎵',
        'name': 'TikTok'
    }
}
