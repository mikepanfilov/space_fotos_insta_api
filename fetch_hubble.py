import os
import argparse
import requests
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

def main():
    parser = argparse.ArgumentParser(
        description='Downloads photo by collection name'
        )
    parser.add_argument('collection', help='Enter collection name')
    args = parser.parse_args()
    payload = {'collection_name': args.collection}
    url = 'http://hubblesite.org/api/v3/images'
    response = requests.get(url, params=payload)
    image_ids = response.json()
    for image in image_ids:
        fetch_hubble_images(image['id'])

if __name__ == "__main__":
    main()