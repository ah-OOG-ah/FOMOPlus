# Define URLs
BASE_URL = "https://api.github.com"

# Organization URLS
ORG_URL = f"{BASE_URL}/orgs/{{0}}"
ORG_REPOS_URL = f"{ORG_URL}/repos"

# Headers
HEADERS_FORMAT = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {{0}}",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Query string
PAGINATED_FORMAT = f"?per_page=100&page={{0}}"
