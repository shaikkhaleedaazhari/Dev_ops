#!/bin/bash

VENV_NAME="myenv"

echo " Starting setup..."

if [ ! -d "$VENV_NAME" ]; then                                  #  environment if it doesn't exist
    echo "Creating virtual environment: $VENV_NAME..."             #If multiple requirements.txt files exist, it picks the first one.
    python -m venv $VENV_NAME 
else
    echo "Virtual environment already exists."
fi

echo " Activating virtual environment..."
source $VENV_NAME/Scripts/activate

echo " Upgrading pip..."
python -m pip install --upgrade pip

REQUIREMENTS_PATH=$(find .. -name "requirements.txt" | head -n 1)            #finds the first requirements.txt in the parent directory

if [ -f "$REQUIREMENTS_PATH" ]; then
    echo " Installing dependencies from $REQUIREMENTS_PATH..."
    pip install -r "$REQUIREMENTS_PATH"
else
    echo " Error: requirements.txt not found!"
    exit 1
fi

echo " Starting Flask application..."
python web.py


