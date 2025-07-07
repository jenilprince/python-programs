import pyautogui
pyautogui.moveTo(1090,1040)
pyautogui.click()
pyautogui.PAUSE = 1
pyautogui.moveTo(484,390,1)
pyautogui.PAUSE = 1
pyautogui.click()
pyautogui.moveTo(813,969,1)
pyautogui.click()
pyautogui.write("This is an automated message from Python", interval=0.09)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace", interval=0.1)

