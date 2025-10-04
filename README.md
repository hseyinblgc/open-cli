## open-cli

Kısa açıklama

open-cli, Google GenAI SDK (google-genai) kullanarak terminalden sorular gönderip cevap almanızı sağlayan basit bir Python komut satırı uygulamasıdır. Projedeki ana dosya `start.py` dur.

### Gereksinimler

- Python 3.8 veya üzeri
- pip
- İnternet bağlantısı ve geçerli bir Google GenAI API anahtarı

### Kurulum

1. (İsteğe bağlı) Sanal ortam oluşturun ve etkinleştirin:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
```

Windows PowerShell için:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Gerekli paketleri yükleyin:

```bash
python -m pip install --upgrade pip
python -m pip install google-genai
```

### API Anahtarı (güvenli şekilde ayarlama)

ai studio dan alınan api anahtarı start.py dosyasının içindeki YOUR_API_KEY_HERE ile değiştirilmelidir 

### Çalıştırma

Ortam değişkenini ayarladıktan sonra proje dizininde çalıştırın:

```bash
python start.py
```

Komut satırındaki isteme `type your question:` geldiğinde soru yazıp Enter tuşuna basın. Döngüden çıkmak için `quit` yazın veya Ctrl+C ile işlemi sonlandırın.

### Örnek akış

1. `python start.py`
2. `type your question:` -> "Bugünün hava durumu nasıl?"
3. Gelen cevabı okuyun.
