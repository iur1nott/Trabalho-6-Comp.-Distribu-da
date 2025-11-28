# rest_server.py
from flask import Flask, send_file, jsonify
from music_data import MUSIC_CATALOG as TRACKS

app = Flask(__name__)

@app.route('/tracks', methods=['GET'])
def get_tracks():
    return jsonify(TRACKS)

@app.route('/stream/<int:track_id>', methods=['GET'])
def stream_track(track_id):
    track = next((t for t in TRACKS if t["id"] == track_id), None)
    if not track:
        return "Track não encontrada", 404
    return send_file(
        track["file"],
        mimetype='audio/mpeg',
        as_attachment=False,
        conditional=True
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)