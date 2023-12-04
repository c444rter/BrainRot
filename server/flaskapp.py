from flask import Flask, jsonify
from flask_cors import CORS
from TikTokMaker import fetch_and_download_twitch_clip

flaskapp = Flask(__name__)
CORS(flaskapp)

@flaskapp.route('/get_twitch_clip/<username>', methods=['GET'])

def get_twitch_clip(username):
    fetch_and_download_twitch_clip(username)

    return jsonify({"message": f"Twitch clip for {username} fetched and downloaded successfully!"})


if __name__ == "__main__":
    flaskapp.run(debug=True)