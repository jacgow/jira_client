import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://doubledare.atlassian.net/rest/api/2/issue/10040' #zapytanie o issue numer 10040
auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF06eL1LMgKY418-gTh0hNhL4VJeiUridZjJoAsPMlT8lWtLXY4Ydg5cm5EzloQXmM0QyxrBJTvfJXSI4ObDrcqZqDLOp5tohT3lInGVt90NXmdYJY1SniC3aIk8XbPWVVsCKqAOKvYj6BxW9sY0Lq3xifW4Zv0b41xCFTxiKu2vb0=E2C0E342")
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

""" 
ZWROTKA
{
    "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations,customfield_10010.requestTypePractice",
    "fields": {
        "aggregateprogress": {
            "progress": 0,
            "total": 0
        },
        "aggregatetimeestimate": null,
        "aggregatetimeoriginalestimate": null,
        "aggregatetimespent": null,
        "assignee": null,
        "attachment": [],
        "comment": {
            "comments": [],
            "maxResults": 0,
            "self": "https://doubledare.atlassian.net/rest/api/2/issue/10040/comment",
            "startAt": 0,
            "total": 0
        },
        "components": [],
        "created": "2023-03-14T19:20:09.960+0100",
        "creator": {
            "accountId": "5faecaf3c824730070891224",
            "accountType": "atlassian",
            "active": true,
            "avatarUrls": {
                "16x16": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "24x24": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "32x32": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "48x48": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png" 
            },
            "displayName": "Borys Piasny",
            "emailAddress": "boryspiasny@gmail.com",
            "self": "https://doubledare.atlassian.net/rest/api/2/user?accountId=5faecaf3c824730070891224",
            "timeZone": "Europe/Warsaw"
        },
        "customfield_10001": null,
        "customfield_10002": null,
        "customfield_10003": null,
        "customfield_10004": null,
        "customfield_10005": null,
        "customfield_10006": null,
        "customfield_10007": null,
        "customfield_10008": null,
        "customfield_10009": null,
        "customfield_10010": null,
        "customfield_10014": null,
        "customfield_10015": null,
        "customfield_10016": null,
        "customfield_10017": null,
        "customfield_10018": {
            "hasEpicLinkFieldDependency": false,
            "nonEditableReason": {
                "message": "The Parent Link is only available to Jira Premium users.",
                "reason": "PLUGIN_LICENSE_ERROR"
            },
            "showField": false
        },
        "customfield_10019": "0|i0006n:",
        "customfield_10020": null,
        "customfield_10021": null,
        "customfield_10022": null,
        "customfield_10023": null,
        "customfield_10024": null,
        "customfield_10025": null,
        "customfield_10026": null,
        "customfield_10027": null,
        "customfield_10028": null,
        "customfield_10029": null,
        "customfield_10030": null,
        "customfield_10031": null,
        "description": "Creating of an issue using project keys and issue type names using the REST API",
        "duedate": null,
        "environment": null,
        "fixVersions": [],
        "issuelinks": [],
        "issuerestriction": {
            "issuerestrictions": {},
            "shouldDisplay": false
        },
        "issuetype": {
            "avatarId": 10318,
            "description": "A small, distinct piece of work.",
            "entityId": "c9f8666c-6642-495b-88d8-0da56428ff40",
            "hierarchyLevel": 0,
            "iconUrl": "https://doubledare.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10318?size=medium",
            "id": "10001",
            "name": "Task",
            "self": "https://doubledare.atlassian.net/rest/api/2/issuetype/10001",
            "subtask": false
        },
        "labels": [],
        "lastViewed": null,
        "priority": {
            "iconUrl": "https://doubledare.atlassian.net/images/icons/priorities/medium.svg",
            "id": "3",
            "name": "Medium",
            "self": "https://doubledare.atlassian.net/rest/api/2/priority/3"
        },
        "progress": {
            "progress": 0,
            "total": 0
        },
        "project": {
            "avatarUrls": {
                "16x16": "https://doubledare.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10422?size=xsmall",
                "24x24": "https://doubledare.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10422?size=small",
                "32x32": "https://doubledare.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10422?size=medium",
                "48x48": "https://doubledare.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10422"
            },
            "id": "10000",
            "key": "ITB",
            "name": "Integration test bench",
            "projectTypeKey": "business",
            "self": "https://doubledare.atlassian.net/rest/api/2/project/10000",
            "simplified": true
        },
        "reporter": {
            "accountId": "5faecaf3c824730070891224",
            "accountType": "atlassian",
            "active": true,
            "avatarUrls": {
                "16x16": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "24x24": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "32x32": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png",                "48x48": "https://secure.gravatar.com/avatar/913f2dc648d4ee0fb9d14ac8717b7176?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FBP-3.png" 
            },
            "displayName": "Borys Piasny",
            "emailAddress": "boryspiasny@gmail.com",
            "self": "https://doubledare.atlassian.net/rest/api/2/user?accountId=5faecaf3c824730070891224",
            "timeZone": "Europe/Warsaw"
        },
        "resolution": null,
        "resolutiondate": null,
        "security": null,
        "status": {
            "description": "",
            "iconUrl": "https://doubledare.atlassian.net/",
            "id": "10000",
            "name": "To Do",
            "self": "https://doubledare.atlassian.net/rest/api/2/status/10000",
            "statusCategory": {
                "colorName": "blue-gray",
                "id": 2,
                "key": "new",
                "name": "To Do",
                "self": "https://doubledare.atlassian.net/rest/api/2/statuscategory/2"
            }
        },
        "statuscategorychangedate": "2023-03-14T19:20:10.392+0100",
        "subtasks": [],
        "summary": "REST ye merry gentlemen. python",
        "timeestimate": null,
        "timeoriginalestimate": null,
        "timespent": null,
        "timetracking": {},
        "updated": "2023-03-14T19:20:09.960+0100",
        "versions": [],
        "votes": {
            "hasVoted": false,
            "self": "https://doubledare.atlassian.net/rest/api/2/issue/ITB-24/votes",
            "votes": 0
        },
        "watches": {
            "isWatching": true,
            "self": "https://doubledare.atlassian.net/rest/api/2/issue/ITB-24/watchers",
            "watchCount": 1
        },
        "worklog": {
            "maxResults": 20,
            "startAt": 0,
            "total": 0,
            "worklogs": []
        },
        "workratio": -1
    },
    "id": "10040",
    "key": "ITB-24",
    "self": "https://doubledare.atlassian.net/rest/api/2/issue/10040"
} 
"""