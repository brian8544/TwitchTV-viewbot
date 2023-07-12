@echo off
setlocal enabledelayedexpansion

:: Define the path to the Chrome driver executable
set "driver_path=%~dp0chromedriver.exe"

:: Get the list of running processes
for /f "tokens=2" %%a in ('tasklist /fi "imagename eq chrome.exe" /nh') do (
  :: Check if the process is associated with the Selenium-driven Chrome instances
  tasklist /fi "pid eq %%a" /v | findstr /i /c:"!driver_path!" >nul
  if errorlevel 1 (
    :: Close the Chrome process
    taskkill /PID %%a /F
  )
)

endlocal
pause
exit
