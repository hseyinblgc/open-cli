from google import genai
import torch
import sounddevice as sd
import threading

apikey = genai.Client(api_key="YOUR_API_KEY_HERE")

def callapi(user_input):
    response = apikey.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    out = response.text
    if len(out) < 1000: 
        # Ses çıkışını ayrı thread'de başlat
        audio_thread = threading.Thread(target=rise, args=(response.text,))
        audio_thread.daemon = True  # Ana program kapandığında thread'i sonlandır
        audio_thread.start()
    
    return response  # yield yerine return

## Voice model
is_running = True

language = 'en'
model_id = 'v3_en'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                      model='silero_tts',
                                      language=language,
                                      speaker=model_id)
model.to(device)

sample_rate = 48000
speaker = 'en_0'

# let me hear
def rise(speak):
    audio = model.apply_tts(text=speak,
                            speaker=speaker,
                            sample_rate=sample_rate)
    
    sd.play(audio.numpy(), sample_rate)
    sd.wait()