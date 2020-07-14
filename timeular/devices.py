from typing import Dict, List
from timeular.exceptions import TimeularException
from timeular.util import TimeularApiUtil


class Devices(TimeularApiUtil):
    """ Provides devices endpoints for Timeular v2 public API
    """

    def __init__(self, token: str):
        """Devices constructor
        """
        super().__init__()
        self.token = token

    def list(self) -> List[dict]:
        """Get list of known devices

        endpoint: GET /devices
        """
        response = self._get('/devices', token=self.token)
        return self._get_content_or_raise_error(response, 'devices')

    def activate(self, device_serial: str) -> Dict:
        """Sets the status of a Device to active

        endpoint: POST /devices/{device_serial}/active
        """
        response = self._post(f'/devices/{device_serial}/active', token=self.token)
        return self._get_content_or_raise_error(response)

    def deactivate(self, device_serial: str) -> Dict:
        """Removes the active status from the given Device

        endpoint: DELETE /devices/{device_serial}/active
        """
        response = self._delete(f'/devices/{device_serial}/active', token=self.token)
        return self._get_content_or_raise_error(response)

    def rename(self, device_serial: str, name: str) -> Dict:
        """Rename a device

        endpoint: PATCH /devices/{device_serial}
        """
        payload = {
            'name': name
        }

        response = self._patch(f'/devices/{device_serial}', data=payload, token=self.token)
        return self._get_content_or_raise_error(response)

    def disown(self, device_serial: str) -> bool:
        """Remove known device

        endpoint: DELETE /devices/{device_serial}
        """
        response = self._delete(f'/devices/{device_serial}', token=self.token)
        return self._get_content_or_raise_error(response)

    def enable(self, device_serial: str) -> Dict:
        """Enable a device

        endpoint: DELETE /devices/{device_serial}/disabled
        """

        # to enable a device you delete a disabled status
        response = self._delete(f'/devices/{device_serial}/disabled', token=self.token)
        return self._get_content_or_raise_error(response)

    def disable(self, device_serial: str) -> Dict:
        """Disable a device

        endpoint: POST /devices/{device_serial}/disabled
        """

        # to disable a device you set a disabled status
        response = self._post(f'/devices/{device_serial}/disabled', token=self.token)
        return self._get_content_or_raise_error(response)

    def is_active(self, device_serial):
        devices = self.list()
        for device in devices:
            if device.get('serial') == device_serial:
                return device.get('active')
        raise TimeularException(f'Device with serial "{device_serial}" is not among known devices')

    def is_enabled(self, device_serial):
        devices = self.list()
        for device in devices:
            if device.get('serial') == device_serial:
                return not device.get('disabled')
        raise TimeularException(f'Device with serial "{device_serial}" is not among known devices')
