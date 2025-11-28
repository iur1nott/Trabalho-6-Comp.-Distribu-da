# grpc_server.py
import grpc
from concurrent import futures
import music_pb2
import music_pb2_grpc
from music_data import MUSIC_CATALOG
import time

class MusicService(music_pb2_grpc.MusicServiceServicer):
    def GetTrackList(self, request, context):
        tracks = [
            music_pb2.Track(
                id=t["id"],
                title=t["title"],
                artist=t["artist"],
                album=t["album"],
                genre=t["genre"],
                duration_sec=t["duration_sec"]
            )
            for t in MUSIC_CATALOG
        ]
        return music_pb2.TrackListResponse(tracks=tracks)

    def StreamTrack(self, request, context):
        track = next((t for t in MUSIC_CATALOG if t["id"] == request.track_id), None)
        if not track:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Track not found")
            return
        
        try:
            with open(track["file"], "rb") as f:
                while chunk := f.read(4096):
                    yield music_pb2.TrackChunk(data=chunk)
                    time.sleep(0.01)  # Simula streaming contínuo
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Audio file not found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    music_pb2_grpc.add_MusicServiceServicer_to_server(MusicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()