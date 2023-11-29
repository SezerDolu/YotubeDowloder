import pytube

url = input("Enter video URL: ")
path = r"C:\Users\sedol\OneDrive\Masaüstü\YoutubeDownload"  # Dikkat: \ karakterlerini çift \\ olarak yazmalısınız.

yt = pytube.YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(output_path=path)

print("Video indirme tamamlandı!")




