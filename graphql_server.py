# graphql_server.py
import graphene
from flask import Flask, send_file
from flask_graphql import GraphQLView
from music_data import MUSIC_CATALOG

class Track(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    artist = graphene.String()
    album = graphene.String()
    genre = graphene.String()
    duration_sec = graphene.Int()
    stream_url = graphene.String()

class Query(graphene.ObjectType):
    tracks = graphene.List(Track)
    track = graphene.Field(Track, id=graphene.ID(required=True))

    def resolve_tracks(root, info):
        return [
            Track(
                id=t["id"],
                title=t["title"],
                artist=t["artist"],
                album=t["album"],
                genre=t["genre"],
                duration_sec=t["duration_sec"],
                stream_url=f"/stream/{t['id']}"
            )
            for t in MUSIC_CATALOG
        ]

    def resolve_track(root, info, id):
        id_int = int(id)
        track_data = next((t for t in MUSIC_CATALOG if t["id"] == id_int), None)
        if not track_data:
            return None
        return Track(
            id=track_data["id"],
            title=track_data["title"],
            artist=track_data["artist"],
            album=track_data["album"],
            genre=track_data["genre"],
            duration_sec=track_data["duration_sec"],
            stream_url=f"/stream/{track_data['id']}"
        )

schema = graphene.Schema(query=Query)
app = Flask(__name__)

@app.route('/stream/<int:track_id>')
def stream_track(track_id):
    track = next((t for t in MUSIC_CATALOG if t["id"] == track_id), None)
    if not track:
        return "Track não encontrada", 404
    return send_file(
        track["file"],
        mimetype='audio/mpeg',
        as_attachment=False,
        conditional=True
    )

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(port=5001, debug=True)