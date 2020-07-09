from typing import List
from .util import TimeularApiUtil


class Integrations(TimeularApiUtil):
    """ Provides integrations endpoints for Timeular v2 public API
    """

    def __init__(self, token: str):
        """timeular.Integrations constructor
        """
        super().__init__()
        self.token = token

    def get_enabled_integrations(self) -> List[str]:
        """Get list of enabled Integrations

        endpoint: GET /integrations
        """
        response = self._get('/integrations', token=self.token)
        return self._get_content_or_raise_error(response, 'integrations')
