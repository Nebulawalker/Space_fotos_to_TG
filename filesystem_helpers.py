import requests
import os
from urllib.parse import urlparse
from typing import Iterable
from image_compressor import compress_image


def download_images(urls: Iterable, service: str) -> None:
    os.makedirs("image", exist_ok=True)
    for index, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        file_extention = get_extension(url)
        path = f"image/{service}_{index}{file_extention}"
        with open(path, "wb") as file:
            file.write(response.content)

        if os.path.getsize(path) > 20971520:
            compress_image(path)


def get_extension(url):
    parsed_url = urlparse(url)
    file_path = os.path.splitext(parsed_url.path)
    file_extension = file_path[1]
    return file_extension
