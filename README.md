# **📦 termux-lan-media-server**
A lightweight LAN media & file upload server built with FastAPI, designed to run on:
- 🐧 Linux (Kali, Ubuntu, etc.)
- 🪟 Windows
- 📱 Android (Termux)

Supports:
- 📂 File uploads over HTTP
- 🎬 VLC-compatible media streaming
- 🔎 Interactive web UI (search, play, copy link)
- 📡 Byte-range streaming (206 Partial Content → seeking works)

## 🚀 Why This Project?
SMB was painful.  
Storage on old Android was limited.  
OS switching was inconvenient.

So this project provides:  
A simple HTTP-based LAN media server that works across all devices without OS dependency.

## 🏗 Architecture
```scss
Client (Phone / VLC / Browser)
        │
        ▼
   FastAPI Server
        │
        ▼
   Movies Directory (Custom Path)
```

- Backend: Python + FastAPI
- Frontend: HTML + CSS + Vanilla JS
- Streaming: HTTP Range Requests
- Protocol: Pure HTTP (no SMB)

## 📁 Project Structure
```pgsql
termux-lan-media-server/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── doc/
│   └── dev-notes.md
│
├── src/
│   ├── main.py          # Entry point (uvicorn target)
│   ├── config.py        # Environment + settings
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── app.js
│
└── run.py               # Optional launcher script

```