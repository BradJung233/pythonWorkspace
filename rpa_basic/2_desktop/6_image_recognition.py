import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png") # 해당이미지로 마우스커서 이동
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)   # 파일을 찾지 못할 경우 "None" return

# for i in pyautogui.locateAllOnScreen("checkbox.png"): # 동일한 이미지 모두 찾기
#     print(i)
#     pyautogui.click(i, duration=0.25)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True) # grayscale=True 이미지를 흑백으로 전환해서 비교함. 속도 측면 유리
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height)
# pyautogui.moveTo(trash_icon)

# 1488,623
# 1881,760

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90% 이상 이미지 일치
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")    

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)    

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None 
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target        

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")     
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 1)


