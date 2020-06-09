import os
import requests
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
from pathlib import Path

def resize_for_instagram():
    outpath = Path.cwd()
    os.makedirs(outpath/'images'/'insta', exist_ok=True)
    for image_number,image in enumerate(os.listdir(outpath/'images')):
        picture = Image.open(outpath/'images'/image)
        width, height = picture.size
        if width == 1920 and height == 1200:
            picture.thumbnail((1080, 1080))
            picture.save(outpath/'images'/'insta'/f'/insta_space_{image_number}.jpg')

def main():
    load_dotenv()
    username = os.environ['INSTA_USER']
    password = os.environ['INSTA_PASSWORD']
    bot = Bot()
    bot.login(username=username, password=password)
    insta_path = 'images/insta/'
    for picture in os.listdir(insta_path):
        bot.upload_photo(insta_path + picture)

if __name__ == "__main__":
    main()