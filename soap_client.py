# soap_client.py
from zeep import Client
import base64
import os
import time

WSDL_URL = "http://localhost:8000/?wsdl"

def main():
    try:
        client = Client(WSDL_URL)
    except Exception as e:
        print(f"❌ Erro ao conectar ao serviço SOAP: {e}")
        return
    
    # Listar músicas
    print("🎵 Catálogo de músicas (SOAP):")
    try:
        tracks = client.service.GetTrackList()
        for track in tracks:
            print(f"[{track.id}] {track.title} - {track.artist} ({track.album}) | {track.duration_sec}s")
    except Exception as e:
        print(f"❌ Erro ao buscar catálogo: {e}")
        return
    
    # Escolher música
    try:
        track_id = int(input("\nDigite o ID da música para download: "))
    except ValueError:
        print("ID inválido!")
        return
    
    # Download (SOAP não faz streaming nativo, baixa completo)
    output_file = f"soap_download_{track_id}.mp3"
    print(f"\n⬇️ Baixando música (ID: {track_id})...")
    
    try:
        audio_base64 = client.service.StreamTrack(track_id)
        if not audio_base64:
            print(f"❌ Música ID {track_id} não encontrada ou arquivo ausente")
            return
        
        # Converter base64 para arquivo
        audio_data = base64.b64decode(audio_base64)
        with open(output_file, "wb") as f:
            f.write(audio_data)
        
        print(f"✅ Download concluído! Arquivo salvo como '{output_file}'")
        print(f"▶️ Execute: {os.path.abspath(output_file)}")
    
    except Exception as e:
        print(f"❌ Erro no download: {e}")
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    main()