echo off

:: Delete pyinstaller folders and files, to make sure every compile is fresh
rmdir /s /q build
rmdir /s /q dist
del main.spec
cls

:: Compilation start
python -m pip install -r requirements.txt
pip-upgrade requirements.txt
pyinstaller --noconfirm --onedir --console --icon "contrib/images/twitch.ico" --add-data "chromedriver.exe;." --add-data "cleanup.bat;."  "main.py"

:: Cleanup
rmdir /s /q build
del main.spec

:: Open folder for end-user
cd /d dist\main
start .

pause
exit