import json

import requests

from . import defaults
from .exceptions import ResponseJsonError
from .model import Gitmoji, Guide


def fetch_guide() -> Guide:
    """Fetch the Gitmoji guide from the official Gitmoji API.

    This function sends a GET request to the Gitmoji API to retrieve the current state
    of the Gitmoji guide.

    Returns:
        A `Guide` object representing the current state of the Gitmoji API.

    Raises:
        ResponseJsonError: If the API response doesn't contain the expected JSON data.
    """
    try:
        (response := requests.get(defaults.GITMOJI_API_URL)).raise_for_status()

        if (gitmojis_json := response.json().get(defaults.GITMOJI_API_KEY)) is None:
            raise ResponseJsonError
    except requests.RequestException:
        with defaults.GITMOJI_API_PATH.open(encoding="UTF-8") as f:
            gitmojis_json = json.load(f)

    guide = Guide(gitmojis=[Gitmoji(**gitmoji_json) for gitmoji_json in gitmojis_json])

    return guide
