import pyautogui

# countdown(n): countdown for n seconds before start
# pyautogui.countdown(3)
# print("start")

# alert(): error message
pyautogui.alert("failed!", "error")

# confirm(): confirm message
result = pyautogui.confirm("continue?", "confirm")
print(result)  # OK : Cancel

# prompt(): get input from users
result = pyautogui.prompt("input", "input")
print(result)  # inputted data : None

# password(): get password from users
result = pyautogui.password("input", "input")
print(result)  # inputted data : None
