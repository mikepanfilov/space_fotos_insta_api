from instabot import Bot
from dotenv import load_dotenv
from utils import requests, Path, os
from utils import download_image, fetch_hubble_images, resize_for_instagram


def main():
    load_dotenv()
    username = os.environ['INSTA_USER']
    password = os.environ['INSTA_PASSWORD']
    bot = Bot()
    bot.login(username=username, password=password)
    resize_for_instagram()
    outpath = Path.cwd()
    insta_path = outpath/'images'/'insta'
    for picture in os.listdir(insta_path):
        bot.upload_photo(insta_path/picture)

if __name__ == "__main__":
    main()