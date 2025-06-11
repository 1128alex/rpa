import pyautogui

for w in pyautogui.getAllWindows():
    print(w)

w = pyautogui.getWindowsWithTitle("x가계부.xlsx - Chrome")[0]

if w.isActive == False:
    w.activate()

pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("excel_file.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("create_a_copy.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("download_a_copy.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.rightClick(pyautogui.locateOnScreen("file_explorer.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("file_download.png", confidence=0.8))
pyautogui.sleep(0.7)

fw = pyautogui.getActiveWindow()
if fw.isMaximized == False:
    fw.maximize()
pyautogui.sleep(0.7)

pyautogui.write("x")
# pyautogui.click(
#     pyautogui.locateOnScreen("file_account_book.png", confidence=0.6), interval=2
# )
pyautogui.hotkey("ctrl", "x")
pyautogui.sleep(0.7)

pyautogui.doubleClick(pyautogui.locateOnScreen("cs.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.doubleClick(pyautogui.locateOnScreen("automation.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.doubleClick(
    pyautogui.locateOnScreen("account_book_folder.png", confidence=0.8)
)
pyautogui.sleep(0.7)

pyautogui.click(pyautogui.locateOnScreen("view.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("list_view.png", confidence=0.8))
pyautogui.sleep(0.7)
pyautogui.click(800, 500)
pyautogui.write("1")
pyautogui.sleep(0.7)
pyautogui.click(pyautogui.locateOnScreen("trashcan.png", confidence=0.8))
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
