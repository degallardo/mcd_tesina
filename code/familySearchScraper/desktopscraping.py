from turtle import isvisible
import pyautogui
import time, json, os, datetime
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#----SELENIUM-----#
v_settings = None
with open('config.json', 'r') as read_json:
    v_settings = json.load(read_json)
    print(v_settings['edge_driver'])

options = EdgeOptions()
options.use_chromium = True
options.add_argument('start-maximized')

browser = webdriver.Edge(v_settings['edge_driver'], options=options)
# browser.implicitly_wait(3) # seconds
browser.get('https://www.familysearch.org/es/')

# time.sleep(3)
wait = WebDriverWait(browser, 10)
truste_consent_button = wait.until(EC.element_to_be_clickable((By.ID, 'truste-consent-button')))
truste_consent_button.click()
# browser.find_element(By.ID, 'truste-consent-button').click()

signInLink = wait.until(EC.element_to_be_clickable((By.ID, 'signInLink')))
signInLink.click()
# browser.find_element(By.ID, 'signInLink').click()

userName = wait.until(EC.element_to_be_clickable((By.ID, 'userName')))
userName.send_keys('dgallardo')

password = browser.find_element(By.ID, 'password')
password.send_keys('noidgaar')

submit_button = browser.find_element(By.NAME, 'submitButton')
submit_button.click()

# Leemos el ardhivo datasets.json para obtener las urls del archivo.
with open("datasets.json", 'r') as json_file:
    urls_data = json.load(json_file)
    print(urls_data['main_folder'])
    for urls in urls_data['urls']:
        if urls["active"] == True:
            print(urls["url"])
            print(urls["img_qty"])
            print(urls["folder"])

            # browser.get('https://www.familysearch.org/records/images/image-details?page=1&place=2945258&lifeEvent=102860&rmsId=M989-TG6&imageIndex=0&singleView=true')
            browser.get(urls["url"])

            # fs_image_viewer = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fs-image-viewer__overlay-rects')))

            # is_download_path_set = pyautogui.confirm('Asegurate de tener la carpeta de descargas configurada en el navegador.')
            time.sleep(10)

            fs_image_viewer_tools = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div[2]/div/div[2]/fs-single-image-viewer/div[5]/div[1]/fs-image-viewer-control[5]')))
            fs_image_viewer_tools.click()

            i_img_total = int(urls["img_qty"])
            i_img_counter = 1
            s_folder = urls["folder"]

            while i_img_counter <= i_img_total:
                fs_image_viewer_download = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'download')))
                if not fs_image_viewer_download.is_displayed():
                    fs_image_viewer_tools = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div[2]/div/div[2]/fs-single-image-viewer/div[5]/div[1]/fs-image-viewer-control[5]')))
                    fs_image_viewer_tools.click()

                fs_image_viewer_download.click()

                ly_navbar__next = browser.find_element(By.CLASS_NAME, 'ly-navbar__next')
                ly_navbar__next.click()

                i_img_counter += 1

                time.sleep(8)


            dest_folder = os.path.join(urls_data['main_folder'], urls["folder"])

            if not os.path.isdir(dest_folder):
                # os.makedirs(os.path.join(urls_data['main_folder'], urls["folder"]))
                print("Creating folder " + dest_folder + "...")
                os.makedirs(dest_folder)
                print("Folder " + dest_folder + " has been created.")

            download_folder = r"C:\Users\sesa443933\Downloads"
            print("Moving files from " + download_folder + " to " + dest_folder + "...")
            for file in os.listdir(download_folder):
                if datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(download_folder, file))).strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d"):
                    # print(file, datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(download_folder, file))).strftime("%Y-%m-%d"))
                    fl_from = os.path.join(download_folder, file)
                    fl_to = os.path.join(dest_folder, file)
                    print("Moving " + fl_from + " to " + fl_to + "...")
                    os.replace(fl_from, fl_to)

browser.close()

#----SELENIUM-----#

def move_files(source_dir, dest_dir):
    pass


def manual_scrape():
    t_start_time = time.time()

    pyautogui.PAUSE = 3.5
    pyautogui.FAILSAFE = True

    confirm_star = pyautogui.confirm('¿Tienes la página lista para empezar a descargar imágenes?')

    if confirm_star == 'OK':
        s_img_total = pyautogui.prompt('¿Cuantas imágenes hay en el lote?')
        s_save_pathyn = pyautogui.confirm('¿Quieres especificar el folder donde se guardaran las imágenes? OK = SI Cancel = NO')
        if s_save_pathyn == 'OK':
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
                    if s_save_pathyn == 'OK':
                        pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/saveas.png', confidence=0.9))
                        if i_img_counter == 1:
                            pyautogui.typewrite(s_save_path)
                            pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/save.png', confidence=0.9))
                        pyautogui.click(pyautogui.locateCenterOnScreen('code/familySearchScraper/img/save.png', confidence=0.9))
                    i_img_counter += 1
        else:
            pyautogui.alert('El valor capturado deber ser un número entero.')

    t_end_time = time.time()

    print(t_start_time)
    print(t_end_time)
    print(t_end_time - t_start_time)