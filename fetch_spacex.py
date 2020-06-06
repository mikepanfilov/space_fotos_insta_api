import os
import requests

def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    dir = 'images'
    if not os.path.exists(dir):
        os.mkdir(dir)
    filepath = os.path.join(dir,filename)
    with open (filepath, 'wb') as file:
        file.write(response.content)

def main():
    images_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(images_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']
    for link_number, link in enumerate(image_links):
        download_image(link, f'spacex{link_number + 1}.jpg')

if __name__ == "__main__":
    main()