
# 🧠 AI Feedback Summarizer

This AI-powered web application allows users to submit feedback text and receive a concise summary along with sentiment analysis (positive, negative, or neutral). It's built with Python and Flask and leverages powerful NLP models.

## 🚀 Features

- ✂️ **Text Summarization** using HuggingFace Transformers
- 😊 **Sentiment Analysis** with TextBlob
- 🌐 **Simple Web Interface** via Flask and HTML templates
- 📦 **Easy Deployment** with `requirements.txt`

## 📁 Project Structure

```
ai_feedback_summarizer/
├── app.py                  # Flask backend
├── summarizer.py           # HuggingFace summarizer logic
├── sentiment.py            # Sentiment analyzer using TextBlob
├── templates/
│   └── index.html          # Web UI template
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🛠️ Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/mlbyarafat/ai_feedback_summarizer.git
cd ai_feedback_summarizer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://127.0.0.1:5000/
```

## 🧪 Sample Usage

- Input:  
  _"The course was informative, but it could use more real-world examples."_

- Output Summary:  
  _"The course was informative but needs more real-world examples."_

- Sentiment:  
  _Neutral_

## 📚 Tech Stack

- **Backend**: Python, Flask
- **NLP**: HuggingFace Transformers (`distilbart-cnn-12-6`), TextBlob, NLTK
- **Frontend**: HTML (Jinja Templates)
- **Deployment**: Localhost / Cloud-compatible

## 🙌 Author

**MD. ARAFAT**  
GitHub: [mlbyarafat](https://github.com/mlbyarafat)

---

⭐ _Feel free to fork, star, and contribute to this project!_
