from speech_to_text import speech_to_text
from image_generator import generate_image

API_KEY = "YOUR_MONSTERAPI_KEY"
AUDIO_FILE = "audio.wav"

print("🎤 Converting speech to text...")
text = speech_to_text(AUDIO_FILE)
print("📝 Recognized Text:", text)

if "error" not in text.lower():
    print("🖼️ Generating image...")
    image_url = generate_image(text, API_KEY)
    print("✅ Image Generated Successfully!")
    print("🔗 Image URL:", image_url)
else:
    print("❌ Failed to process audio.")
