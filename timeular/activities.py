from typing import Dict, List
from timeular.exceptions import TimeularException
from timeular.util import TimeularApiUtil


class Activities(TimeularApiUtil):
    """ Provides activities endpoints for Timeular v2 public API
    """

    def __init__(self, token: str):
        """timeular.Activities constructor
        """
        super().__init__()
        self.token = token

    def get_active_activities(self, assigned_only=False) -> List[Dict]:
        """Get list of all activities

        endpoint: GET /activities
        """
        response = self._get('/activities', token=self.token)
        activities = self._get_content_or_raise_error(response, 'activities')

        if assigned_only:
            return [activity for activity in activities if activity.get('deviceSide') is not None]
        else:
            return activities

    def create(self, name: str, color: str, integration: str = None) -> Dict:
        """Create an Activity

        endpoint: POST /activities
        """
        payload = {
            'name': name,
            'color': color,
        }

        if integration:
            payload['integration'] = integration

        response = self._post('/activities', data=payload, token=self.token)
        return self._get_content_or_raise_error(response)

    def edit(self, activity_id: str, name: str = None, color: str = None) -> Dict:
        """Edit an Activity

        endpoint: PATCH /activities/{activity_id}
        """
        payload = {}
        if name:
            payload['name'] = name
        if color:
            payload['color'] = color

        response = self._patch(f'/activities/{activity_id}', data=payload, token=self.token)
        return self._get_content_or_raise_error(response)

    def archive(self, activity_id: str, print_errors: bool = True) -> bool:
        """Archive an activity

        endpoint: DELETE /activities/{activity_id}
        """
        response = self._delete(f'/activities/{activity_id}', token=self.token)
        errors = self._get_content_or_raise_error(response, 'errors')

        if errors and print_errors:
            raise print("Activity is archived.\nHowever there were some error(s):\n- {}".format('\n- '.join(errors)))

        return errors

    def assign_activity_to_device_side(self, activity_id: str, device_side: int) -> Dict:
        """Assign an Activity to Device Side

        endpoint: POST /activities/{activity_id}/device-side/{device_side}
        """
        response = self._post(f'/activities/{activity_id}/device-side/{device_side}', token=self.token)
        return self._get_content_or_raise_error(response)

    def unassign_activity_from_device_side(self, activity_id: str, device_side: int = None) -> Dict:
        """Un-assign an Activity from a Device Side

        endpoint: DELETE /activities/{activity_id}/device-side/{device_side}
        """
        if device_side is None:
            assigned_activities = self.get_active_activities(assigned_only=True)
            for act in assigned_activities:
                if act.get('id') == activity_id:
                    device_side = act.get('deviceSide')
                    break
            else:
                raise TimeularException(f'Activity "{activity_id}" is not assigned to any device side')
        response = self._delete(f'/activities/{activity_id}/device-side/{device_side}', token=self.token)
        return self._get_content_or_raise_error(response)

    def get_archived_activities(self) -> List[Dict]:
        """Get list of archived activities

        endpoint: GET /archived-activities
        """
        response = self._get('/archived-activities', token=self.token)
        return self._get_content_or_raise_error(response)
