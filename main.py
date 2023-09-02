from playlistDownloader import download_playlist, download_playlist_as_mpg

def main():

    playlists = {
        "./Pop Rock Nacional Acústico/": "https://www.youtube.com/playlist?list=PLR3Vhhv_y4m7bBYUcnwJBLlWAPR2lX-C6",
        "./Eletrônicas 2023/": "https://www.youtube.com/playlist?list=PLoZDU1CpacjwRoo4lXhMscEVHFSu1TQ1T",
        "./Top Global - Spotify/": "https://www.youtube.com/playlist?list=PLgzTt0k8mXzEk586ze4BjvDXR7c-TUSnx",
        "./Top Brasil 2022 - Spotify/": "https://www.youtube.com/playlist?list=PLLSRxlC_12JNhrqw899C030xd2g5qfICI",
        "./Rap Internacional/": "https://www.youtube.com/playlist?list=PLJn4hP4ODKFyHR5UQcRG7gJhiqtoyavUs"
    }

    for outputfolder, playlist_url in playlists.items():
        download_playlist_as_mpg(playlist_url, outputfolder)


if __name__ == "__main__":
    main()