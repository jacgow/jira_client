import requests
from requests.auth import HTTPBasicAuth
import json


url = 'https://doubledare.atlassian.net/rest/api/3/issue/10040'
auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF06eL1LMgKY418-gTh0hNhL4VJeiUridZjJoAsPMlT8lWtLXY4Ydg5cm5EzloQXmM0QyxrBJTvfJXSI4ObDrcqZqDLOp5tohT3lInGVt90NXmdYJY1SniC3aIk8XbPWVVsCKqAOKvYj6BxW9sY0Lq3xifW4Zv0b41xCFTxiKu2vb0=E2C0E342")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( 
 {
  "fields": {
    "summary": "changed description from api v2"
  }
}
)

response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)
print(response.text)

#sukces, działa! Brak printu


