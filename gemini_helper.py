import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# ✅ This is the correct latest model name:
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()
