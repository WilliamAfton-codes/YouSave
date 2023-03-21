from pytube import YouTube
import os
import pathlib
import animation
os.chdir(pathlib.Path.home() / "Downloads")
print("ALL VIDEOS WILL BE SAVED IN THE 'Downloads' DIRECTORY OF WINDOWS")
link = str(input("\nPaste your fill YouTube link here: "))
print("\n")
wait = animation.Wait('bar', text='Downloading... ', color='red')
def mainScript():
    global link
    global wait
    while True:
        try:
            wait.start()
            yt=YouTube(link)
            yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
            wait.stop()
            break
        except Exception:
            wait.stop()
            os.system('cls')
            print("Invalid Youtube Link!")
            link = str(input("\nPaste your fill YouTube link here: "))
mainScript()
print("Video saved successfully!")
input("[Press Enter to exit]")
