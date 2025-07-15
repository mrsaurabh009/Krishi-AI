
# 🌾 Krishi AI – Crop Recommendation System

An AI-powered web application that predicts the most suitable crop to grow based on soil nutrients and weather conditions. Built using Python, Flask, and scikit-learn, the system helps farmers make smarter agricultural decisions for better yield and sustainability.

---

## 🔗 Live Demo
> 🌐 [Krishi AI](https://krishi-ai-3025.onrender.com/)

---

## 📸 Example Usage
### 👨‍🌾 Input:
- Nitrogen: 90
- Phosphorus: 45
- Potassium: 50
- Temperature: 23.5°C
- Humidity: 80%
- pH: 6.5
- Rainfall: 120 mm

### 📈 Output:
**Recommended Crop:** `Rice`

---

## 🧠 Features
- ✅ AI-based crop recommendation using ML model
- 🌐 Responsive web interface (HTML + CSS)
- 🧪 Input form for soil and climate conditions
- 📥 Result display for most suitable crop
- 📦 Lightweight deployment-ready with Render

---

## 🏗️ Tech Stack
| Component       | Tech Used            |
|----------------|----------------------|
| Backend         | Flask (Python)       |
| Frontend        | HTML, CSS, FontAwesome |
| ML Model        | scikit-learn (RandomForest) |
| Deployment      | Render               |
| UI Animation    | CSS3 + Flexbox       |

---

## 📂 Project Structure
```
Krishi-AI/
├── app.py
├── crop_model.pkl
├── requirements.txt
├── Procfile
├── static/
│   ├── style.css
│   └── about.css
├── templates/
│   ├── index.html
│   ├── form.html
│   └── about.html
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/mrsaurabh009/Krishi-AI.git
cd Krishi-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App
```bash
python app.py
```

Open your browser and go to:
```
http://localhost:5000
```

---

## 🚀 Deploying to Render (Free Hosting)

### ✅ Prerequisites:
- GitHub repository
- `requirements.txt` with dependencies
- `Procfile` with:
  ```
  web: gunicorn app:app
  ```

### 🔧 Steps:
1. Go to [https://render.com](https://render.com)
2. Sign in and click **New Web Service**
3. Connect your GitHub repo
4. Fill in:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3.x
   - **Branch**: `main`
5. Click **Deploy**

After build, your live app URL will be ready.

---

## 🧪 Prediction Model
The model is trained using `RandomForestClassifier` on a dataset of agricultural conditions.
- Features used:
  - N, P, K values
  - Temperature
  - Humidity
  - pH
  - Rainfall
- Target: Best-suited crop

Saved as `crop_model.pkl`

---

## ✨ UI Highlights
- Responsive Navbar with dropdown
- Cards with icons (Font Awesome)
- Smooth animations and hover effects
- Prediction results displayed dynamically

---

## 👨‍🎓 Contributors
- **Saurabh Kumar** – [GitHub](https://github.com/mrsaurabh009) | [LinkedIn](https://www.linkedin.com/in/mrsaurabh009)


## 📜 License
[MIT License](LICENSE) – Use freely with attribution.

---

## 🙌 Support
If you like this project, leave a ⭐️ on [GitHub Repo](https://github.com/mrsaurabh009/Krishi-AI) and share with others!

> "Empowering farmers through AI – one crop at a time." 🌾
