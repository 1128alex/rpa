import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# write(): write string
pyautogui.write("Hello World!")
pyautogui.write("Hello World!", interval=0.25)
# # No Korean yet
# pyautogui.write("나도 코딩")

# "left", "right", "enter": input keyboard
# https://automatetheboringstuff.com/2e/chapter20/
pyautogui.write(
    ["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25
)

# # how to write shift characters
# # ex) shift 4 -> $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# #  ex) ctrl a -> select all
# pyautogui.keyDown("ctrl")
# pyautogui.press("a")
# pyautogui.keyUp("ctrl")

# simplified
# pyautogui.hotkey("ctrl", "alt", "shift", "a")

# writing Korean
import pyperclip

pyperclip.copy("안녕!")
pyautogui.hotkey("ctrl", "v")

# end automation
# ctrl + alt + del
