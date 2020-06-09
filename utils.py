import os
import requests
from PIL import Image
from pathlib import Path

def download_image(url, filename):
    outpath = Path.cwd()
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(outpath/'images', exist_ok=True)
    filepath = outpath/'images'/filename
    with open (filepath, 'wb') as file:
        file.write(response.content)

def fetch_hubble_images(image_id):
    images_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(images_url)
    response.raise_for_status()
    image_links = response.json()['image_files']
    for link_number, link in enumerate(image_links):
        link_corrected = 'https:' + link['file_url']
        ext = os.path.splitext(link_corrected)[1]
        download_image(link_corrected, f'hubble_id{image_id}_{link_number + 1}' + ext)

def resize_for_instagram():
    outpath = Path.cwd()
    os.makedirs(outpath/'images'/'insta', exist_ok=True)
    for image_number,image in enumerate(os.listdir(outpath/'images')):
        if image.endswith('jpg'):
            picture = Image.open(outpath/'images'/image)
            width, height = picture.size
            picture.thumbnail((1080, 1080))
            picture.save(outpath/'images'/'insta'/f'insta_space_{image_number}.jpg')

if __name__ == "__main__":
    pass