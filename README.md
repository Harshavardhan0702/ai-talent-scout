# 🤖 AI-Powered Talent Scouting Agent

## 📌 Overview

This project is an AI-powered talent scouting system that helps recruiters automatically discover, evaluate, and rank candidates based on a job description.

It extracts required skills, matches candidates from a dataset, simulates candidate interest, and provides a ranked shortlist with explainability.

---

## 🚀 Features

* Extract skills from job descriptions
* Match candidates based on skills
* Simulate candidate interest (engagement)
* Provide explainability (matched & missing skills)
* Rank candidates using scoring logic
* Visualize rankings with charts

---

## 🧠 Architecture

```
Job Description Input
        ↓
Skill Extraction (utils.py)
        ↓
Candidate Dataset (candidates.json)
        ↓
Matching Algorithm
        ↓
Interest Simulation
        ↓
Scoring Engine
        ↓
Ranking Output (Streamlit UI)
```

---

## ⚙️ Scoring Logic

Final Score = 0.7 × Match Score + 0.3 × Interest Score

* Match Score → based on skill overlap
* Interest Score → simulated candidate response

---

## ▶️ How to Run Locally

1. Install dependencies:
   pip install streamlit

2. Run the app:
   streamlit run app.py

---

## 📊 Sample Input

Looking for a Python developer with Flask, Machine Learning, and SQL experience.

---

## 📈 Sample Output

* Extracted Skills: Python, Flask, SQL
* Top Candidate: Anjali
* Match Score: 100%
* Interest Score: 82
* Final Score: 94.6

---

## 🎥 Demo Video

(Add your video link here)

---

## 🌐 Project URL

Local setup instructions provided above.

---

## 📂 GitHub Repository

https://github.com/Harshavardhan0702/ai-talent-scout

---

## 👨‍💻 Author

Harshavardhan
