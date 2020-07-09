from .util import TimeularApiUtil


class Timeular(TimeularApiUtil):
    """ Provides a base class for Timeular v2 public API
    """

    def __init__(self, api_key: str, api_secret: str):
        """Timeular constructor
        """
        super().__init__()
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = None

        self.sign_in()

    def sign_in(self) -> None:
        """Sign-in with API Key & API Secret to fetch and save the session token.
        It also gets called when from constructor.

        endpoint: POST /developer/sign-in
        """
        payload = {
            'apiKey': self.api_key,
            'apiSecret': self.api_secret,
        }

        response = self._post('/developer/sign-in', data=payload)
        self.token = self._get_content_or_raise_error(response, 'token')

    def get_api_key(self) -> None:
        """Get API Key

        endpoint: GET /developer/api-access
        """
        response = self._get('/developer/api-access', token=self.token)
        self.api_key = self._get_content_or_raise_error(response, 'apiKey')

    def generate_api_key_and_secret(self) -> None:
        """Generate new API Key & API Secret

        endpoint: POST /developer/api-access
        """
        response = self._post('/developer/api-access', token=self.token)
        content = self._get_content_or_raise_error(response)

        self.api_key = content.get('apiKey')
        self.api_secret = content.get('apiSecret')
