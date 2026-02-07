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