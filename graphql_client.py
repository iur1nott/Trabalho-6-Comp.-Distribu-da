# graphql_client.py
import requests
import json
import time
import os

GRAPHQL_URL = "http://localhost:5001/graphql"

def execute_query(query, variables=None):
    response = requests.post(
        GRAPHQL_URL,
        json={'query': query, 'variables': variables or {}},
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise Exception(f"Query falhou com status {response.status_code}: {response.text}")
    return response.json()

def main():
    # Listar músicas
    print("🎵 Catálogo de músicas (GraphQL):")
    query = '''
    {
      tracks {
        id
        title
        artist
        album
        durationSec
        streamUrl
      }
    }
    '''
    
    try:
        result = execute_query(query)
        tracks = result['data']['tracks']
        for track in tracks:
            print(f"[{track['id']}] {track['title']} - {track['artist']} ({track['album']}) | {track['durationSec']}s")
    except Exception as e:
        print(f"❌ Erro ao buscar catálogo: {e}")
        return
    
    # Escolher música
    try:
        track_id = int(input("\nDigite o ID da música para streaming: "))
    except ValueError:
        print("ID inválido!")
        return
    
    # Obter URL de streaming
    query_track = '''
    query GetTrack($id: ID!) {
      track(id: $id) {
        id
        title
        streamUrl
      }
    }
    '''
    
    try:
        result = execute_query(query_track, variables={"id": str(track_id)})
        track = result['data']['track']
        if not track:
            print(f"❌ Música ID {track_id} não encontrada")
            return
    except Exception as e:
        print(f"❌ Erro ao buscar detalhes da música: {e}")
        return
    
    # Streaming via URL REST
    stream_url = f"http://localhost:5001{track['streamUrl']}"
    output_file = f"graphql_stream_{track_id}.mp3"
    print(f"\n🔊 Iniciando streaming: {track['title']}...")
    
    try:
        with requests.get(stream_url, stream=True) as r:
            r.raise_for_status()
            total_bytes = 0
            
            with open(output_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
                        total_bytes += len(chunk)
                        print(f"⏬ Recebidos {total_bytes} bytes...", end='\r')
            
            print(f"\n✅ Streaming concluído! Arquivo salvo como '{output_file}'")
            print(f"▶️ Execute: {os.path.abspath(output_file)}")
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro no streaming: {e}")
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    main()