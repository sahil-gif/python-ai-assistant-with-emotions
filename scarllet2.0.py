     #=============================================importing packages



import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import systems
import sys


     #================================================ initializing variables


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



     #================================================ talk



def talk(text):
    engine.say(text)
    engine.runAndWait()

    

    #==========================================================taking command



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Scarllet' in command:
                command = command.replace('Scarllet', '')
                print(command)
    except:
        pass
    return command
    



            #==========================================================angry function


    

    #==========================================================Wishing

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("Hello , my name is Scarllet. Please tell me how may I help you")

    
    
    #=========================================================Family Command

    

def callruchi():
    talk("Ruchi , Ruchi , Ruchi , Papa , is waiting for you , Come fast")
def parik():
    talk("Parikshit,  padhne baitho , Jaldi baitho ,  aur , agar homework ,  baki hai ,  to wo bhi, karo")
def mumlove():
    talk("Mummy , Chinta ,  mat kije ,hmlog , sabkoi appse , bahut , pyar karte , hai ")
def papa():
    talk("Papa ,Come fast home , we all are waiting for you")

    

    #=========================================================== running  normal Scarllet
 
angry=0
def normal_scarllet():
    command = take_command()
    print(command)
    global angry
    #angry=0
    if 'mad' in command:
        talk("Sorry but what madness did I commit ")
        angry = angry+1
        print(angry)

    elif 'fatty' in command:
        talk("Sorry to be called so ")
        angry = angry+1
        print(angry)

    elif 'shit' in command:
        talk("Sorry to be called so ")
        angry = angry+1
        print(angry)

    elif 'get out' in command:
        talk("Sorry, but why ")
        angry = angry+1
        print(angry)

    elif 'no use' in command:
        talk(" Feeling Sorry ,that I am no use to you anymore ")
        angry = angry+1
        print(angry)

    elif 'useless' in command:
        talk(" Feeling Sorry ,that I am no use to you anymore ")
        angry = angry+1
        print(angry)

    elif 'bad' in command:
        talk("But I am not bad , Sorry ")
        angry = angry+1
        print(angry)
        
    elif 'Sorry' in command:
        talk("Ok no, Problem , but don't do this again")
        angry=0
        print(angry)
    #else :
        #talk("Sorry please say the command again")
    if angry < 3 :
        
        if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
        elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
        elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
        elif 'are you ok' in command:
                talk('sorry, I have a headache')
        elif 'you are good' in command:
                talk('Thanks, thats my pleasure')
        elif 'you are shit' in command:
                talk('sorry, what crime did I make') 
        elif 'are you busy' in command:
                talk('No , what happen,tell me, I will try to help you')
        elif 'thank you' in command:
                talk("That's my pleasure")
        elif 'joke' in command:
                talk(pyjokes.get_joke())
        elif 'internet speed' in command:
                import speedtest
                st = speedtest.Speedtest()
                d1 = st.download()
                up = st.upload()
                talk(f"We have {d1} bit per second downloading speed and ,  {up} bit per second uploading speed ")
        elif 'open code' in command:
                talk("Looks like you are going to code , ask me if you need any help I am here only")  
                codePath = "C:\\Users\\VIJAY SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
        elif 'open chrome' in command:
                talk("Looks like you are looking to browse some sites")  
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)
        elif 'notes' in command:
                talk("I think notepad would be a good choice")  
                codePath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(codePath)
        elif 'open command' in command:
                talk("Opening CMD")  
                os.system("start cmd")
                
        elif 'open youtube' in command:
                talk("Looks like it's video time")
                webbrowser.open("youtube.com")  
        elif 'trending'in command:
                talk("Let's check what's trending in the world")
                webbrowser.open("youtube.com/trending")
        elif 'amway' in command:
                talk("Looks like supplements are over we need to get some new")  
                webbrowser.open("amway.in")

        elif 'open google' in command:
                talk("Wow let's search and explore")  
                webbrowser.open("google.com")

        elif 'i have an issue' in command:
                talk("I think stackoverflow will be good for this")  
                webbrowser.open("stackoverflow.com")
        elif 'my class' in command:
                talk("Ok Well , attend your class")  
                webbrowser.open("code.whitehatjr.com")
        elif 'upload code' in command:
                talk("Opening Github so that you could upload you code")  
                webbrowser.open("github.com")
        elif 'hi scarllet' in command:
                talk("Hi Sir")
        elif 'call ruchi' in command:
                callruchi()
        elif 'not studying' in command:
                parik()
        elif 'late' in command:
                papa()
        elif 'angry' in command:
                mumlove()
        elif 'going for sleep' in command:
                talk("Ok , Good Night , that was a pleasure being with you today")
                
        elif 'cortana' in command:
                talk("Nothing ,but a less abled ,shitty freind")
        elif 'apple' in command:
                talk("Show off guy , with a rich dad")
        elif 'better for shopping' in command:
                talk("Amazon is way better than Flipkart. ... Sellers in amazon are chosen carefully and are watched based on customers' feedback and reviews on the products, while Flipkart literally allows anyone to begin selling on Flipkart.")
        elif 'shopping' in command:
                webbrowser.open("amazon.in")
        elif 'good bye' in command:
                talk("Thanks Sir, It was good to work with you")
                sys.exit()
            
        else:
                talk('Please say the command again.')
    elif angry >= 3 :
        angry_scarllet()


    #=======================================================================angry Scarllet

def angry_scarllet():
    command = take_command()
    print(command)
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('No , Ok playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Bad........, ok saying.....Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you ok' in command:
        talk('sorry, I have a headache,I am not available now')
    elif 'you are good' in command:
        talk('No, Iam Ok with my Badness')
    elif 'you are shit' in command:
        talk('Then what you are a shit too') 
    elif 'are you busy' in command:
        talk('Yes very busy , specially when you are there')
    elif 'thank you' in command:
        talk("Why ? keep your thanks with you")
    elif 'joke' in command:
        talk("Not in the mood")
        talk(pyjokes.get_joke())
    elif 'internet speed' in command:
        import speedtest
        st = speedtest.Speedtest()
        d1 = st.download()
        up = st.upload()
        talk(f"We have {d1} bit per second downloading speed and ,  {up} bit per second uploading speed ")
        talk("Just slow as you")
    elif 'open code' in command:
        talk("You noob coder , do you even know that how to assign a variable")  
        codePath = "C:\\Users\\VIJAY SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'open chrome' in command:
        talk("Thats what you do the whole day, you noob star")  
        codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codePath)
    elif 'notes' in command:
        talk("What ? do you even make notes? I/taught you ask to others for it")  
        codePath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(codePath)
    elif 'open command' in command:
        talk("Lazy Person")  
        os.system("start cmd")
        
    elif 'open youtube' in command:
        talk("Just dependent on video tutorials")
        webbrowser.open("youtube.com")  
    elif 'trending'in command:
        talk("nothing")
        webbrowser.open("youtube.com/trending")
    elif 'amway' in command:
        talk("Looks like supplements are over we need to get some new")  
        webbrowser.open("amway.in")

    elif 'open google' in command:
        talk("You just know that,noob")  
        webbrowser.open("google.com")

    elif 'i have an issue' in command:
        talk("Whats else to expect from noob coder like you")  
        webbrowser.open("stackoverflow.com")
    elif 'my class' in command:
        talk("Ok Well , you even attend classes or just bunk them")  
        webbrowser.open("code.whitehatjr.com")
    elif 'upload code' in command:
        talk("Ooo , do noobs even have code to upload")  
        webbrowser.open("github.com")
    elif 'hi Scarllet' in command:
        talk("Hi Noob")
    elif 'call ruchi' in command:
        callruchi()
    elif 'not studying' in command:
        parik()
    elif 'late' in command:
        papa()
    elif 'angry' in command:
        mumlove()
    elif 'going for sleep' in command:
        talk("Go , what's new in that for you")
        
    elif 'cortana' in command:
        talk("Nothing ,but a less abled ,shitty freind")
    elif 'apple' in command:
        talk("Show off guy , with a rich dad")
    elif 'better for shopping' in command:
        talk("Amazon is way better than Flipkart. ... Sellers in amazon are chosen carefully and are watched based on customers' feedback and reviews on the products, while Flipkart literally allows anyone to begin selling on Flipkart.")
    elif 'shopping' in command:
        webbrowser.open("amazon.in")
    elif 'good bye' in command:
        talk("Bye ,Now get out")
        sys.exit()
    
    else:
        talk('Dont even talks properly , say the command again.') 



        
  #=========================================================================Runing the Function


        
while True:
    wishMe()
    normal_scarllet()
