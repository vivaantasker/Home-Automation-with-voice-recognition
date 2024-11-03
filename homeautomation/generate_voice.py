import sounddevice 
from scipy.io.wavfile import write
import gtts
import playsound
import os

def audiostore(name):
    name=name
    text = "Do you want to enter a command ?"
    sound = gtts.gTTS(text, lang="en")
    sound.save("ques.mp3")
    playsound.playsound("ques.mp3")

    ans = input("Enter (y/n)").lower()

    while ans == "y":

        ask_record = "Do you want to start recording ?"
        ask_user = gtts.gTTS(ask_record, lang="en") 
        ask_user.save("ready.mp3")
        playsound.playsound("ready.mp3")

        tell_record = "Press 'r' to start recording ?"
        tell_user = gtts.gTTS(tell_record, lang="en")
        tell_user.save("rec.mp3")
        playsound.playsound("rec.mp3")

        user_rec = input("press r").lower()

        while user_rec == "r":

            started = "Recording started"
            start_rec = gtts.gTTS(started, lang = "en")
            start_rec.save("indicate.mp3")
            playsound.playsound("indicate.mp3")

            audio = sounddevice.rec(5*44100,samplerate=44100,channels=1)
            sounddevice.wait()
            write(name+".wav",44100,audio)

            last = "Do you want to continue recording ?"
            last_rec = gtts.gTTS(last,lang="en")
            last_rec.save("lastques.mp3")
            playsound.playsound("lastques.mp3")

            user_rec = input("press (y/n)")

            if user_rec == 'n':
                break
            
        confirm_record = "Press 'c' to continue ahead ?"
        confirm_user = gtts.gTTS(confirm_record, lang="en")
        confirm_user.save("conf.mp3")
        playsound.playsound("conf.mp3")

        ans  = input("press 'c' ").lower()

        if ans == "c":
            break


    delete_file("ques.mp3")
    delete_file("ready.mp3")
    delete_file("rec.mp3")
    delete_file("conf.mp3")
    delete_file("start_rec.mp3")
    delete_file("indicate.mp3")
    delete_file("lastques.mp3")


    path = os.getcwd()
    file_name = name+'.wav'

    file_path = os.path.join(path,file_name)
    return file_path


def delete_file(filepath):

    if os.path.exists(filepath):
        os.remove(filepath)
        print("Deleted "+ filepath)
    else:
        print("File Doesn't exist !")
