import speech_recognition as sr
import subprocess
import pyautogui
import time
from datetime import datetime
import random
import calendar
from threading import Thread 
import pyaudio
p = pyaudio.PyAudio()


print("")
print("")
print("█░█ ▄▀█ █▄▀ █░█ █▄░█ ▄▀█   █▀▄▀█ ▄▀█ ▀█▀ ▄▀█ ▀█▀ ▄▀█")
print("█▀█ █▀█ █░█ █▄█ █░▀█ █▀█   █░▀░█ █▀█ ░█░ █▀█ ░█░ █▀█")
print("")
print("by kberkboz")
print("")

with open('Configurations\\language.txt', "r") as  f:
    language = [line.rstrip() for line in f]
    f.close()

if len(language)==0:
    while True:
        with open('Configurations\\language.txt', "w") as  f:
            print("Select Speech Recognition Language")
            print("==============================")
            print("0-Türkçe")
            print("1-English")
            print("==============================")
            b= input("")
            if b == "0":
                f.write("tr-tr")
                break
            elif b=="1":
                f.write("en-en")
                break
            f.close

with open('Configurations\\language.txt', "r") as  f:
    language = [line.rstrip() for line in f]
    f.close()



    
print("Setup")
print("==============================")
print("Zoom>Settings>Video>Turn off my video...")
print("Zoom>Settings>Video>Always show preview...[uncheck]")
print("Zoom>Settings>Audio>Automatically join audio...")
print("Zoom>Settings>Audio>Mute my microphone when joining a meeting")
print("Zoom>Settings>General>")
print("==============================")
print("Edit the files on the Days folder as:")
print("time")
print("meeting id")
print("password")
print("==============================")
print("Edit the files on the Configurations folder as:")
print("Add your auto-messages to autoChat")
print("Add the path to Zoom.exe to filePath")
print("Add the keywords to be listened for to keywords")
print("==============================")
print("")


def sign_in(meetingid, password):
    subprocess.call(dosya[0])
    l = None
    while l is None:
        l = pyautogui.locateOnScreen('Images\\join_button.png', grayscale = True, confidence= 0.7)
    pyautogui.moveTo(l)
    pyautogui.click()

    time.sleep(1)

    pyautogui.write(meetingid)
    time.sleep(1)
    pyautogui.press("enter")

    time.sleep(5)

    pyautogui.write(password)
    pyautogui.press("enter")

    print("==============================")
    print("Login Successful")
    print("==============================")




#Gerekli Dosyaları Açma
with open('Configurations\\autoChat.txt') as f:
    lines = [line.rstrip() for line in f]
with open('Days\\Monday.txt') as p:
    ptesi = [line.rstrip() for line in p]
with open('Days\\Tuesday.txt') as sl:
    sal = [line.rstrip() for line in sl]
with open('Days\\Wednesday.txt') as c:
    cars = [line.rstrip() for line in c]
with open('Days\\Thursday.txt') as pr:
    pers = [line.rstrip() for line in pr]
with open('Days\\Friday.txt') as cm:
    cuma = [line.rstrip() for line in cm]
with open('Configurations\\keywords.txt') as a:
    kelime = [line.rstrip() for line in a]
with open('Configurations\\filePath.txt') as d:
    dosya = [line.rstrip() for line in d]

#Programı Okuma ve ID-Şifre Değerlerini Verme
def loop1 ():
    while True:

        if (datetime.today().strftime('%A')) =="Monday":
            if any(time.strftime("%H:%M") in s for s in ptesi):
                m_id = ptesi[(ptesi.index(time.strftime("%H:%M")))+1]
                m_pswd =ptesi[(ptesi.index(time.strftime("%H:%M")))+2]
                sign_in(m_id, m_pswd)
                
        if (datetime.today().strftime('%A')) =="Tuesday":
            if any(time.strftime("%H:%M") in s for s in sal):
                m_id = sal[(sal.index(time.strftime("%H:%M")))+1]
                m_pswd =sal[(sal.index(time.strftime("%H:%M")))+2]
                sign_in(m_id, m_pswd)

        if (datetime.today().strftime('%A')) =="Wednesday":
            if any(time.strftime("%H:%M") in s for s in cars):
                m_id = cars[(cars.index(time.strftime("%H:%M")))+1]
                m_pswd =cars[(cars.index(time.strftime("%H:%M")))+2]
                sign_in(m_id, m_pswd)

        if (datetime.today().strftime('%A')) =="Thursday":
            if any(time.strftime("%H:%M") in s for s in pers):
                m_id = pers[(pers.index(time.strftime("%H:%M")))+1]
                m_pswd =pers[(pers.index(time.strftime("%H:%M")))+2]
                sign_in(m_id, m_pswd)

        if (datetime.today().strftime('%A')) =="Friday":
            if any(time.strftime("%H:%M") in s for s in cuma):
                m_id = cuma[(cuma.index(time.strftime("%H:%M")))+1]
                m_pswd =cuma[(cuma.index(time.strftime("%H:%M")))+2]
                sign_in(m_id, m_pswd)

        print ("Time Checked")
        time.sleep(60)

r = sr.Recognizer()
def loop2 (x):
    while True:
        with sr.Microphone(device_index= x) as source:
            r.adjust_for_ambient_noise(source)
        
            try:
                ses = r.listen(source, timeout=2, phrase_time_limit=5)
                print(r.recognize_google(ses, language=language[0]))
                giris = r.recognize_google(ses, language=language[0])

                for word in kelime: 
                    if word==giris:
                        pyautogui.hotkey('alt', 'h')
                        time.sleep(2)
                        x = random.randint(0,Len(lines)-1)
                        pyautogui.write((lines[x]))
                        time.sleep(2)


                        

            except sr.WaitTimeoutError:
                print("Timed out")

            except sr.UnknownValueError:
                print("I did not understand")

            except sr.RequestError:
                print("Could not connect to the internet")

thread1 = Thread(target=loop1)
thread1.start()



while True:
    a=input("Enable Auto-Chat-Responding? (y/n)\n")
    if a=="y":
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
                if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                    print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
        x= int(input("Enter index of the input device (Stereo Mix is recommended)\n"))

        thread2 = Thread(target=loop2(x))
        thread2.start()
        break

    elif(a=="n"):
        break
    else:
        continue




