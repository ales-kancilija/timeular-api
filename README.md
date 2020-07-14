# timeular-api
Timeular v2 API Client

## Usage

```python
from timeular import Timeular

API_KEY = '<your_api_key>'
API_SECRET = '<your_api_secret>'

client = Timeular(api_key=API_KEY, api_secret=API_SECRET)

# AUTH

# gets the session token. Is called from constructor. Updates value: 'timeular.token'
client.sign_in()

# gets the api key from server. Updates value: 'timeular.api_key'
client.get_api_key()

# gets new api key and secret. Updates values 'timeular.api_key' and 'timeular.api_secret'
client.generate_api_key_and_secret()

# INTEGRATIONS
integrations = client.integrations()
enabled_integraions = integrations.get_enabled_integrations()

# ACTIVITIES
activities = client.activities()

# List activities
activities.get_all()  # returns list of all non-archived activities
activities.get_all(active_only=True)  # returns list of all non-archived activities, that are assigned to some device side
activities.get_archived_activities()  # returns list of all archived activities

# Create new activity
sport_activity = activities.create(name='Sport', color='#98FB98')

# Edit activity's name and/or color
sport_activity = activities.edit(sport_activity.get('id'), color='#9B7')

# Assign activity to device side
sport_activity = activities.assign_activity_to_device_side(sport_activity.get('id'), 8)

# Unassign activity from device side. Setting device side is optional.
# If activity is not assinged to any device side, Exception will be raised
sport_activity = activities.unassign_activity_from_device_side(sport_activity.get('id'))

# Archive activity (Activity doesn't get deleted, but archived. All its the recorded entries remain)
# returns a List[str] of errors which can be ignored and did not prevented action to be performed successfully. 
activities.archive(sport_activity.get('id'))

# DEVICES
devices = client.devices()

# get list of known devices
all_devices = devices.list()

device = all_devices[0]

# Activate a device
device = devices.activate(device.get('serial'))

# Deactivate a device
device = devices.deactivate(device.get('serial'))

# Rename a device
device = devices.rename(device.get('serial'), 'Best Gadget')

# Enable a device
device = devices.enable(device.get('serial'))

# Disable a device
device = devices.disable(device.get('serial'))

# Check if device is enabled
enabled = devices.is_enabled(device.get('serial'))

# Check if device is active
active = devices.is_active(device.get('serial'))

# Remove device from know devices
devices.disown(device.get('serial'))
```
    
