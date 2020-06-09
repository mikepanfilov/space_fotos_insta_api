import os
import requests
from PIL import Image
from pathlib import Path
from instabot import Bot
from dotenv import load_dotenv

def download_image(url, filename):
    outpath = Path.cwd()
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(outpath/'images', exist_ok=True)
    filepath = outpath/'images'/filename
    with open (filepath, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_lauch():
    images_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(images_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']
    for link_number, link in enumerate(image_links):
        download_image(link, f'spacex{link_number + 1}.jpg')

def get_file_extention(url):
    return url.split('.')[-1]

def fetch_hubble_images(image_id):
    images_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(images_url)
    response.raise_for_status()
    image_links = response.json()['image_files']
    for link_number, link in enumerate(image_links):
        link_corrected = 'https:' + link['file_url']
        ext = get_file_extention(link_corrected)
        download_image(link_corrected, f'hubble_id{image_id}_{link_number + 1}.' + ext)

def fetch_hubble_collection(collection_name):
    payload = {'collection_name':collection_name}
    url = 'http://hubblesite.org/api/v3/images'
    response = requests.get(url, params=payload)
    image_ids = response.json()
    for image in image_ids:
        fetch_hubble_images(image['id'])

def resize_for_instagram():
    outpath = Path.cwd()
    os.makedirs(outpath/'images'/'insta', exist_ok=True)
    for image_number,image in enumerate(os.listdir(outpath/'images')):
        picture = Image.open(outpath/'images'/image)
        width, height = picture.size
        if width == 1920 and height == 1200:
            picture.thumbnail((1080, 1080))
            picture.save(outpath/'images'/'insta'/f'/insta_space_{image_number}.jpg')

def upload_to_instagram():
    outpath = Path.cwd()
    username = os.environ['INSTA_USER']
    password = os.environ['INSTA_PASSWORD']
    bot = Bot()
    bot.login(username=username, password=password)
    insta_path = outpath/'images'/'insta'
    for picture in os.listdir(insta_path):
        bot.upload_photo(insta_path/picture)

def main():
    load_dotenv()

if __name__ == '__main__':
    main()