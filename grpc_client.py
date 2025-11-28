# grpc_client.py
import grpc
import music_pb2
import music_pb2_grpc
import time

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = music_pb2_grpc.MusicServiceStub(channel)
        
        # Listar todas as músicas
        print("🎵 Catálogo de músicas:")
        response = stub.GetTrackList(music_pb2.GetTrackListRequest())
        for track in response.tracks:
            print(f"[{track.id}] {track.title} - {track.artist} ({track.album}) | {track.duration_sec}s")
        
        # Escolher música para streaming
        track_id = int(input("\nDigite o ID da música para streaming: "))
        
        # Streaming com feedback em tempo real
        output_file = f"streamed_track_{track_id}.mp3"
        print(f"\n🔊 Iniciando streaming da música (ID: {track_id})...")
        bytes_received = 0
        
        with open(output_file, "wb") as f:
            for chunk in stub.StreamTrack(music_pb2.TrackRequest(track_id=track_id)):
                f.write(chunk.data)
                bytes_received += len(chunk.data)
                print(f"⏬ Recebidos {bytes_received} bytes...", end='\r')
        
        print(f"\n✅ Streaming concluído! Arquivo salvo como '{output_file}'")

if __name__ == '__main__':
    main()