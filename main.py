from python_imagesearch import imagesearch
import pyautogui

while True:
    pos = imagesearch.imagesearch("target.png")
    if pos[1] != -1:
        pyautogui.click(pos[0] - 2560 + 50, pos[1] + 20, button="right")
        pyautogui.keyDown("shift")
        pos = imagesearch.imagesearch("delete.png")
        if pos[1] == -1:
            pos = imagesearch.imagesearch("delete_alt.png")
        if pos[0] != -1:
            pyautogui.click(pos[0] - 2560, pos[1])
        pyautogui.keyUp("shift")
