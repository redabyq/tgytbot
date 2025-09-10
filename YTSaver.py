from pytubefix import YouTube
from pydub import AudioSegment
import os
import subprocess
import requests
from AutoLog import log 
class Downloader:
    def __init__(self, lnk):
        self.link = lnk
        self.yt =YouTube(self.link)
        log("w","Видео обработано")
    def downloadpreview(self):
        
        response = requests.get(self.yt.thumbnail_url)
        with open(f"{self.getname()}.jpg", "wb") as file:
            file.write(response.content)
        return f"{self.getname()}.jpg"
    def getlength(self):
        log("w",'Длина '+str(self.yt.length))
        return self.yt.length
    def getname(self):

        return self.yt.title

    def getqualities(self):

        """"""

        quarArr=[]
        for i in self.yt.streams:
            quarArr.append(i.resolution)
        quarArr=set(quarArr)
        quarArr.remove(None)

        return quarArr


    def downloadmp4(self,quality:str="720p"):
        
        quarArr = self.getqualities()
        if quality not in quarArr:
            raise ValueError("Такого качества нет")
        video_stream = self.yt.streams.filter(res=quality, file_extension='mp4').first()
        video_filename = "rerhuinya.mp4"
        video_stream.download(filename=video_filename)
        audio_stream = self.yt.streams.filter(only_audio=True, file_extension='mp4').first()
        audio_filename = "rerauhuinya.mp4"
        audio_stream.download(filename=audio_filename)
        output_filename = f"{self.yt.title}.mp4"
        cmd = ['ffmpeg','-i', video_filename,'-i', audio_filename,'-c', 'copy', '-shortest',output_filename,'-y' ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(video_filename)
        os.remove(audio_filename)
        log("w",f"Видео сохранено: {output_filename}")
        return output_filename


    def downloadmp3(self):

        t= self.yt.streams.filter(only_audio=True).all()
        t[0].download()
        audio = AudioSegment.from_file(f"{t[0].title}.m4a", format="m4a")
        audio.export(f"{t[0].title}.mp3", format="mp3")
        file_path =f"{t[0].title}.m4a" 
        os.remove(file_path)  
        log("w",f"Аудио сохранено: {t[0].title}.mp3")
        return f"{t[0].title}.mp3"
# vid= Downloader("https://www.youtube.com/watch?v=QF0ACRyNDbM")
# vid.getlength()
# print(vid.downloadpreview())
# Downloader.downloadmp3("https://www.youtube.com/watch?v=QF0ACRyNDbM")
# print( Downloader.getqualities("https://www.youtube.com/watch?v=QF0ACRyNDbM"))
