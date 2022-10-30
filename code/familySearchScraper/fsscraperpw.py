# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("https://www.familysearch.org/es/")
#         print(await page.title())
#         await browser.close()

# asyncio.run(main())


# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()

import os, datetime

# dest_folder = os.path.join("C:\\Users\\sesa443933\\OneDrive - Schneider Electric\\MCD\\Tetra 5\\Proyecto de Consultoria\\dataset\\", "Apodaca. Marriage Records 1891-1900")
# print(dest_folder)
# os.makedirs(dest_folder)

print(datetime.datetime.now().strftime("%Y-%m-%d"))

download_folder = r"C:\Users\sesa443933\Downloads"
dest_folder = r"C:\Users\sesa443933\OneDrive - Schneider Electric\MCD\Tetra 5\Proyecto de Consultoria\dataset\Apodaca. Marriage Records 1891-1900"
for file in os.listdir(download_folder):
    if datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(download_folder, file))).strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d"):
        print(file, datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(download_folder, file))).strftime("%Y-%m-%d"))
        os.replace(os.path.join(download_folder, file), os.path.join(dest_folder, file))