# This is Starter
# Used to start the server
# Imports
import sys
import uvicorn
import os

# Default path for linux
TERMUX = "storage/emulated/0/Movies"

# Check if args are passed correctly!
if len(sys.argv) < 2:
    print("Usage: python run.py /path/to/your/movies <--termux>")
    sys.exit(1)

pth = sys.argv[1]

# Init Environment
if sys.argv[1] == "--termux":
    os.environ["MOVIES_DIR"] = TERMUX
elif os.path.exists(pth):
    os.environ["MOVIES_DIR"] = pth
else:
    print('Argument Error: Please Enter valid location')
    sys.exit(1)

uvicorn.run(
    "server:app",
    host = "0.0.0.0",
    port = 8000
)