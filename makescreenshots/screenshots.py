import pyautogui, time
time.sleep(6)

screenshot = pyautogui.screenshot()
screenshot.save("screenshot1.png")
print("I just took a screenshot!")
screenshot.save("screen2.png")
print("I just took 2 screenshots!")