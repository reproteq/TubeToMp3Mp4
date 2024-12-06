import yt_dlp
import os

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Nombre del archivo descargado
        'format': 'best',  # Descargar la mejor calidad disponible
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Solicitar al usuario la URL del video de YouTube
    video_url = input("Introduce la URL completa del video de YouTube: ")

    # Obtener la ruta donde está ubicado el script ejecutado
    # Esto asegura que obtienes la ruta correcta incluso al arrastrar el archivo
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Solicitar al usuario la carpeta de destino, usando la carpeta actual del script como predeterminada
    output_folder = input(f"Introduce la ruta donde deseas guardar el video (por defecto: {script_directory}): ") or script_directory

    # Llamar a la función para descargar el video
    download_youtube_video(video_url, output_folder)
