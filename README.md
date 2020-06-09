# Upload space fotos to Instagram

Script downloads space-thematic photos from SpaceX and Hubble repos to Instagram. All using sites API.
Script creates Images folder and puts all downloaded there.

## How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

Make virtual environment with 'INSTA_USER' and 'INSTA_PASSWORD' for instagram login.

## How to use

To download latest photos from SpaceX photo resources use:

```bash
python fetch_spacex.py
```

To download photo-collections from Hubble site photo resources use:

```bash
python fetch_hubble.py {collection name}
```

For Instagram uploads use:

```bash
python instagram_upload.py
```

*Note:* Iside this script updates images sizes to appropriate 1080x1080 size.

All scripts are refering to utils.py where common functions are placed.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
