# Imports
from fastapi import FastAPI, UploadFile, File              # Imports for Uploading, File Handling and API
from fastapi.responses import HTMLResponse, FileResponse   # Imports for Returning Response
import os,shutil        # Imports for OS level operations

# Storage Location
MOVIE_DIR = "/storage/Movies/"

# Defining API
app = FastAPI()

# Directory Creation
os.makedirs(MOVIE_DIR,exist_ok=True)

# Method for Home Directory
@app.get("/",response_class=HTMLResponse)
def Home():
    files = os.listdir(MOVIE_DIR)                       # Get the list of files
    file_list = "".join(f"<li>{f}<li>" for f in files)  # Create a list with HTML Tags

    # Return a HTML Page
    return f"""   
        <h2>LAN Server</h2
        <h3>Upload Movie</h3>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>

        <h3>Available Files</h3>
        <ul>{file_list}</ul>   
    """

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