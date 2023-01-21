#imports
import unicodedata
from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import eyed3

#generate a waiting list to download
waiting_list = {}

#insert all desired playlist to download waiting list
while True:
    playlist_url = str(input("Insira a url da playlist (Digite CANCELAR para sair): "))
    
    if playlist_url.strip().upper() == "CANCELAR":
        break

    # Get a list of all video URLs in the playlist

    playlist = Playlist(playlist_url)

    video_urls = playlist.video_urls

    output_folder_name = playlist.title

    if output_folder_name in waiting_list:
        print("Essa playlist já foi adicionada à lista de espera...")
        continue

    waiting_list[output_folder_name] = video_urls


#generate paths
downloaded_files_path = './downloadedFiles/'

for playlistName, video_urls in waiting_list.items():
    output_folder_name = "./convertedFiles/" + playlistName
    
    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)

    i = 0
    for video_url in video_urls:
        i += 1
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_lowest_resolution()
            stream.download(downloaded_files_path)

            files = os.listdir(downloaded_files_path)

            for file in files:
                input_file_path = os.path.join(downloaded_files_path, file)
                print('Converting video: ' + input_file_path)
                clip = VideoFileClip(input_file_path)
                fileIndex = "{:03d}".format(i)
                output_file_path = os.path.join(output_folder_name, fileIndex + "_" + file).replace('.mp4', '.mp3')

                if not os.path.exists(output_file_path):
                    clip.audio.write_audiofile(output_file_path)

                    audio = eyed3.load(output_file_path)
                    audio.tag.title = str(file).replace(".mp4", "")
                    audio.tag.save()

                clip.close()    

                os.remove(input_file_path)
            
        except Exception as e:
            print(f"Algo de inesperado aconteceu com o video: {video_url}. Ex: {e}")