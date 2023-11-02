from typing import Final

import requests

from .model import Gitmoji, Guide

GITMOJI_API_URL: Final = "https://gitmoji.dev/api/gitmojis"

GITMOJI_API_KEY: Final = "gitmojis"


def fetch_guide() -> Guide:
    response = requests.get(GITMOJI_API_URL)

    gitmojis_json = response.json()[GITMOJI_API_KEY]

    guide = Guide(gitmojis=[Gitmoji(**gitmoji_json) for gitmoji_json in gitmojis_json])

    return guide
