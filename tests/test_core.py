import pytest
import requests

from gitmojis.core import GITMOJI_API_KEY, fetch_guide
from gitmojis.model import Guide


@pytest.fixture()
def response(mocker):
    return mocker.Mock(spec_set=requests.Response)


def test_fetch_guide_creates_guide_from_api_response_json(mocker, response):
    response.json.return_value = {GITMOJI_API_KEY: []}

    mocker.patch("requests.get", return_value=response)

    guide = fetch_guide()

    assert isinstance(guide, Guide)
