pip install pyinstaller
pyinstaller --noconfirm --onedir --console --add-data "source;." --add-data "resource;."  "main.py"
xcopy resource dist\\main\\resource\ /s /d
