# Gena

<img src="architecture/doc/images/icon/icon_128.png">

![Hits-of-Code](https://hitsofcode.com/github/aparovyshnaya/gena?branch=main) ![Apache-2.0 License](https://img.shields.io/badge/License-Apache--2.0-brightgreen.svg) ![GitHub release](https://img.shields.io/github/release/AParovyshnaya/gena)

Gena generate online catalog from data.json. Language are Python 3, JSON for data and HTML & JS & CSS for web-catalog.

# How assemble Gena?

You need [Python 3.7 +](https://www.python.org/downloads/) and [PyInstaller 4.2 +](#How install PyInstaller).

Open directory `gena/gena/src`. Use this command:

```
pyinstaller -F --icon=icon.ico main.py 
```
`-F` create one script in one file. `--icon=icon.ico` install `icon.ico` for main.exe like icon. Main .py file - `main.py`.

You will have `main.spec`, `build` and `dist` directories. You will can find in `dist` `main.exe`.
 
# How install PyInstaller

PyIntaller is Python Libriry, so just write that:

```
pip install pyinstaller
```

You can check version with this command:

```
pyinstaller --version
```
