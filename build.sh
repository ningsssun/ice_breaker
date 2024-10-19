#!/bin/bash
# Check if the virtual environment already exists
if [ ! -d "venv" ]; then
    # Create the virtual environment
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run your app or any other build steps
python3 app.py
