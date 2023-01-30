# import datetime
import asyncio
import pathlib
import json
import http

from classes import *

# If needed, set your name and personal access token
username = None
pat = None

# The name of the organization you want to scan
org_name = "EpicGames"

if __name__ == "__main__":

    # Get the repos owned by an organization and dump them
    repos = get_org_repos(org_name)
    raw_data = json.dumps(repos, indent=2)

    # Generate the directory and files for the org
    org_dir = f"./out/{org_name}"
    org_repos_file = org_dir + "/repos.json"

    # Create the org dir if not existing
    if not pathlib.Path(org_dir).is_dir():
        
        pathlib.Path(org_dir).mkdir()

    # Overwrite/create the repo file
    with open(org_repos_file, "w+") as file:

        file.write(raw_data)