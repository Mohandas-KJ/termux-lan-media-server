# Imports
from fastapi import FastAPI, UploadFile, File              # Imports for Uploading, File Handling and API
from fastapi.responses import HTMLResponse, FileResponse   # Imports for Returning Response
import os,shutil        # Imports for OS level operations

# New Imports
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request

# Storage Location
MOVIE_DIR = os.getenv("MOVIES_DIR")

# Defining API
app = FastAPI()

# Directory Creation
os.makedirs(MOVIE_DIR,exist_ok=True)

# Mount Server Static Files
app.mount("/static",StaticFiles(directory="static"),name="static")

# Templates Folder
templates = Jinja2Templates(directory="templates")

# Method for Home Directory
@app.get("/",response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  # Return a .html template

# Method for listing the Contents of the directory
@app.get("/list")
def list_movies():
    files = sorted(os.listdir(MOVIE_DIR))  # List all the files in the directory
    return {"files": files}  # Return a response in the form of a dictionary

# Method for uploading
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    dest = os.path.join(MOVIE_DIR,file.filename)  # Upload File Destination

    with open(dest,"wb") as buffer:           # Open a New File with the Path
        shutil.copyfileobj(file.file,buffer)  # Write to the file
    
    return {"status":"uploaded","file":file.filename}  # Return response

# Method for Streaming the file
@app.get("/play/{filename}")
def play(filename: str):
    path = os.path.join(MOVIE_DIR,filename)  # Get the File
    return FileResponse(path, media_type="video/mp4")  # Return the File