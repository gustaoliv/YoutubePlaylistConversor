import tkinter as tk
from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import tkinter as tk
from Utils import *


def download_playlist(playlist_url, download_type, output_folder, textarea):
    match download_type:
        case "MP4 (Alta Qualidade)":
            download_playlist_mp4(playlist_url, "HIGH", output_folder, textarea)
        case "MP4 (Baixa Qualidade)":
            download_playlist_mp4(playlist_url, "LOW", output_folder, textarea)
        case "MPG":
            download_playlist_as_mpg(playlist_url, output_folder, textarea)
        case _:
            textarea.insert(tk.END, "Tipo inválido...\n", "failed")


def download_playlist_mp4(playlist_url, qualityType, output_folder, textarea):
    # Get a list of all video URLs in the playlist
    playlist = Playlist(playlist_url)
    if playlist == None:
        textarea.insert(tk.END, "Não foi possível encontrar nenhum vídeo nessa url...\n", "failed")
        return
    
    video_urls = playlist.video_urls
    if video_urls == None or len(video_urls) <= 0:
        textarea.insert(tk.END, "Não foi possível encontrar nenhum vídeo nessa url...\n", "failed")
        return
    else:
        textarea.insert(tk.END, f"Foram encontrados {len(video_urls)} vídeos, começando a baixar...\n")
    
    output_folder_name = remove_accents(str(playlist.title).replace(" ", "_").replace("-", "_").replace("__", "_").title()).strip()

    full_path = os.path.join(output_folder, output_folder_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    # The 'i' variable will make that the files has the same order that they have in the playlist
    i = 0
    for video_url in video_urls:
        i += 1
        try:                
            yt = YouTube(video_url)
            if qualityType == "HIGH":

                resolution_list = ["2160p", "1440p", "1080p", "720p" ,"480p" ,"360p" ,"240p" ,"144p"]
                for resolution in resolution_list:
                    stream = yt.streams.get_by_resolution(resolution)
                    if(stream != None):
                        break
            else:
                stream = yt.streams.get_lowest_resolution()

            if stream == None:
                textarea.insert(tk.END, "Aconteceu alguma falha durante o download do video...\n", "failed")
                continue

            # Save the video to a local path
            stream.download(full_path)
            video_name = yt.title
            textarea.insert(tk.END, f"Download concluído: {video_name}\n", "success")
            
        except Exception as e:
            textarea.insert(tk.END, "Aconteceu alguma falha durante o download do video...\n", "failed")
            continue


def download_playlist_as_mpg(playlist_url, output_folder, textarea):
    # Get a list of all video URLs in the playlist
    playlist = Playlist(playlist_url)
    if playlist == None:
        textarea.insert(tk.END, "Url invalida para playlist...\n", "failed")
        return

    video_urls = playlist.video_urls
    if video_urls == None or len(video_urls) <= 0:
        textarea.insert(tk.END, "Não foi possível encontrar nenhum vídeo nessa url...\n", "failed")
        return
    else:
        textarea.insert(tk.END, f"Foram encontrados {len(video_urls)} vídeos, começando a baixar...\n")

    #generate paths
    downloaded_files_path   = './downloadedFiles/'

    output_folder_name = remove_accents(str(playlist.title).replace(" ", "_").replace("-", "_").replace("__", "_").title()).strip()

    full_path = os.path.join(output_folder, "MPG_" + output_folder_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    # The 'i' variable will make that the files has the same order that they have in the playlist
    i = 0
    for video_url in video_urls:            
        try:
            # Initialize the Youtube video object
            yt = YouTube(video_url)
            stream = yt.streams.get_by_resolution("480p")
            if stream == None:
                stream = yt.streams.get_by_resolution("360p")

            # Save the video to a local path
            stream.download(downloaded_files_path)
            files = os.listdir(downloaded_files_path)

            video_name = yt.title
            textarea.insert(tk.END, f"Download concluído: {video_name}...Realizando conversão...\n", "success")

            for file in files:
                # Get the downloaded path
                input_file_path = os.path.join(downloaded_files_path, file)

                # Initializ the conversor object
                clip = VideoFileClip(input_file_path)
                i += 1
                fileIndex = "{:03d}".format(i)
                output_file_path = os.path.join(full_path, fileIndex + "_" + file).replace('.mp4', '.mpg')

                if not os.path.exists(output_file_path):
                    # Make the conversion
                    clip.write_videofile(output_file_path, codec='mpeg2video')

                clip.close()    

                # Delete the youtube video from local path
                textarea.insert(tk.END, f"Vídeo convertido com sucesso: {video_name}\n", "success")
                os.remove(input_file_path)

        except Exception as e:
                textarea.insert(tk.END, f"Ocorreu uma falha para baixar o vídeo {video_url}\n", "failed")

