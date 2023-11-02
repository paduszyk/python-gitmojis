import requests

from . import defaults
from .exceptions import ResponseJsonError
from .model import Gitmoji, Guide


def fetch_guide() -> Guide:
    response = requests.get(defaults.GITMOJI_API_URL)

    if (gitmojis_json := response.json().get(defaults.GITMOJI_API_KEY)) is None:
        raise ResponseJsonError

    guide = Guide(gitmojis=[Gitmoji(**gitmoji_json) for gitmoji_json in gitmojis_json])

    return guide
