import pyttsx3       #install using pip install pyttsx3
import datetime      #built in module
import speech_recognition as sr   #this module converts spoken words in text.
import wikipedia
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')      #sapi5 provides voices
voices = engine.getProperty('voices')       #this will give the details of the voices.
# print(voices)    #after you run this it will tell you that there are 2 voices in your computer. 
engine.setProperty('voice', 'voices[0].id')     #changing index will change the voice. 0 for male and 1 for female.
print(voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 190)

#its better if we write all thi s inside a function
def speak(audio):       # speak is the function name and audio is taken as an argument. 
    engine.say(audio)              
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning dhruvil sir ")

    elif hour>=12 and hour<18:
        speak("good afternoon dhruvil sir ")
    
    else:
        speak("good evening dhruvil sir")

    speak("I am scully your personal assisstant. What can I do for you?")

def takecommand():                    #this function is taking audio form the microphone and converting it into n string
    """It takes microphone input from the user and return string output"""
    r = sr.Recognizer()      #recognizer class will help to recognize voice
    with sr.Microphone() as source:            # use the default microphone as the audio source
        print("sir I am listening...")
        r.pause_threshold = 1                   #ctrl +click on pt to kno more about it.
        audio = r.listen(source)                #ctrl +click on listen to kno more about it.    

    try:
        print("Decoding..")
        query = r.recognize_google(audio, language='en-in')             #uses google engine. click on it to know more
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)        comment out beacuse if error comes it will print the error.              

       print("Can you please say that again..")
       return "None"                        #none is the string here.
    return query




if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
    
        #logic for executing task based on some query
        if 'wikipedia' in query:
            speak("On it sir..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak( results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is...")
            speak(strtime)
            print(strtime)

        elif 'tell me about yourself' in query:
            speak("I am Norm scully. People get confused between my wife's name and dog's name. Also I am regarded as a medical marvel as a reference to my medical problems. ")
  

    


            
# engine.say("shiv is a boy")     
# engine.runAndWait()   #or you can also write this         




