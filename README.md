# timeular-api
Timeular v2 API Client

## Usage

```python
from timeular import Timeular

API_KEY = '<your_api_key>'
API_SECRET = '<your_api_secret>'

timeular = Timeular(api_key=API_KEY, api_secret=API_SECRET)

# AUTH

# gets the session token. Is called from constructor. Updates value: 'timeular.token'
timeular.sign_in()

# gets the api key from server. Updates value: 'timeular.api_key'
timeular.get_api_key()

# gets new api key and secret. Updates values 'timeular.api_key' and 'timeular.api_secret'
timeular.generate_api_key_and_secret()

# INTEGRATIONS
integrations = timeular.integrations()
enabled_integraions = integrations.get_enabled_integrations()
```
    
