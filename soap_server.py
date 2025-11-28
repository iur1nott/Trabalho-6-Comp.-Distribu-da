# soap_server.py
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import base64
from music_data import MUSIC_CATALOG

class Track(ComplexModel):
    id = Integer
    title = Unicode
    artist = Unicode
    album = Unicode
    genre = Unicode
    duration_sec = Integer

class MusicService(ServiceBase):
    @rpc(_returns=Array(Track))
    def GetTrackList(ctx):
        return [Track(**track) for track in MUSIC_CATALOG]

    @rpc(Integer, _returns=Unicode)
    def StreamTrack(ctx, track_id):
        track = next((t for t in MUSIC_CATALOG if t["id"] == track_id), None)
        if not track or not track["file"]:
            return ""
        try:
            with open(track["file"], "rb") as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except FileNotFoundError:
            return ""

application = Application(
    [MusicService],
    tns='spyne.examples.music',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server running on http://0.0.0.0:8000/?wsdl")
    server.serve_forever()