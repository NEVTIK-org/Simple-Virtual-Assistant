cd /D "%~dp0"
data\python-3.8.1-amd64.exe
copy data\JANE.lnk "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
copy data\swigwin-3.0.12\Lib\*.swg "%userprofile%\AppData\Local\Programs\Python\Python38\Lib"
copy data\swigwin-3.0.12\Lib\python\* "%userprofile%\AppData\Local\Programs\Python\Python38\Lib"
xcopy data\swigwin-3.0.12\Lib\typemaps "%userprofile%\AppData\Local\Programs\Python\Python38\Lib"
python -m pip install --upgrade pip setuptools wheel
pip install --upgrade pocketsphinx
pip install playsound
pip install SpeechRecognition
pip install gTTS
