from google import genai
import torch
import sounddevice as sd

apikey = genai.Client(api_key="YOUR_API_KEY_HERE")
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

## Call gemini
def callapi():
    user_input = input("type your question:\n>")
    if user_input == "quit":
        return False
    
    print("Thinking...\n")
    
    try:
        response = apikey.models.generate_content(
            model="gemini-2.5-flash", contents=user_input
        )
        out = response.text
        print(out + "\n")
        if len(out) < 1000:    
            rise(response.text)
        else:
             print("Too long, No audio will be generated for this response")
        return True
    except Exception as e:
        print(f"Error: {e}\n")
        return True

# let me hear
def rise(speak):
        audio = model.apply_tts(text=speak,
                                speaker=speaker,
                                sample_rate=sample_rate)
        
        sd.play(audio.numpy(), sample_rate)
        sd.wait() 

while is_running:
    is_running = callapi()
