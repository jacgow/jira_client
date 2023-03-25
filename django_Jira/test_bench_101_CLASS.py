import requests
from requests.auth import HTTPBasicAuth
import json
from .jira_issue_api import JiraIssueApi


if __name__ == "__main__":
   auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF06eL1LMgKY418-gTh0hNhL4VJeiUridZjJoAsPMlT8lWtLXY4Ydg5cm5EzloQXmM0QyxrBJTvfJXSI4ObDrcqZqDLOp5tohT3lInGVt90NXmdYJY1SniC3aIk8XbPWVVsCKqAOKvYj6BxW9sY0Lq3xifW4Zv0b41xCFTxiKu2vb0=E2C0E342")
   url = 'https://doubledare.atlassian.net/rest/api/2/issue/10040' #zapytanie o issue numer 10040
   jira_issue_api_object = JiraIssueApi(auth = auth)
   result = print (jira_issue_api_object.get_jira_issue(url = url)) #endpoint


