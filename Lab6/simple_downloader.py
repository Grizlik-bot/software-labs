from downloader import Downloader

class SimpleDownloader(Downloader):
    def download(self, url: str) -> bytes:
        print(f"Downloading from: {url}")
        return b"Example of downloaded smth"
