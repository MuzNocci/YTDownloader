import os, re
from pytubefix import YouTube



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ytDownloader:


    def downloader(self, url):

        if not self.is_valid_youtube_url(url):
            print("Invalid YouTube URL.")
            return None

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        try:
            downloads_path = os.path.join(BASE_DIR, 'downloads')
            if not os.path.exists(downloads_path):
                os.makedirs(downloads_path, exist_ok=True)
                os.chmod(downloads_path, 0o755)

            stream.download(downloads_path)
            print('Video downloaded successfully!')
            return stream.default_filename

        except Exception as e:
            print('Error: Failed to download the video!', e)
            return None


    def is_valid_youtube_url(self, url):

        if not url:
            print("Invalid YouTube URL.")
            return False
        
        yt_regex = (
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*[?&]v=[\w-]+'
        )
        return re.match(yt_regex, url) is not None
        

if __name__ == '__main__':

    downloader = ytDownloader()

    while True:
        input_url = input('Enter the YouTube video URL: ')
        print('Downloading...')
        downloader.downloader(input_url)

        if input('Do you want to download another video? (y/n): ').lower() != 'y':
            break