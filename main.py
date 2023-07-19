import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def download_images(images, project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    for i, img in enumerate(images):
        response = requests.get(img['src'], stream=True)
        with open(os.path.join(project_name, 'img{}.jpg'.format(i)), 'wb') as out_file:
            out_file.write(response.content)


def main():
    url = "https://www.behance.net/ProfileUserName"
    driver = webdriver.Chrome()  # you may need to specify the path to the chromedriver

    driver.get(url)

    # scroll down to load all projects
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # pause to load new projects
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    base_url = "https://www.behance.net"
    project_links = [base_url + a['href'] if a['href'].startswith(
        '/') else a['href'] for a in soup.select('.e2e-ProjectCoverNeue-link')]

    for link in project_links:
        print(f"Opening link: {link}")  # print the link before opening
        try:
            driver.get(link)
            time.sleep(2)  # pause to load all images
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            project_name = soup.select_one('.Project-title-Q6Q').text.strip()
            images = soup.select('.grid__item-image')

            # If no images found using first selector, try with the second selector
            if not images:
                images = soup.select('.ImageElement-image-SRv')

            # print the image URLs
            print(f"Image URLs: {[img['src'] for img in images]}")
            download_images(images, project_name)
        except Exception as e:
            print(f"Error with link {link}: {str(e)}")

    driver.quit()


if __name__ == "__main__":
    main()
