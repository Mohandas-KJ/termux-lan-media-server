# This is Starter
# Used to start the server
# Imports
import sys
import uvicorn
import os

Gate = False

# Default path for linux
TERMUX = "storage/emulated/0/Movies"

# Check if args are passed correctly!
if len(sys.argv) < 2:
    print("Usage: python run.py /path/to/your/movies <--termux>")
    sys.exit(1)

# Init Environment
if sys.argv[1] == "--termux":
    os.environ["MOVIES_DIR"] = TERMUX
    Gate = True
else:
    os.environ["MOVIES_DIR"] = sys.argv[1]
    Gate = True

if not Gate:
    print("Argument Error. Please recheck")
    sys.exit(1)