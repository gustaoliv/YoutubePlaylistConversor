from playlistDownloader import download_playlist

def main():
    playlist_url = "https://www.youtube.com/playlist?list=PL5LpFMyPnSV9HrkdOP-eb_nr9wturu0B6"
    download_playlist(playlist_url)


if __name__ == "__main__":
    main()