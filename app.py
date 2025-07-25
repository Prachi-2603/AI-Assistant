from flask import Flask, render_template, request
from gemini_helper import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        function = request.form["function"]
        user_input = request.form["user_input"]

        # Define prompts for different functions
        if function == "answer":
            prompt = f"Answer this question: {user_input}"
        elif function == "summarize":
            prompt = f"Summarize the following text: {user_input}"
        elif function == "creative":
            prompt = f"Generate a creative content based on this input: {user_input}"
        else:
            prompt = user_input

        response = generate_response(prompt)

    return render_template("index.html", response=response)

@app.route("/feedback", methods=["POST"])
def feedback():
    user_feedback = request.form["feedback"]
    with open("feedback_log.txt", "a") as file:
        file.write(user_feedback + "\n")
    return "Thank you for your feedback!"

if __name__ == "__main__":
    app.run(debug=True)


