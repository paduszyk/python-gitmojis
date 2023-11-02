class GitmojisException(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or getattr(self.__class__, "message", ""))


class ApiError(GitmojisException):
    pass


class ResponseJsonError(ApiError):
    message = "unsupported format of the JSON data returned by the API"
