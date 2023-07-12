python -m pip install -r requirements.txt
pyinstaller --noconfirm --onedir --console --uac-admin --add-data "chromedriver.exe;."  "main.py"
pause