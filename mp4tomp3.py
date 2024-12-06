from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_mp3(mp4_file, output_folder=None):
    """
    Convierte un archivo MP4 a MP3.
    
    Args:
        mp4_file (str): Ruta del archivo MP4.
        output_folder (str, opcional): Carpeta donde se guardará el archivo MP3. 
                                       Si no se especifica, se usa la misma carpeta que el MP4.
    
    Returns:
        str: Ruta del archivo MP3 convertido.
    """
    if not os.path.isfile(mp4_file):
        print(f"El archivo {mp4_file} no existe.")
        return None
    
    # Obtener nombre del archivo y carpeta
    base_name = os.path.splitext(os.path.basename(mp4_file))[0]
    output_folder = output_folder or os.path.dirname(mp4_file)
    mp3_file = os.path.join(output_folder, f"{base_name}.mp3")
    
    try:
        # Cargar el archivo de video
        video_clip = VideoFileClip(mp4_file)
        # Extraer y guardar el audio como MP3
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        video_clip.close()
        print(f"Archivo convertido exitosamente: {mp3_file}")
        return mp3_file
    except Exception as e:
        print(f"Error al convertir {mp4_file} a MP3: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    input_file = input("Ingresa la ruta del archivo MP4: ").strip()
    output_folder = input("Ingresa la carpeta de salida (opcional, presiona Enter para usar la misma carpeta): ").strip()
    output_folder = output_folder if output_folder else None
    convert_mp4_to_mp3(input_file, output_folder)
