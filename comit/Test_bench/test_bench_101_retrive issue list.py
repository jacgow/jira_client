# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://doubledare.atlassian.net/rest/api/2/search'

auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF06eL1LMgKY418-gTh0hNhL4VJeiUridZjJoAsPMlT8lWtLXY4Ydg5cm5EzloQXmM0QyxrBJTvfJXSI4ObDrcqZqDLOp5tohT3lInGVt90NXmdYJY1SniC3aIk8XbPWVVsCKqAOKvYj6BxW9sY0Lq3xifW4Zv0b41xCFTxiKu2vb0=E2C0E342")

headers = {
  "Accept": "application/json"
}

query = {
  'jql': 'project = ITB',
    }

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


#działa