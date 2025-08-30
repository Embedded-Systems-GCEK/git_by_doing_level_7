import requests

def users_forked():
    forked_users = []
    url = "https://api.github.com/repos/aruncs31s/programming/forks"
    headers = {
        "Accept": "application/vnd.github+json",
        # "Authorization": "Bearer <YOUR-TOKEN>",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    
    for fork in response.json():
    # print(f"Fork ID: {fork['id']}, Fork Name: {fork['full_name']}")
        forked_users.append(fork['owner']['login'])
    return forked_users


if __name__ == "__main__":
    users = users_forked()
    print("Users who forked the repository:")
    for user in users:
        print(f"- {user}")