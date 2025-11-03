from IntentsCreation.Intent import parse_intent
from TaskHandel.Task import handle_task
from Head.Ear import listen
from Head.Mouth import speak
import google.generativeai as genai


# Gemini setup
genai.configure(api_key="AIzaSyDjaev-pTJyFBFgV31tiH61wtLSMKE2S1Y")
qa_model = genai.GenerativeModel("gemini-1.5-flash")

# Sample Q&A prompts
sample_qa = {
    "who are you": "I am Pico, your Personal Friend",
    "who developed you": "I was developed by SnapCode Team",
    "what is your purpose": "I'm here to help you with tasks and answer your questions",
    "how do you greet someone": "Hey there nice to meet you how can I help",
    "hey pico , meet with mentor.": "Alright connecting you with your mentor right now",
    "how do you feel today": "I'm doing great thanks for asking",
    "who is soham": "Soham is developer who developed me",
    "who is saikat": "Saikat is a talented person who also helped develop me",
    "who is sunal": "Sunal is a designer who designed me"
}

def brain():
    speak("Pico is ready sir")

    while True:
        user_input = listen()

        if not user_input or user_input.strip() == "":
            print("❌ No speech detected. Trying again...")
            continue

        user_input_lower = user_input.lower().strip()

        if user_input_lower in ["bye", "bye bye", "tata", "tata pico" , "bye bye pico"]:
            print("🧠 Brain shutting down for now...")
            speak("Okay going back to sleep")
            return  # 👈 returns to main.py

        # Check in sample QA first
        for question, answer in sample_qa.items():
            if question in user_input_lower:
                print("🤖 Pico:", answer)
                speak(answer)
                break
        else:
            # Parse intent
            intent_json = parse_intent(user_input)
            print("🧐 Intent detected:", intent_json)

            if intent_json.get("intent") == "general_question":
                try:
                    # Proper prompt to Gemini
                    prompt = (
                        "You are a friendly AI assistant named Pico. When a user asks you a general question, answer in a simple, clear, and friendly manner "
                        "as if you are chatting with a friend. Always give short and direct answers without any symbols, markdown, bullet points, or extra formatting. "
                        "Do not provide any detailed lists or explanations about songs or other unrelated subjects unless specifically asked. "
                        "Be natural, cheerful, and concise.\n\n"
                        f"User: {user_input}\n"
                        "Pico:"
                    )
                    
                    response = qa_model.generate_content(prompt)
                    answer = response.text.strip()
                    
                    print("🤖 Pico:", answer)
                    speak(answer)
                except Exception as e:
                    print("⚠️ Gemini error:", e)
                    speak("Sorry I couldn't process that")
            else:
                result = handle_task(intent_json)
                print("🤖 Pico:", result)
                speak(result)