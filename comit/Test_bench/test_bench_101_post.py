import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://doubledare.atlassian.net/rest/api/2/issue'
auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF06eL1LMgKY418-gTh0hNhL4VJeiUridZjJoAsPMlT8lWtLXY4Ydg5cm5EzloQXmM0QyxrBJTvfJXSI4ObDrcqZqDLOp5tohT3lInGVt90NXmdYJY1SniC3aIk8XbPWVVsCKqAOKvYj6BxW9sY0Lq3xifW4Zv0b41xCFTxiKu2vb0=E2C0E342")
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps(
{
    "fields": {
       "project":
       {
          "key": "ITB"
       },
       "summary": "REST ye merry gentlemen 2.",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "id": "10001"
       }
   }
}
)

response = requests.post(url,headers = headers,data = payload,auth = auth)
print(response.text)

#responce from create task jira api:
#{"id":"10040","key":"ITB-24","self":"https://doubledare.atlassian.net/rest/api/2/issue/10040"}

