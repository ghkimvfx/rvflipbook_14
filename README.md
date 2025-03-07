[Kor Description, 한국어설명](https://github.com/ghkimvfx/rvflipbook_14/blob/master/README_kr.md)

![ezgif-79c48a9c5b6186](https://github.com/user-attachments/assets/19d58cce-017e-4d14-9c7e-a4973b399bb1)
## 📔Description
This Python code is based on the existing 

https://learn.foundry.com/nuke/developers/63/pythondevguide/flipbook.html 

documentation.

I've modified the syntax where it intermittently didn't work in Nuke 14 and later to make it work in Nuke 14-15.

## ❓ How to set up
1. Import `rv_flipbook.py` in the `./nuke` folder
2. Add the following code to `menu.py`
```python
import nuke
import nukescripts
import os

try:
    import rv_flipbook
    nuke.tprint("RV Flipbook Loaded Successfully!")
except Exception as e:
    nuke.tprint(f"Error loading RV Flipbook: {e}")
```

3. Set the path and environment variables in Windows
<br> Reference Links  : https://www.computerhope.com/issues/ch000549.htm
4. Add the following path to the Path entry in System Variables: <br>
`C:\Program Files\Shotgun\RV-7.1.1\bin`
<br>IMPORTANT: The path above refers to the path to the RV currently installed on your computer.

If you are using Open RV or a different version of RV, you will need to change it to the installed path for it to work.

## ⚠️Important Notes
If the installed RV version is different or the installed path is different, you must change the entry in line 10 of `rv_flipbook.py`
``` 
 self._rvPath = "C:/Program Files/Shotgun/RV-7.1.1/bin/RV.exe"
```
to the correct path.

- You must distinguish between the path syntax “/” in rv_flipbook.py and the path “\” in Windows.

## 🖥️Tested environment
****Nuke | 14 v4 ~ 15.1 v5****
<br>
**Windows 10 ~ 11**

>⚠️Not supported on Mac.
<br>Or may not work on untested environments (e.g. nuke 13 or lower).

## ☀️How to use
With the Read node selected, press Alt+F, select RV in the Flipbook window, and then press OK. RV will run in flipbook mode and work.

Tip: To check the comp you worked on, it is recommended to render it in advance and use it.

### 🕷️Bug report
If you encounter any bugs or parts that do not work while using it, please contact us at the email address below along with the version of Nook and Windows you are using.

gihan.kim.vfx@gmail.com

Thank you



