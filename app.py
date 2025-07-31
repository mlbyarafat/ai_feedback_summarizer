from flask import Flask, render_template, request, jsonify
from summarizer import summarize_text
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["feedback"]
    summary = summarize_text(text)
    sentiment = analyze_sentiment(text)
    return jsonify({"summary": summary, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
