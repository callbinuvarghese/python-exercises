import google.auth
import google.auth.transport.requests
import requests

# getting the credentials and project details for gcp project
credentials, your_project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

#getting request object
auth_req = google.auth.transport.requests.Request()

print(credentials.valid) # prints False
credentials.refresh(auth_req) #refresh token
#cehck for valid credentials
print(credentials.valid)  # prints True
print(credentials.token) # prints token
print(your_project_id)

########################################################################
'''
import googleapiclient.discovery

service = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

response = service.projects().getIamPolicy(resource=f'{your_project_id}', body={}).execute()

print(response)
'''

import googleapiclient.discovery
from urllib.parse import urlencode

def search_transitive_groups(service, member, page_size):
  try:
    groups = []
    next_page_token = ''
    while True:
      query_params = urlencode(
        {
          "query": "member_key_id == '{}' && 'cloudidentity.googleapis.com/groups.discussion_forum' in labels".format(member),
          "page_size": page_size,
          "page_token": next_page_token
        }
      )
      request = service.groups().memberships().searchTransitiveGroups(parent='groups/-')
      request.uri += "&" + query_params
      response = request.execute()

      if 'memberships' in response:
        groups += response['memberships']

      if 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
      else:
        next_page_token = ''

      if len(next_page_token) == 0:
        break;

    print(groups)
  except Exception as e:
    print(e)

service = googleapiclient.discovery.build('cloudidentity', 'v1')

# Return results with a page size of 50
search_transitive_groups(service, 'binu.b.varghese@accenture.com', 50)
