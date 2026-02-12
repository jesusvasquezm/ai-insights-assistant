# 🤖 AI Insights Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black)
![Status](https://img.shields.io/badge/Status-Active-success)

A full-stack AI-powered text analysis application built with modern web technologies.

This project demonstrates backend integration with OpenAI, structured error handling, and a resilient fallback system designed to keep the application functional even when external APIs fail.

---

## 🚀 Tech Stack

### 🔹 Frontend
- React
- Vite
- TypeScript
- Fetch API

### 🔹 Backend
- FastAPI
- Python
- OpenAI API
- Pydantic
- CORS Middleware

---

## ✨ Features

- ⚡ Real-time text analysis  
- 🤖 OpenAI API integration  
- 🛡️ Automatic fallback system (Mock Mode)  
- 📄 REST API documented with Swagger  
- 🔐 Environment variable configuration  
- 🎯 Clean and minimal UI  

---

## 🧠 Architecture

```
User Input (React Frontend)
        ↓
FastAPI Backend
        ↓
OpenAI API
```

If the OpenAI quota is exceeded, the system automatically switches to **Mock Mode**, ensuring the application continues to operate without crashing.

---

## 📂 Project Structure

```
ai-insights-assistant/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── package.json
│
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file inside the `backend` folder:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit your real `.env` file.

---

## 🖥️ How to Run Locally

### 1️⃣ Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 📈 What I Learned

- Full-stack communication (Frontend ↔ Backend)
- REST API design with FastAPI
- OpenAI API integration
- Error handling patterns
- CORS configuration
- Environment variable management
- Debugging real-world API failures (429, 500)

---

## 🎯 Future Improvements

- Authentication system  
- Database integration (history storage)  
- Deployment (Render + Vercel)  
- Improved UI/UX  
- Advanced AI prompt engineering  

---

## 👨‍💻 Author

**Jesús Vásquez Medina**  
Frontend Developer | React | TypeScript | AI Integration  

---

⭐ If you found this project interesting, feel free to connect with me on LinkedIn.
