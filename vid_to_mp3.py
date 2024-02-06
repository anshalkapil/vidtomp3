import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import subprocess
import os

root = tk.Tk()
root.geometry("800x800")

def main():
    upload_button = tk.Button(root, text="Upload Video File", command=file_upload)
    upload_button.pack()
    

def file_upload():
    video_file_path = filedialog.askopenfilename()
    file_name = os.path.basename(video_file_path)
    file_name = os.path.splitext(file_name)[0]
    subtitles_file_path = convert(video_file_path,file_name)
    print(subtitles_file_path)
    
def convert(video_file_path,file_name):
    audio_file_path = f"D:/Autosubber/{file_name}.mp3"
    subprocess.run(['ffmpeg', '-i', video_file_path, '-vn', '-codec:a', 'mp3', audio_file_path])
    finished = tk.Label(root, text="Finished!")
    finished.pack()
    

main()  
root.mainloop()
