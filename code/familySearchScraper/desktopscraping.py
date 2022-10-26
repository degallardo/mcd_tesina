import pyautogui
import time

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

confirm_star = pyautogui.confirm('¿Tienes la página lista para empezar a descargar imágenes?')

if confirm_star == 'OK':
    s_img_total = pyautogui.prompt('¿Cuantas imágenes hay en el lote?')
    s_save_path = pyautogui.prompt('¿En qué folder quieres guardar las imágenes?')
    if s_img_total.isdigit():
        i_img_total = int(s_img_total)
        if i_img_total > 0:
            i_img_counter = 1
            while i_img_counter <= i_img_total:
                if i_img_counter > 1:
                    pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/next.png', confidence=0.9))
                    # pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/previous.png', confidence=0.9))
                # time.sleep(2)
                if i_img_counter == 1:
                    pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/tools.png', confidence=0.9))
                pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/download.png', confidence=0.9))
                pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/saveas.png', confidence=0.9))
                if i_img_counter == 1:
                    pyautogui.typewrite(s_save_path)
                    pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/save.png', confidence=0.9))
                pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/save.png', confidence=0.9))
                i_img_counter += 1
    else:
        pyautogui.alert('El valor capturado deber ser un número entero.')