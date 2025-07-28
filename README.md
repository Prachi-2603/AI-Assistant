AI Assistant Web App

 This project is a simple, user-friendly AI Assistant web application built with Python and Flask,
 powered by Google's Gemini API. The assistant can:
 
 1. Answer Questions
 
 2. Summarize Text
 
 3. Generate Creative Content
 
 Project Structure:-----------------
 
 app.py               - Flask application logic
 gemini_helper.py     - Gemini API integration
 feedback_log.txt     - Logs for user feedback
 templates/index.html - Frontend HTML form
 static/style.css     - CSS styling
 
 How to Run:----------

 1. Install Dependencies:
   pip install flask
   pip install google-generativeai
 
 2. Set Gemini API Key:
   Replace "YOUR_API_KEY" in gemini_helper.py with your actual key.
 
 3. Run the App:
   python app.py
   Visit http://127.0.0.1:5000 in your browser.
 
 Features:---------- 
 
 -Answer factual questions (e.g., "What is the capital of Japan?")
 
 - Summarize text input (e.g., "Summarize this: [Text]")
 
 - Generate stories or poems based on user input
 
 Feedback Logging:----------------
 
 -User feedback is saved in feedback_log.txt after every interaction.
 
 Testing & Improvements:------------------------ 
 
 Uses gemini-1.5-pro-latest model- Dynamic prompts based on function- Opportunities to improve prompt design and user tracking
 
 Interface:----------- 
 
 -Dropdown function selector
 
 - Text area for input
 
 - Feedback submission form
 
 - Responsive display and styling
 
 License:-------

 This project is for educational use only.
 
 Acknowledgements:------------------ 
 
 Google Gemini API- Flask Web Framework- Font Awesome & Google Fonts
