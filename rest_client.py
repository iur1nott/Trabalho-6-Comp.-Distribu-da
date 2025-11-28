# rest_client.py
import requests
import time
import os

BASE_URL = "http://localhost:5000"

def main():
    # Listar músicas
    print("🎵 Catálogo de músicas (REST):")
    response = requests.get(f"{BASE_URL}/tracks")
    if response.status_code != 200:
        print(f"Erro ao buscar catálogo: {response.status_code}")
        return
    
    tracks = response.json()
    for track in tracks:
        print(f"[{track['id']}] {track['title']} - {track['artist']} ({track['album']}) | {track['duration_sec']}s")
    
    # Escolher música
    try:
        track_id = int(input("\nDigite o ID da música para streaming: "))
    except ValueError:
        print("ID inválido!")
        return
    
    # Streaming
    output_file = f"rest_stream_{track_id}.mp3"
    print(f"\n🔊 Iniciando streaming da música (ID: {track_id})...")
    
    try:
        with requests.get(f"{BASE_URL}/stream/{track_id}", stream=True) as r:
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