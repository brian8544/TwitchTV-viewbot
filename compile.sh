#!/bin/bash

# Delete pyinstaller folders and files, to make sure every compile is fresh
rm -rf build
rm -rf dist
rm main.spec

# Compilation start
python -m pip install -r requirements.txt
pip install --upgrade -r requirements.txt
pyinstaller --noconfirm --onedir --console --icon "contrib/images/twitch.ico" --add-data "chromedriver.exe:." --add-data "cleanup.bat:." "main.py"

# Cleanup
rm -rf build
rm main.spec

# Open folder for end-user
cd dist/main
xdg-open .

read -p "Press Enter to exit"
