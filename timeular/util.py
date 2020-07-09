import requests
from json import dumps
from typing import Dict, Any
from .exceptions import ResponseError


class TimeularApiUtil:
    """Provides basis for making requests to Timeular v2 public API
    """

    def __init__(self):
        """TimeularApiUtil contructor
        provides methods for making requests to Timeular API
        """
        self.base_url = 'https://api.timeular.com/api/v2'
        self.token = None

    def _get(self, uri: str, params: Dict = None, args: Dict = None, token: str = None) -> Any:
        """Create GET http request
        """
        full_url = self.base_url + uri
        if params is None:
            params = {}
        if args is None:
            args = {}

        args.update(**{'headers': self._get_headers(token)})
        return requests.get(full_url, params=dumps(params), **args)

    def _post(self, uri: str, data: Dict = None, json: Dict = None, args: Dict = None, token: str = None) -> Any:
        """Create POST http request
        """
        full_url = self.base_url + uri
        if data is None:
            data = {}
        if json is None:
            json = {}
        if args is None:
            args = {}

        args.update(**{'headers': self._get_headers(token)})
        return requests.post(full_url, data=dumps(data), json=json, **args)

    def _put(self, uri: str, data: Dict = None, args: Dict = None, token: Dict = None) -> Any:
        """Create PUT http request
        """
        full_url = self.base_url + uri
        if data is None:
            data = {}
        if args is None:
            args = {}

        args.update(**{'headers': self._get_headers(token)})
        return requests.put(full_url, data=dumps(data), **args)

    def _patch(self, uri: str, token: str, data: Dict = None, args: Dict = None) -> Any:
        """Create PATCH http request
        """
        full_url = self.base_url + uri
        if args is None:
            args = {}
        if data is None:
            data = {}

        args.update(**{'headers': self._get_headers(token)})
        return requests.patch(full_url, data=dumps(data), **args)

    def _delete(self, uri: str, token: str, args: Dict = None) -> Dict:
        """Create DELETE http request
        """
        full_url = self.base_url + uri
        if args is None:
            args = {}

        args.update(**{'headers': self._get_headers(token)})
        return requests.delete(full_url, **args)

    @staticmethod
    def _get_headers(token: str = None) -> Dict:
        """Get necessary headers. When token is provided adds 'Authorization' value as well
        """
        headers = {
            'accept': 'application/json;charset=UTF-8',
            'Content-Type': 'application/json',
        }
        if token:
            headers['Authorization'] = 'Bearer ' + token

        return headers

    @staticmethod
    def _get_content_or_raise_error(response: requests.Response, key: str = None) -> Any:
        """Process response based on status_code.
        If status_code is in 2xx range, returns processed Fresponse, otherwise ResponseError is raised.
        """
        status_code = response.status_code

        if status_code == 200:
            response_content = response.json()
            if key is not None:
                if key not in response_content:
                   raise ValueError(f'Key \'{key}\' is not present in response JSON ({response_content})')
                return response_content.get(key)
            else:
                return response_content
        elif status_code == 201:
            return response.json()
        elif status_code == 204:
            return True
        elif 200 <= status_code < 300:
            # all other 2xx status codes
            return response.content
        else:
            reason = response.json()['message']
            raise ResponseError(status_code, reason)
