# 📊 Telecom Churn Prediction Dashboard

An **end-to-end Machine Learning project** that predicts customer churn and presents results through an **interactive Streamlit dashboard** with a **Power BI–style dark user interface**.

This project demonstrates how machine learning models can be integrated into **real-world business dashboards** to support **customer retention and data-driven decision making**.

---

## 🚀 Key Features

- End-to-end ML pipeline (**data → model → dashboard**)
- Customer churn prediction (**Churn / Stay**)
- Probability-based churn risk estimation
- Interactive Streamlit dashboard
- Custom dark theme using CSS (Power BI–inspired UI)

---

## 🛠️ Technologies Used (Tech Stack)

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Custom CSS**

---

## 📂 Project files

- **telco_churn.csv**
- **app.py**
- **style.css**
- **train_model.py**
- **churn_model.pkl**
- **requirements.txt**
- **README.md**


---

## ⚙️ How It Works

1. Customer data is cleaned, preprocessed, and encoded
2. A **Logistic Regression** model is trained on historical data
3. The trained model is saved using **joblib**
4. Streamlit loads the trained model
5. Churn predictions are generated in **real time**
6. Results are displayed in a **clean, business-friendly dashboard**

---


## 🧩 Installation Instructions

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/telecom-churn-dashboard.git
cd telecom-churn-dashboard
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Train the Model
```bash
python train_model.py
```
### ▶️ Usage Guide
Run the Dashboard
```bash
python -m streamlit run app.py
```
Open your browser and go to:
```bash
http://localhost:8501
```
### 3️⃣ Train the Model
```bash
python train_model.py
```
### Sample Input Values


- **Gender: Female**
- **Age: 34**
- **Weekly Minutes Watched: 200**
- **Videos Watched: 14y**
- **Customer Support Calls: 2**
- **Days Subscribed: 2**
  
### 📈 Output

- **Churn Prediction: Yes / No**
- **Risk Probability: Percentage-based churn likelihood**

### 💡 Use Case

 This dashboard can help businesses to:

- **Identify high-risk customers**
- **Improve customer retention strategies**
- **Support data-driven business decisions**
- **Demonstrate ML deployment skills for internships and entry-level roles**

### 🔮 Future Improvements

- **Train the model using all dashboard input features**
- **Add feature importance visualization**
- **Deploy the application on Streamlit Cloud**
- **Include historical churn analytics and trends**


## 👤 Author

**Guru Patel**

Data Science & Analytics Intern
