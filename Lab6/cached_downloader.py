from downloader import Downloader
from simple_downloader import SimpleDownloader

class CachedDownloader(Downloader):
    def __init__(self, simple_downloader: SimpleDownloader) -> None:
        self.simple_downloader = simple_downloader
        self.cache = {}

    def download(self, url: str) -> bytes:
        if url in self.cache:
            print(f"Fetching: {url}")
            return self.cache[url]
        else:
            print(f"Downloading: {url}")
            data = self.simple_downloader.download(url)
            self.cache[url] = data
            return data
