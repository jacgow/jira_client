import requests
from requests.auth import HTTPBasicAuth
import json
from jira_issue_api import JiraIssueApi


if __name__ == "__main__":
   http_basic_auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF0Sxvu-rAfWCHnsaPn0sEbSRpehPRKl7Y5vkcWOBcvzKrzNUfFSoKwcRUcR6EYr-Q9K3IDfDIsVMGlZpQq5Pmwi8QLMtgnegLn79tYi6Fqe_tc5w2qL2lx2tv6uzIegjR7zFppDfIvDwnTpe0IA16reQ_w97LZ96fOS_E1HUgtxFU=6FE0ADB2")
   #issue_id = 10040 #zapytanie o issue numer 10040
   query = {'jql': 'project = ITB',}
   jira_issue_api_object = JiraIssueApi(auth = http_basic_auth, jira_base_url = 'https://doubledare.atlassian.net/rest/api/')
   #result = jira_issue_api_object.get_jira_issue(issue_id = issue_id)
   #print(result)
   result = jira_issue_api_object.get_list_jira_issues(query)
   print(result)


