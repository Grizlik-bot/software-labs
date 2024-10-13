from simple_downloader import SimpleDownloader
from cached_downloader import CachedDownloader

def main():
    downloader = CachedDownloader(SimpleDownloader())

    data1 = downloader.download("https://smth.com/1")
    data2 = downloader.download("https://smth.com/2")
    data3 = downloader.download("https://smth.com/3")

if __name__ == "__main__":
    main()
