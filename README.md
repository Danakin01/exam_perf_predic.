# 🎓 Exam Performance Prediction  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/scikit--learn-ML-yellow?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" />
</p>

<p align="center">
  A machine learning project for <b>predicting student exam performance</b> based on academic, social, and personal factors.  
  The goal is to identify which variables influence scores and help improve educational outcomes.  
</p>

---

## 🧠 About
This project predicts **student exam scores** using a dataset of academic and socio-demographic features such as **hours studied, attendance, parental involvement, internet access, tutoring, and more**.  
By analyzing these factors, the model provides insights that can guide **educators, parents, and policymakers** in supporting students effectively.  

---

## ✨ Features
- 📊 **20 input features** covering academic, social, and lifestyle factors.  
- 🤖 Trains machine learning models to predict exam scores.  
- 📈 Supports regression and classification experiments.  
- 🔍 Explores the effect of features like **attendance, tutoring, and motivation** on outcomes.  
- 📑 Provides EDA, visualizations, and model performance metrics.  

---

## 📊 Dataset
The dataset contains **20 features** + `Exam_Score` (target). Example features:  

- `Hours_Studied` → Number of study hours per week  
- `Attendance` → % attendance in school  
- `Parental_Involvement` → Low / Medium / High  
- `Access_to_Resources` → Low / Medium / High  
- `Extracurricular_Activities` → Yes / No  
- `Sleep_Hours` → Avg sleep per night  
- `Previous_Scores` → Last exam performance  
- `Motivation_Level` → Low / Medium / High  
- `Internet_Access` → Yes / No  
- `Tutoring_Sessions` → Number of extra lessons attended  
- `Family_Income` → Low / Medium / High  
- `Teacher_Quality` → Low / Medium / High  
- `School_Type` → Public / Private  
- `Peer_Influence` → Positive / Neutral / Negative  
- `Physical_Activity` → Hours of exercise per week  
- `Learning_Disabilities` → Yes / No  
- `Parental_Education_Level` → High School / College / Postgraduate  
- `Distance_from_Home` → Near / Moderate / Far  
- `Gender` → Male / Female  

Target:  
- `Exam_Score` → Final exam score (numeric)  

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/Danakin01/exam_perf_predic..git
cd exam_perf_predic.

# (Optional) Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```
🚀 Usage
Open the notebook or script:


```bash
jupyter notebook exam_prediction.ipynb
Train and evaluate models.

Visualize relationships between features and exam scores.

Test predictions on new student data.
```

🗂️ Project Structure
``` kotlin

exam_perf_predic./
│── data/
│   └── exam_dataset.csv
│── exam_prediction.ipynb
│── requirements.txt
└── README.md
```
🛠️ Dependencies
Package	Purpose
pandas	Data analysis
numpy	Numerical operations
matplotlib	Data visualization
seaborn	Statistical plotting
scikit-learn	Machine learning models

📝 Notes
Can experiment with different ML algorithms (Linear Regression, Random Forest, Gradient Boosting, etc.).

EDA helps reveal feature importance (e.g., study hours, attendance, motivation).

Dataset can be extended with larger samples for better generalization.

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Fork the repo

Create a feature branch (git checkout -b feature/YourFeature)

Commit changes (git commit -m "Add feature")

Push (git push origin feature/YourFeature)

Open a Pull Request

📧 Contact
💡 Issues & PRs welcome!

📩 Email: danielakinwande00@gmail.com
🌐 GitHub: Danakin01
🔗 LinkedIn: Daniel Akinwande

<p align="center">Built with ❤️ by <b>DANAKIN</b></p> ```
