import pyautogui

for w in pyautogui.getAllWindows():
    print(w)

w = pyautogui.getWindowsWithTitle("x가계부.xlsx - Chrome")[0]

if w.isActive == False:
    w.activate()

pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/excel_file.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/create_a_copy.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/download_a_copy.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.rightClick(
    pyautogui.locateOnScreen("images/file_explorer.png", confidence=0.8)
)
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/file_download.png", confidence=0.8))
pyautogui.sleep(0.7)

fw = pyautogui.getActiveWindow()
if fw.isMaximized == False:
    fw.maximize()
pyautogui.sleep(0.7)

pyautogui.write("x")
pyautogui.hotkey("ctrl", "x")
pyautogui.sleep(0.7)

pyautogui.doubleClick(pyautogui.locateOnScreen("images/cs.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.doubleClick(pyautogui.locateOnScreen("images/automation.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.doubleClick(
    pyautogui.locateOnScreen("images/account_book_folder.png", confidence=0.8)
)
pyautogui.sleep(0.7)

pyautogui.click(pyautogui.locateOnScreen("images/view.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/list_view.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(800, 500)
pyautogui.write("1")
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("images/trashcan.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(800, 500)
pyautogui.sleep(0.7)
pyautogui.hotkey("ctrl", "v")
pyautogui.sleep(0.7)
pyautogui.write("x")
pyautogui.sleep(0.7)
pyautogui.write(["F2"])
pyautogui.sleep(0.7)
pyautogui.write("1account_book")
pyautogui.sleep(0.7)
pyautogui.write(["enter"])
pyautogui.sleep(0.7)
pyautogui.hotkey("ctrl", "w")
