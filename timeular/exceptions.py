
class ResponseError(Exception):

    def __init__(self, status_code: int, message: str) -> None:
        """ResponseError raised for all non-successful responses
        """
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Response (code: {self.status_code}) -> {self.message}'
