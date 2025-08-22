# 🛡️ Spam/Ham Email Classifier (Flask + ML)

This project is a **Machine Learning-powered Spam/Ham Classifier** built with **Flask**.  
It uses **Naive Bayes Classification** on text data to detect whether an email/message is spam or not.

---

## 🚀 Features
- 📩 Classifies text as **Spam** or **Ham (Not Spam)**
- 🧠 Trains a **Naive Bayes model** with `CountVectorizer`
- 📊 Uses dataset (`spam_ham_dataset.csv` / `spambase.data`)
- 🌐 Web interface with **Flask**
- 🔄 Real-time user input classification
- ⚡ Simple UI (enter message → get prediction)

---

## 🧑‍💻 Technologies Used
- **Python 3.x**
- **Flask** (for web app)
- **Scikit-learn** (Naive Bayes, CountVectorizer)
- **Pandas, NumPy**
- **HTML/CSS** (frontend templates)

---

## 📂 Project Structure

---

## 🔧 Setup Instructions

### ✅ Prerequisites
- Python (>=3.8)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
# Clone the repo
git clone https://github.com/your-username/spam-ham-classifier.git
cd spam-ham-classifier

# Run Flask app
python app.py
