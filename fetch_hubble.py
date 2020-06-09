import argparse
from utils import download_image, fetch_hubble_images, requests

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