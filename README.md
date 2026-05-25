<div align="center">

# 🧠 Personality Classifier

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-App-FF6B6B?style=for-the-badge&logo=gradio)](https://gradio.app)
[![scikit-learn](https://img.shields.io/badge/Accuracy-92.93%25-success?style=for-the-badge)](https://scikit-learn.org)
[![HuggingFace](https://img.shields.io/badge/🤗-Live%20Demo-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/marwanthe0/Personality_Classifier)

**Predicts whether you are an Introvert or Extrovert based on 7 social behavior features — with 92.93% test accuracy.**

[🚀 Try Live Demo](https://huggingface.co/spaces/marwanthe0/Personality_Classifier) · [📖 Report Bug](https://github.com/Marwanthe0/Personality_Classifier/issues)

</div>

---

## ✨ Features

- Trained on a dataset of **2,900 records**
- Uses **7 social behavior features** (time alone, social event frequency, etc.)
- **92.93% test accuracy** with Random Forest + hyperparameter tuning
- Deployed as a **Gradio app on Hugging Face Spaces**
- Clean preprocessing pipeline with feature importance analysis

---

## 🔍 Input Features

| Feature | Type | Description |
|---------|------|-------------|
| Time Spent Alone | Numeric | Hours per day spent alone |
| Social Event Frequency | Numeric | Events attended per month |
| Going Outside Frequency | Numeric | Days per week outside |
| Friends Circle Size | Numeric | Number of close friends |
| Post Frequency on Social Media | Numeric | Posts per week |
| Stage Fright | Binary | Yes / No |
| Drained After Socializing | Binary | Yes / No |

---

## 🤖 Model Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | **92.93%** |
| Algorithm | Random Forest |
| Dataset Size | 2,900 records |
| Train/Test Split | 80/20 |

---

## ⚙️ Running Locally

```bash
git clone https://github.com/Marwanthe0/Personality_Classifier.git
cd Personality_Classifier
pip install -r requirements.txt
python app.py
```

Or run the FastAPI backend:
```bash
uvicorn main:app --reload
```

---

## 🗂️ Project Structure
Personality_Classifier/
│
├── app.py                  # Gradio interface
├── main.py                 # FastAPI backend
├── model_training.py       # Training script
├── personality_model.pkl   # Serialized model
├── dataset.csv             # Training data
├── requirements.txt
└── README.md
---

## 🙋 Author

**Shafikul Islam Marwan** · [LinkedIn](https://www.linkedin.com/in/marwanahmed27/) · [GitHub](https://github.com/Marwanthe0)

<div align="center">⭐ Star this repo if it helped you!</div>
