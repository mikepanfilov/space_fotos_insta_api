import os
import requests
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv

def resize_for_instagram():
    os.makedirs('images/insta', exist_ok=True)
    for image_number,image in enumerate(os.listdir('images')):
        picture = Image.open('images/' + image)
        width, height = picture.size
        if width == 1920 and height == 1200:
            picture.thumbnail((1080, 1080))
            picture.save(dir + f'/insta_space_{image_number}.jpg')

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