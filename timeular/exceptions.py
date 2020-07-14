class TimeularHttpException(Exception):

    def __init__(self, status_code: int, url: str, message: str = None) -> None:
        """TimeularHttpException raised for all non-successful responses
        """
        super().__init__()
        self.status_code = status_code
        self.url = url
        self.message = message or ''

    def __str__(self):
        return f'TimeularHttpException ({self.status_code}):{self.url} -> {self.message}'

    def __repr__(self):
        return f'<TimeularHttpException [{self.status_code}]>'


class TimeularException(Exception):

    def __init__(self, message: str = None) -> None:
        """TimeularException raised for all other errors
        """
        super().__init__()
        self.message = message or ''

    def __str__(self):
        return f'TimeularException: {self.message}'

    def __repr__(self):
        return f'<TimeularException [{self.message}]>'
