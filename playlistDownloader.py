#imports
from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import eyed3


def download_playlist(playlist_url):
    # Get a list of all video URLs in the playlist
    playlist = Playlist(playlist_url)
    if playlist == None:
        print("Invalid playlist url...")
        return

    video_urls = playlist.video_urls
    if video_urls == None or len(video_urls) <= 0:
        print("Could not find any available video in this url...")
        return

    output_folder_name = playlist.title

    #generate paths
    downloaded_files_path   = './downloadedFiles/'
    output_folder_name      = "./convertedFiles/" + output_folder_name

    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)
    else:
        print("This playlist already been downloaded....")

    # The 'i' variable will make that the files has the same order that they have in the playlist
    i = 0
    for video_url in video_urls:
        i += 1
        try:
            # Initialize the Youtube video object
            yt = YouTube(video_url)
            stream = yt.streams.get_lowest_resolution()
            # Save the video to a local path
            stream.download(downloaded_files_path)
            files = os.listdir(downloaded_files_path)

            for file in files:
                # Get the downloaded path
                input_file_path = os.path.join(downloaded_files_path, file)
                print('Converting video: ' + input_file_path)

                # Initializ the conversor object
                clip = VideoFileClip(input_file_path)
                fileIndex = "{:03d}".format(i)
                output_file_path = os.path.join(output_folder_name, fileIndex + "_" + file).replace('.mp4', '.mp3')

                if not os.path.exists(output_file_path):
                    # Make the conversion
                    clip.audio.write_audiofile(output_file_path)

                    # Edit the converted file to add metadata
                    audio = eyed3.load(output_file_path)
                    audio.tag.title = str(file).replace(".mp4", "")
                    audio.tag.save()

                clip.close()    

                # Delete the youtube video from local path
                os.remove(input_file_path)
            
        except Exception as e:
            print(f"Something wrong happend with the video: {video_url}. Ex: {e}")