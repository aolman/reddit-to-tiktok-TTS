import requests
import json

def text_to_speech(text, output_path):
    with open("config/settings.json") as f:
        creds = json.load(f)["elevenlabs"]
    api_key = creds["api_key"]
    voice_id = creds["voice_id"]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Audio successfully saved to {output_path}")
    else:
        print("Error generating speech:", response.text)
    