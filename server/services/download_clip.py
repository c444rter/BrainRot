import requests
import os

def download_clip(thumbnail_url):
    index = thumbnail_url.find('-preview')
    clip_url = thumbnail_url[:index] + '.mp4'
    r = requests.get(clip_url)

    if r.headers['Content-Type'] == 'binary/octet-stream':
        if not os.path.exists('files/clips'): 
            os.makedirs('files/clips')
        filename = thumbnail_url.split("/")[-1].replace('-preview', '') + '.mp4'
        with open(os.path.join('files/clips', filename), 'wb') as f:
            f.write(r.content)

    else:
        print(f'Failed to download clip from thumb: {thumbnail_url}')
