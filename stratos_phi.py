from transformers import AutoTokenizer, AutoModelForCausalLM
from textblob import TextBlob

class StratosBrain:
    def __init__(self):
        print("🧠 Loading Phi-2 model...")
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")
        print("✅ Phi-2 loaded.")

    def detect_emotion(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.3:
            return "happy"
        elif polarity < -0.3:
            return "sad"
        else:
            return "neutral"

    def respond(self, user_input):
        try:
            mood = self.detect_emotion(user_input)

            emotion_prompt = {
                "happy": "You're feeling happy and energetic!",
                "sad": "You're feeling down. Comfort the user kindly.",
                "neutral": "You're having a normal day. Be helpful.",
            }[mood]

            prompt = f"You are Stratos, a friendly and thoughtful AI.\nUser mood: {mood} – {emotion_prompt}\nUser: {user_input}\nStratos:"
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_new_tokens=100)
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response.split("Stratos:")[-1].strip()

        except Exception as e:
            return f"⚠️ Error thinking: {str(e)}"
