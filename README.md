# 🌾 Crop Recommendation System

An AI-powered web application that predicts the most suitable crop to grow based on soil nutrients and weather conditions. This system helps farmers and agricultural enthusiasts make informed decisions for maximum yield and sustainability.

---

## 📺 Live Demo
[🌐 Visit the Live Website](https://krishi-ai-1.onrender.com)

---

## 📸 Example

> 📥 Input:
- Nitrogen: 90
- Phosphorus: 42
- Potassium: 43
- Temperature: 20.5°C
- Humidity: 80%
- pH: 6.5
- Rainfall: 120 mm

> 📤 Output:
**Recommended Crop:** `Rice`

---

## 📂 Project Structure
```
Crop-Recommendation-System/
├── app.py
├── crop_model.pkl
├── requirements.txt
├── Procfile
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── form.html
│   └── about.html
```

---

## 🧠 Tech Stack
- Python
- Flask (Backend Web Framework)
- HTML, CSS (Frontend UI)
- scikit-learn (Machine Learning)
- Render (Deployment)

---

## 🔍 Features
- 💡 AI-based crop prediction
- 📊 User-friendly form for data input
- 🌐 Fully responsive interface
- 📥 Real-time results
- 🇮🇳 Indian agriculture focused (can be localized)

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

---

## ☁️ Deployment on Render

### 1. Ensure These Files Exist
- `requirements.txt`
- `Procfile` with the content:
```
web: gunicorn app:app
```

### 2. Push to GitHub
```bash
git add .
git commit -m "Deploy-ready version"
git push origin main
```

### 3. Deploy on Render
- Go to [https://render.com](https://render.com)
- Click **New Web Service**
- Connect your GitHub repo
- Set Build Command: `pip install -r requirements.txt`
- Set Start Command: `gunicorn app:app`
- Choose Free Plan and Deploy

---

## 🧾 About the Project
This project was developed by students of **D Y Patil University Pune, Ambi - School of Engineering & Technology** under the guidance of **Prof. Shakil Tamboli** as a Smart Farming innovation.

### 👨‍💻 Team Members
- Saurabh Kumar
- Navneet Sinha
- Anjali Kumari
- Shreya Kunjir

---


## 🙌 Support & Feedback
Have feedback or need help?
Open an [issue](https://github.com/mrsaurabh009/your-repo/issues) or drop us a message.

---

> "Empowering farmers with AI to grow smarter, not harder."

