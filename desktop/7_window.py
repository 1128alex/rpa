import pyautogui

# getActiveWindow(): get active window info
fw = pyautogui.getActiveWindow()

# get title of window
print(fw.title)
# get size of window
print(fw.size)
# get coordinates
print(fw.left, fw.top, fw.right, fw.bottom)
pyautogui.click(fw.left + 10, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

for w in pyautogui.getWindowsWithTitle("코딩"):
    print(w)

w = pyautogui.getWindowsWithTitle("코딩")[0]
print(w)
# activate(): activate window
if w.isActive == False:
    w.activate()

# maximize(): maximize window
if w.isMaximized == False:
    w.maximize()

# minimize(): minimize window
if w.isMinimized == False:
    w.minimize()

# restore(): restore window
w.restore()

# close(): close window
w.close()
