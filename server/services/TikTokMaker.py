import requests
from download_clip import download_clip

def fetch_and_download_twitch_clip(username):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": "kmbu7hh74r8brdi2nbj40i3rvj2rmw",
        "client_secret": "ct4hxwwkpkzlmj3yeb4vm17jzakwqc",
        "grant_type": "client_credentials"
    }

    response = requests.post(url, params=params)
    data = response.json()
    access_token = data['access_token']

    headers = {
        "Client-ID": "kmbu7hh74r8brdi2nbj40i3rvj2rmw",
        "Authorization": f"Bearer {access_token}"
    }

    user_url = f"https://api.twitch.tv/helix/users?login={username}"
    user_response = requests.get(user_url, headers=headers)
    user_data = user_response.json()

    # The broadcaster_id will be in the 'data' field of the response
    broadcaster_id = user_data['data'][0]['id']

    print(f"The broadcaster ID for {username} is: {broadcaster_id}")

    clips_url = f"https://api.twitch.tv/helix/clips?broadcaster_id={broadcaster_id}&first=1&sort=created_at"
    clips_response = requests.get(clips_url, headers=headers)
    clips_data = clips_response.json()

    # The most recent clip will be the first and only item in the 'data' field of the response
    most_recent_clip = clips_data['data'][0]
    print(f"Most Recent Clip ID: {most_recent_clip['id']}, Title: {most_recent_clip['title']}, URL: {most_recent_clip['url']}")

    thumbnail_url = most_recent_clip['thumbnail_url']

    download_clip(thumbnail_url)
