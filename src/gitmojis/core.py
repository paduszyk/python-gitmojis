import json

import requests

from . import defaults
from .exceptions import ResponseJsonError
from .model import Gitmoji, Guide


def fetch_guide() -> Guide:
    """Fetch the Gitmoji guide from the official Gitmoji API.

    This function sends a GET request to the Gitmoji API to retrieve the current state
    of the Gitmoji guide. If the request is successful and contains the expected JSON
    data, a `Guide` object is returned. If the expected JSON data is not present, a
    `ResponseJsonError` is raised. In case of an HTTP error during the request (e.g.,
    connection error, timeout), the function falls back to loading a local copy of the
    Gitmoji guide.

    Returns:
        A `Guide` object representing the current state of the Gitmoji API.

    Raises:
        ResponseJsonError: If the API response doesn't contain the expected JSON data or
            if there is an error loading the local backup of the Gitmoji guide.
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
