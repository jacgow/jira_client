import requests
import json

class JiraIssueApi:
#############################################################################
    def __init__(self, auth):
      self.auth = auth
#############################################################################
    def create_jira_issue(self, url):
        headers = {"Accept": "application/json"}

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

        if response.status_code == 200:
                result = requests.post(url,headers = headers,data = payload,auth = auth)
                return result
        else:
                raise Exception()
        
#############################################################################
    def get_jira_issue(self, url):
     
      headers = {"Accept": "application/json"}

      response = requests.request(
         "GET",
         url,
         headers=headers,
         auth=self.auth
      )

      if response.status_code == 200:
         result = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
         return result
      else:
         raise Exception()
#############################################################################
    def update_jira_issue(self, url):

        headers = { "Accept": "application/json", "Content-Type": "application/json"}

        payload = json.dumps( { "fields": { "summary": "changed description from api v2" } } )

        response = requests.request(
        "PUT",
        url,
        data=payload,
        headers=headers,
        auth=self.auth 
        )

        if response.status_code == 200:
            result = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
            return result
        else:
            raise Exception()
#############################################################################    
    def delete_jira_issue(self, url):
        pass
#############################################################################
    def get_list_jira_issues(self, url):
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

        if response.status_code == 200:
            result = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
            return result
        else:
            raise Exception()
        
    def jira_url(self, url)

#############################################################################
#'get issue'
#url = 'https://doubledare.atlassian.net/rest/api/2/issue/10040'

#'post issue'
#url = 'https://doubledare.atlassian.net/rest/api/2/issue'

#'retrive issue'
#url = 'https://doubledare.atlassian.net/rest/api/2/search'

#'update issue'
#url = 'https://doubledare.atlassian.net/rest/api/3/issue/10040'
