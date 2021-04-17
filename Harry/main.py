import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import smtplib
import random
import pyautogui
import time
import pyttsx3
import os
import pyaudio
import wikipedia
import datetime
import webbrowser
import speech_recognition as sr
py = pyaudio.PyAudio()
r1=sr.Recognizer()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wiseme():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("good morning  Mr. Hariom ! , have a nice day sir")
    elif hours>=12 and hours<18:
        speak("good afternoon Mr. Hariom !")
    elif hours >=18 and hours<22:
        speak("good evening Mr. Hariom !")
    else:
        speak("good night Mr. Hariom have a sweet dream sir ")
    speak("i am  Harry sir , how may i help you sir ")

def takecommand():
    #"this function take input from microphone of user device and return string output"
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            speak("listening....")
            r.pause_threshold=1
            r.enrgy_threshold=800
            audio=r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language='en-in')#recongize_bing()
            #recongnize_google()recongize_houndify()recongize_ibm() recongize_wit() recongize_sphins()
            print("you said " , query)
        except Exception as e:
            #it gives all exception during runtime
            #print(e)# it will print error
            print("say that again please...")
            return "None"
        return query
def sendEmail(to, content):
    password='mangoman'
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('mishrahariom7926@gmai.com','mangoman')
    server.sendmail('misrahariom7926@gmail.com',to,content)
    server.close()
def alarm():
    speak(" sir enter  the hour of alarm ")
    alarmhour=int(input("enter hours of alarm"))
    speak("now enter   the minute of alarm ")
    alarmmin=int(input("enter the minute of alarm"))
    speak("sir ,  enter am or pm  of  alarm ")
    am_pm=str(input("am or pm :"))
    r="what should be reminder of alarm"
    print(r)
    speak(r)
    reminder=takecommand()
    speak("reminder  and alarm is set")
    am_pm.lower()
    if(am_pm=="pm"):
        alarmhour=int(alarmhour) + 12
    while(1==1):
        if (alarmhour==datetime.datetime.now().hour and
            alarmmin==datetime.datetime.now().minute):
            alarm_sound="wake up  sir  \n wake up sir\nwake up  sir "
            speak(alarm_sound)
            music_dir='C:\\Users\\Mr. Hariom\\Music'
            q=random.randrange(1,434)
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[q]))
            #continue # for not play a music only alarm_sound
            break# for both music and alarm_sound
def check_phone_number():
    speak("enter the phone number sir")
    num=input("enter phone number with ISD code")
    print("entered number is "+ num)
    #for check the carrier of number
    ser_num=phonenumbers.parse(num ,"RO")
    car=carrier.name_for_number(ser_num ,"en")
    car_info="carrier of phone number is " + car
    print(car_info)
    speak(car_info)
    #for checking the country of number
    ch_number=phonenumbers.parse(num ,"CH")
    coun=geocoder.description_for_number(ch_number,"en")
    count_info=("number from " + coun )
    print(count_info)
    speak(count_info)
def google():
    url_google='https://www.google.com/search?q='
    search_on_google="what i should search  on google"
    print(search_on_google)
    speak(search_on_google)
    get_google=takecommand()
    webbrowser.get().open(url_google+get_google)
def youtube():
    url_youtube='https://www.youtube.com/results?search_query='
    search_on_youtube="what i should search  on youtube"
    print(search_on_youtube)
    speak(search_on_youtube)
    get_youtube=takecommand()
    webbrowser.get().open(url_youtube+get_youtube)
    time.sleep(2)
    speak("should i play first video sir ")
    Lis=takecommand()
    if Lis=="yes" or "yehhh" or "ya sure":
        speak("playing the first video sir")
        time.sleep(1)
        pyautogui.click(612,397)
    else:
        speak("what should i do sir")
def shutdown():
    speak("yes sir saving states of all program")
    confirm= " state of all program is saved , sir ! surely  you want to shutdown the computer"
    speak(confirm)
    confirm_for_shutdown = takecommand()
    if confirm_for_shutdown=='yes':
        os.system("shutdown /s /t 1")
    else:
        exit()
def restart():
    speak("yes sir! saving states of all program")
    confirmr= " state of all program is saved , sir ! surely youwant to restart  the computer"
    speak(confirmr)
    confirm_for_restart=takecommand()
    if confirm_for_restart=='yes':
        os.system("shutdown /r /t 1")
    else:
        exit()
if __name__=="__main__":
    #speak("Mr. Hariom is good boy")
    wiseme()
    while True:#for infinte time
    #if 1:# for 1 time only
        query = takecommand().lower()
        #logic task based on query
        # if 'harry' or 'hey harry' in query:
        #     speak('how may I help you sir')
        #     while True:
        #         query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching on wikipedia")
            print("searching on wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            engine.setProperty('rate', 200)
            speak(results)
        elif 'youtube' in query:
            youtube()
        elif 'open google' in query:
            google()
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            break
        # elif 'sms' in query:
        #     sms()
        elif 'check number ' in query or 'number' in query:
            check_phone_number()
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        # elif 'shutdown the computer' in query:
        #     shutdown()
        elif 'restart the computer' in query:
            restart()
        elif ' music' in query:
            music_dir = 'C:\\Users\\Mr. Hariom\\Music'
            music = random.randrange(1, 434)
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[music]))
        elif 'alarm' in query:
            speak("wait setting the alarm")
            alarm()
        elif ' open Harry' in query:
            os.startfile("‪D:\\Harry.py")
        elif 'what can you do' in query:
            do = " i am just at my learning stage so i am trying to learn from you , sir i can open  and search anything on youtube , " \
                 "google ,facebook,send the email , play some music,i can search anything in wikipedia and  for you i set the  alarm sir "
            print(do)
            speak(do)

        elif 'shutdown' in query:
            speak("ok sir wait..")
            pyautogui.hotkey("alt", "f4")
            time.sleep(5)
            pyautogui.moveTo(682, 437)
            speak("shutting down the Harry ")
            time.sleep(2)
            pyautogui.click(682, 437)

        elif 'send email' in query:
            try:
                speak("what should i send in content sir ")
                content = takecommand()
                speak("to whom i sent email")
                to = str(input("enter the email id of receiver sir"))
                # to = takecommand()
                sendEmail(to, content)
                speak("email has  successfully  send ")
            except Exception as e:
                print(e)
                speak("sorry my sir i am not able to send email right now")
        elif 'thank you' in query:
            print('thank you so much')
            speak('thank you so much')
            break

        else:
            print("please say that again sir i didn't understand")
            speak("please say that again sir i didn't understand")
