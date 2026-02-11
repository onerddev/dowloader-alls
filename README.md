# 🎬 Video Downloader Pro

Um aplicativo moderno e poderoso para baixar vídeos do YouTube, Instagram e TikTok com suporte a múltiplas qualidades e extração de áudio.

## ✨ Recursos

- ✅ **Suporte Multiplataforma**: YouTube, Instagram e TikTok
- ✅ **Múltiplas Qualidades**: Escolha entre best, alta (1080p), média (720p) e rápida (480p)
- ✅ **Extração de Áudio**: Baixe apenas o áudio em formato MP3
- ✅ **Validação de URL**: Valide URLs antes de fazer download
- ✅ **Informações do Vídeo**: Veja título, duração, canal e visualizações
- ✅ **Histórico de Downloads**: Acompanhe todos os downloads realizados
- ✅ **Interface Moderna**: Interface web responsiva e intuitiva
- ✅ **Versão Terminal**: Aplicação de linha de comando também disponível

## 📋 Requisitos

- Python 3.8+
- FFmpeg (para extração de áudio)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/video-downloader-pro.git
cd video-downloader-pro
```

### 2. Crie um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Instale FFmpeg (se ainda não tiver)

**Windows (usando chocolatey):**
```bash
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

## 💻 Como Usar

### Versão Web

```bash
python app.py
```

Acesse `http://localhost:5000` no seu navegador.

### Versão Terminal

```bash
python main.py
```

Siga o menu interativo para escolher suas opções.

## 🎯 Funcionalidades

### Download de Vídeo
1. Cole a URL do vídeo
2. Escolha o tipo de download (Vídeo ou Áudio)
3. Selecione a qualidade desejada
4. Clique em "Baixar"

### Ver Informações
1. Vá para a aba "ℹ️ Info"
2. Cole a URL
3. Clique em "Validar"
4. Veja os detalhes do vídeo

### Histórico
1. Vá para a aba "📜 Histórico"
2. Veja todos os downloads realizados
3. Use "🗑️ Limpar" para limpar o histórico

## 📁 Estrutura do Projeto

```
video-downloader-pro/
├── app.py                 # Aplicação Flask (web)
├── main.py               # Aplicação terminal
├── config.py             # Configurações do projeto
├── requirements.txt      # Dependências Python
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Este arquivo
├── templates/
│   └── index.html       # Interface web
└── download_history.json # Histórico de downloads
```

## 🔌 API Endpoints

### POST `/download`
Baixa um vídeo completo
- **Parâmetros**: `url`, `quality` (best|high|medium|low)

### POST `/download-audio`
Baixa apenas o áudio em MP3
- **Parâmetros**: `url`

### POST `/api/validate-url`
Valida URL e detecta plataforma
- **Body**: `{ "url": "..." }`
- **Response**: `{ "valid": boolean, "platform": string, "info": object }`

### POST `/api/info`
Obtém informações do vídeo
- **Body**: `{ "url": "..." }`
- **Response**: `{ "title": string, "duration": number, "uploader": string, "view_count": number }`

### GET `/api/history`
Obtém histórico de downloads
- **Response**: Array de downloads

### POST `/api/history/clear`
Limpa o histórico
- **Response**: `{ "success": boolean }`

## ⚙️ Configuração

Edite o arquivo `config.py` para ajustar:
- Tamanho máximo de arquivo
- Diretórios de download
- Chave secreta do Flask
- Opções de yt-dlp

## 🐛 Troubleshooting

### FFmpeg não encontrado
Certifique-se de que FFmpeg está instalado e no PATH do sistema.

### Erro ao fazer download
- Verifique se a URL é válida
- Tente uma URL diferente (alguns vídeos podem estar protegidos)
- Verifique sua conexão com a internet

### Histórico não aparece
Limpe o cache do navegador ou abra em modo incógnito.

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 👨‍💻 Autor

onerd dev

## 🤝 Contribuições

## ⭐ Se gostou do projeto, não esqueça de deixar uma estrela!

---

**Última atualização**: Fevereiro 2026

