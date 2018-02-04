Command to create .exe from .py:
--------------------------------
pyinstaller --onefile --noconsole -i iconFilename.ico filename.py

* When the "--noconsole" switch is provided,
no console will be created for stdin/stdout.
The GUI must handle all user interactions.


Command to install PyInstaller:
-------------------------------
pip install pyinstaller