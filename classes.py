import requests
import json
import math

from constants import *

def get_org(org: str, token=None):
    """Get an organization by name

    Arguments:
        org -- Name of the organization
    """
    """GH's reference implementation in cURL
    curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer <YOUR-TOKEN>"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/orgs/ORG
    """

    # Write the headers
    headers = HEADERS_FORMAT.copy()

    if token is None:

        # Without a token, use no token
        del headers["Authorization"]
    else:

        # Add and format the token
        headers["Authorization"] = headers["Authorization"].format(token)

    # Create and request the url
    url = ORG_URL.format(org)
    org = requests.get(url, headers=headers)

    # Load it into a python object
    org = json.loads(org.text)
    
    return org


def get_org_repos(org: str, token=None) -> str:
    """Get repositories owned by an organization

    Arguments:
        org -- Name of the organization you're scanning
        token -- Your personal access token

    Returns:
        JSON as raw, unformatted text.
    """
    """GH's reference implementation in cURL
    curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer <YOUR-TOKEN>"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/orgs/ORG/repos
    """

    # Find out how many repos the org has
    repo_num = get_org(org, token=token)["public_repos"]

    # Write the headers
    headers = HEADERS_FORMAT.copy()

    if token is None:

        # Without a token, use no token
        del headers["Authorization"]
    else:

        # Add and format the token
        headers["Authorization"] = headers["Authorization"].format(token)

    # This program requests 100 repos per page by default
    # Request as many as is required to catch all the repos
    repos = []
    for i in range(1, math.ceil(repo_num / 100) + 1):

        # Create and request the url
        # Format the org in and append the querystring
        url = ORG_REPOS_URL.format(org) + PAGINATED_FORMAT.format(i)
        # Get the URL, take the text, convert it to a python object, add it to the array
        repos.extend(json.loads(requests.get(url, headers=headers).text))

    # Return the array
    return repos