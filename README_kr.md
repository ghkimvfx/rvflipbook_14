![rv_flipbook_read_node](https://github.com/user-attachments/assets/69a289ca-1303-4ae1-a445-b4daab114853)

## 📔설명
이 파이썬 코드는 기존 https://learn.foundry.com/nuke/developers/63/pythondevguide/flipbook.html 

문서에 있는 코드를 기준으로 작성되었습니다.

Nuke 14버전 이상에서 간헐적으로 동작하지 않았던 부분의 문법을 수정하여 Nuke 14 ~15 버전에서 작동하게 만들었습니다.

## ❓ 설치방법
1. `./nuke` 폴더에 `rv_flipbook.py`를 넣습니다
2. `menu.py`  에 다음과 같은 코드를 추가합니다.
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

3. 환경변수설정을 들어갑니다.
<br> 참조 링크 : https://www.computerhope.com/issues/ch000549.htm
4. 시스템 변수의 Path 항목에 다음과 같은 경로를 추가합니다. <br>
`C:\Program Files\Shotgun\RV-7.1.1\bin`
<br>중요 : 위의 경로는 현재 아티스트의 컴퓨터에 설치된 RV의 경로를 뜻합니다.

만약 Open RV를 사용하거나 다른 버전의 RV를 사용하신다면 설치된 경로로 변경하셔야 합니다.

## ⚠️중요사항
만약 설치된 RV의 버전이 다르거나 설치된 경로가 다르다면 반드시
`rv_flipbook.py`의 10번줄
``` 
 self._rvPath = "C:/Program Files/Shotgun/RV-7.1.1/bin/RV.exe"
```
의 항목을 정확한 경로로 바꾸어야 합니다.

- rv_flipbook.py의 경로 문법 “/”과 윈도우의 경로 “\”를 정확히 구분하셔야합니다

## 🖥️테스트된 환경
****Nuke | 14 v4 ~ 15.1 v5****
<br>
**Windows 10 ~ 11**

>⚠️맥 환경에서는 지원되지 않습니다.
<br>혹은 테스트가 되지않은 환경 (예: nuke 13이하 버전)에서는 동작하지 않을 수 있습니다.

## ☀️사용방법
Read 노드를 선택한 상태로 Alt+F를 누르시고, Flipbook 창에서 RV를 선택 후 OK를 누르면 RV가 flipbook모드로 실행되며 작동합니다.

Tip : 작업한 컴프를 확인하려면 미리 렌더를 하고 사용을 하는 것이 좋습니다.
<br> Read 노드를 제외한 다른 노드에서 사용해도 되지만 **캐싱시간이** 소요됩니다.
### 캐싱시간예시
![rv_flipbook_other](https://github.com/user-attachments/assets/748de9db-b57b-45a7-a922-8f164adb4f9a)
<br> 다음과 같이 캐싱시간이 걸리게됩니다.


## 🕷️버그 리포트
만약 사용중 버그나 작동하지 않는 부분이 있다면
<br> 사용하고 계신 누크, 윈도우의 버전과 함께
<br> gihan.kim.vfx@gmail.com으로 연락 부탁드립니다.
<br> <br> 감사합니다.
