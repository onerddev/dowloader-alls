# Video Downloader Pro

Aplicação para download de vídeos do YouTube, Instagram e TikTok, com suporte a múltiplas qualidades e extração de áudio em MP3. O projeto possui versão web e versão via terminal.

---

## 1. Visão Geral

O sistema permite:

- Download de vídeos em diferentes resoluções
- Extração de áudio em formato MP3
- Validação de URLs antes do download
- Consulta de informações do vídeo
- Histórico local de downloads
- Execução via interface web ou linha de comando

---

## 2. Recursos

- Suporte a YouTube, Instagram e TikTok
- Seleção de qualidade: best, 1080p, 720p, 480p
- Extração de áudio em MP3
- Validação de URL e detecção automática de plataforma
- Visualização de título, duração, canal e visualizações
- Histórico de downloads armazenado em JSON
- Interface web baseada em Flask
- Versão CLI interativa

---

## 3. Requisitos

- Python 3.8 ou superior
- FFmpeg (necessário para extração de áudio)
- pip

---

## 4. Instalação

### 4.1 Clonar o Repositório

```bash
git clone github.com/onerddev/video-downloader-pro.git
cd video-downloader-pro
```

---

### 4.2 Criar Ambiente Virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4.3 Instalar Dependências

```bash
pip install -r requirements.txt
```

---

### 4.4 Instalar FFmpeg

#### Windows (Chocolatey)

```bash
choco install ffmpeg
```

#### macOS

```bash
brew install ffmpeg
```

#### Linux

```bash
sudo apt-get install ffmpeg
```

---

## 5. Execução

### 5.1 Versão Web

```bash
python app.py

---

### 5.2 Versão Terminal

```bash
python main.py
```

Siga o menu interativo exibido no terminal.

---

## 6. Funcionalidades

### Download de Vídeo

1. Informar a URL
2. Escolher tipo de download (vídeo ou áudio)
3. Selecionar qualidade
4. Confirmar download

---

### Consulta de Informações

1. Informar a URL
2. Validar
3. Visualizar:
   - Título
   - Duração
   - Canal
   - Número de visualizações

---

### Histórico

- Lista todos os downloads realizados
- Permite limpar histórico
- Armazenado em `download_history.json`

---

## 7. Estrutura do Projeto

```
video-downloader-pro/
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── download_history.json
```

---

## 8. API Endpoints

### POST /download

Realiza download de vídeo.

Parâmetros:
- url
- quality (best | high | medium | low)

---

### POST /download-audio

Realiza download apenas do áudio em MP3.

Parâmetros:
- url

---

### POST /api/validate-url

Valida URL e identifica plataforma.

Body:
```
{ "url": "..." }
```

Resposta:
```
{ 
  "valid": boolean, 
  "platform": string, 
  "info": object 
}
```

---

### POST /api/info

Obtém informações do vídeo.

Body:
```
{ "url": "..." }
```

Resposta:
```
{
  "title": string,
  "duration": number,
  "uploader": string,
  "view_count": number
}
```

---

### GET /api/history

Retorna histórico de downloads.

---

### POST /api/history/clear

Limpa histórico.

Resposta:
```
{ "success": boolean }
```

---

## 9. Configuração

O arquivo `config.py` permite configurar:

- Diretório de downloads
- Tamanho máximo de arquivo
- Chave secreta do Flask
- Parâmetros personalizados do yt-dlp

---

## 10. Troubleshooting

### FFmpeg não encontrado

Verifique se está instalado e disponível no PATH do sistema.

---

### Erro ao fazer download

- Verifique se a URL é válida
- Teste outra URL
- Verifique conexão com a internet

---

### Histórico não aparece

- Verifique permissões de escrita no arquivo JSON
- Limpe cache do navegador
- Reinicie a aplicação

---

## 11. Licença

MIT License

---

## 12. Autor

onerd dev

---

Última atualização: Fevereiro 2026


