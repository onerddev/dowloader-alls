# 📖 Guia de Instalação Detalhado

## Windows

### 1. Instalar Python
1. Baixe em https://www.python.org/downloads/
2. Execute o instalador
3. **IMPORTANTE**: Marque "Add Python to PATH"
4. Clique "Install Now"

### 2. Instalar Git
1. Baixe em https://git-scm.com/download/win
2. Execute o instalador com as opções padrão

### 3. Instalar FFmpeg
```bash
# Usando chocolatey (mais fácil)
choco install ffmpeg

# Ou baixe manualmente em https://ffmpeg.org/download.html
```

### 4. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/video-downloader-pro.git
cd video-downloader-pro
```

### 5. Criar Ambiente Virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 6. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 7. Executar
**Versão Web:**
```bash
python app.py
```

**Versão Terminal:**
```bash
python main.py
```

---

## macOS

### 1. Instalar Homebrew (se não tiver)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Instalar Python e FFmpeg
```bash
brew install python@3.10 ffmpeg
```

### 3. Instalar Git
```bash
brew install git
```

### 4. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/video-downloader-pro.git
cd video-downloader-pro
```

### 5. Criar Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 7. Executar
**Versão Web:**
```bash
python app.py
```

**Versão Terminal:**
```bash
python main.py
```

---

## Linux (Ubuntu/Debian)

### 1. Instalar Dependências
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git ffmpeg
```

### 2. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/video-downloader-pro.git
cd video-downloader-pro
```

### 3. Criar Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependências Python
```bash
pip install -r requirements.txt
```

### 5. Executar
**Versão Web:**
```bash
python app.py
```

**Versão Terminal:**
```bash
python main.py
```

---

## Troubleshooting

### "python: command not found"
- **Windows**: Reinstale Python marcando "Add Python to PATH"
- **macOS/Linux**: Use `python3` em vez de `python`

### "FFmpeg not found"
- Verifique se FFmpeg está instalado
- Adicione ao PATH se necessário

### "ModuleNotFoundError"
```bash
# Certifique-se que o ambiente virtual está ativado
# Depois reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### Porta 5000 já em uso
```bash
# Mude a porta em app.py
app.run(debug=True, port=5001)
```

---

## Próximos Passos

1. Acesse http://localhost:5000
2. Teste com uma URL de vídeo
3. Leia o README.md para mais informações
4. Abra uma issue se encontrar problemas

Sucesso! 🎉
