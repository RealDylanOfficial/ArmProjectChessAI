powershell.exe Start-Process -FilePath "python" -ArgumentList "./crap_ai/server.py" -NoNewWindow
powershell.exe Start-Process -FilePath "python" -ArgumentList "./main.py" -NoNewWindow -Wait
