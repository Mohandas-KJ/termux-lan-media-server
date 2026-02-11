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

## ⚙️ Installation
**1️⃣ Install dependencies**
```bash
pip install fastapi uvicorn python-multipart
```

## ▶️ Running the Server
**1️⃣ Use Launcher along with path**
```bash
python run.py /path/to/your/dir
```

## 🌐 Access the Server
Find Your IP:
```bash
ip a
```

Then open in browser
```cpp
http://YOUR_IP:8000
```

## 🎬 Streaming
- Click Play in UI
- Or copy link and open in VLC
```arduino
Media → Open Network Stream
```

Server supports:
```css
HTTP 206 Partial Content
```
- Seeking works
- Large files supported
- MKV / MP4 Supported

## 📤 Uploading Files
Use the web UI Upload Form
or
```bash
curl -F "file=@movie.mp4" http://IP:8000/upload
```

## 🧠 Technical Notes
- URL-encoded filenames supported
- Byte-range requests implemented
- Frontend dynamically re-renders movie list
- No database (filesystem-based)
- No authentication (LAN-only usage recommended)

## 🔐 Security Warning
This server is designed for:
- Local network usage only

Do NOT expose it directly to the public internet without:
- Authentication
- Reverse proxy
- HTTPS
- Firewall rules

## ❤️ Author

This project was built to:

- Explore JavaScript and modern web technologies alongside a cybersecurity background  
- Solve a real home-network media sharing problem  
- Avoid unreliable SMB behavior across multiple devices  
- Create a simple, universal HTTP-based solution  
- Support seamless usage across different operating systems  

This server was developed as a practical experiment in clean, minimal, cross-platform design.
