import os
from pprint import pprint
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

def fetch_spacex_last_lauch():
    images_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(images_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']
    for link_number, link in enumerate(image_links):
        download_image(link, f'spacex{link_number + 1}.jpg')

def get_file_extention(address):
    return address.split('.')[-1]

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
        print(image['id'])
        fetch_hubble_images(image['id'])

def main():
    # fetch_spacex_last_lauch()
    # fetch_hubble_images(4673)
    fetch_hubble_collection('wallpaper')
    
if __name__ == '__main__':
    main()