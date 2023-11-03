class GitmojisException(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or getattr(self.__class__, "message", ""))


class ApiRequestError(GitmojisException):
    message = "there was an issue when requesting the data from the API"


class ResponseJsonError(ApiRequestError):
    message = "unsupported format of the JSON data returned by the API"
