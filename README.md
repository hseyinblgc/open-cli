## open-cli

open-cli, Google GenAI SDK (google-genai) ve Silero TTS kullanarak terminalden sorular gönderip hem metin hem de sesli cevap almanızı sağlayan bir Python komut satırı uygulamasıdır.

### Özellikler

- Google Gemini 2.5 Flash modeli ile doğal dil işleme
- Silero TTS ile metin-konuşma dönüşümü (İngilizce)
- 1000 karakterden kısa cevaplar için otomatik sesli yanıt

### Gereksinimler

- Python 3.8 veya üzeri
- pip
- İnternet bağlantısı ve geçerli bir Google GenAI API anahtarı
- Ses çıkışı için ses kartı/hoparlör

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
python -m pip install -r requirements.txt
```

### API Anahtarı Ayarlama

[start.py](start.py) dosyasındaki `YOUR_API_KEY_HERE` kısmını Google AI Studio'dan aldığınız API anahtarı ile değiştirin:

```python
apikey = genai.Client(api_key="YOUR_API_KEY_HERE")
```

### Çalıştırma

API anahtarını ayarladıktan sonra proje dizininde çalıştırın:

```bash
python start.py
```

- `type your question:` istemine sorunuzu yazın ve Enter'a basın
- Metin cevabını okuyun
- 1000 karakterden kısaysa sesli yanıt otomatik olarak çalacaktır
- Döngüden çıkmak için `quit` yazın veya `Ctrl+C` ile işlemi sonlandırın

### Örnek Kullanım

```
$ python start.py
type your question:
>What is Python?
Thinking...

Python is a high-level, interpreted programming language...
[Sesli yanıt çalıyor]

type your question:
>quit
```

### Teknik Detaylar

- **TTS Modeli:** Silero TTS v3_en (İngilizce)
- **AI Modeli:** Google Gemini 2.5 Flash
- **Ses Örnekleme:** 48000 Hz
- **Cihaz:** CPU (varsayılan)
- **Maksimum Sesli Yanıt:** 1000 karakter

### Notlar

- TTS İngilizceye ayarlıdır. Diğer dillerde düzgün seslendirmeyecektir.
- Uzun yanıtlar (>1000 karakter) için ses üretilmez, sadece metin görüntülenir.
- İlk çalıştırmada Silero TTS modeli indirilecektir (~100MB).

### Sorun Giderme

- **Ses çıkmıyorsa:** `sounddevice` paketinin düzgün kurulduğundan ve ses kartınızın çalıştığından emin olun
- **API hatası alıyorsanız:** API anahtarınızın geçerli ve internet bağlantınızın aktif olduğunu kontrol edin
- **Model indirme hatası:** İnternet bağlantınızı kontrol edin ve PyTorch Hub'a erişebildiğinizden emin olun