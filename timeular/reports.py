import datetime
from timeular.util import TimeularApiUtil


class Reports(TimeularApiUtil):
    """ Provides Reports endpoints for Timeular v2 public API
    """

    def __init__(self, token: str):
        """timeular.Reports constructor
        """
        super().__init__()
        self.token = token

    def generate(self, start_at: datetime.datetime, stop_at: datetime.datetime, timezone: str, activity_id: str = None, note_query: str = None, file_type: str = None) -> str:
        """Generate Report

        endpoint: GET /report/{start_at}/{stop_at}
        """
        start_at_str = start_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        stop_at_str = stop_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]

        query_params = {
            'timezone': timezone,
        }

        if activity_id is not None:
            if type(activity_id) != str:
                raise TypeError("'activity_id' must be a str")
            else:
                query_params.update({'activityId': activity_id})

        if note_query is not None:
            if type(note_query) != str:
                raise TypeError("'note_query' must be a str")
            else:
                query_params.update({'noteQuery': note_query})

        if file_type is not None:
            if type(file_type) != str:
                raise TypeError("'file_type' must be a str")
            else:
                query_params.update({'fileType': file_type})

        response = self._get(f'/report/{start_at_str}/{stop_at_str}', params=query_params, token=self.token)
        return self._get_content_or_raise_error(response)
