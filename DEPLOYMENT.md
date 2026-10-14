# 🚀 FIELDAI — Production Deployment Guide

This guide explains how to deploy **FIELDAI** to **Render** or **Railway** (free cloud web services with custom domains and automatic HTTPS).

---

## 🌟 Option A: Deploy to Render (Recommended Free Web Service)

Render automatically detects the [`render.yaml`](file:///c:/Users/sherr/.gemini/antigravity/scratch/fieldai/render.yaml), [`Procfile`](file:///c:/Users/sherr/.gemini/antigravity/scratch/fieldai/Procfile), and [`requirements.txt`](file:///c:/Users/sherr/.gemini/antigravity/scratch/fieldai/requirements.txt) in this repository.

### Step 1: Push your code to GitHub

If you haven't created a GitHub repository yet:
1. Open [github.com/new](https://github.com/new) and create a new repository named `fieldai`.
2. In your terminal, run:
```powershell
cd C:\Users\sherr\.gemini\antigravity\scratch\fieldai
& "C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/fieldai.git
& "C:\Program Files\Git\cmd\git.exe" push -u origin main
```

### Step 2: Connect to Render

1. Go to [dashboard.render.com](https://dashboard.render.com) (sign in with GitHub).
2. Click **New +** ➔ **Web Service**.
3. Select your `fieldai` repository.
4. Render will auto-fill:
   - **Name:** `fieldai`
   - **Region:** Singapore / Oregon / Frankfurt
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
5. Select the **Free** instance type.
6. Click **Deploy Web Service**.

Within 2 minutes, your application will be live at:
`https://fieldai-xxxx.onrender.com`

---

## 🚂 Option B: Deploy to Railway

Railway provides continuous deployments and free SSL certificates.

1. Go to [railway.app](https://railway.app) and sign in with GitHub.
2. Click **New Project** ➔ **Deploy from GitHub repo**.
3. Select `fieldai`.
4. Railway will automatically detect [`Procfile`](file:///c:/Users/sherr/.gemini/antigravity/scratch/fieldai/Procfile) and [`requirements.txt`](file:///c:/Users/sherr/.gemini/antigravity/scratch/fieldai/requirements.txt).
5. In your project settings, click **Generate Domain** to get a public URL (e.g. `https://fieldai.up.railway.app`).

---

## ⚡ Option C: Instant Live Public URL (10 Seconds)

If you want to test and share FIELDAI on your mobile phone or with colleagues **right now** without waiting for cloud builds:

Run this command in PowerShell (uses built-in Windows OpenSSH):
```powershell
ssh -R 80:localhost:5050 nokey@localhost.run
```
or
```powershell
ssh -p 443 -R0:localhost:5050 a.pinggy.io
```

You will get an instant public `https://....localhost.run` URL that connects directly to your live running server!

---

## 🛠️ Environment Variables Reference

| Variable | Recommended Production Value | Description |
| :--- | :--- | :--- |
| `PORT` | `10000` (Render default) / `$PORT` | Web server listening port |
| `DEBUG` | `0` or `false` | Disables debug mode in production |
| `PYTHONUNBUFFERED` | `1` | Ensures real-time console log streaming |
