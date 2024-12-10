import speech_recognition as sr
import pyttsx3
import pywhatkit   
import datetime  
import wikipedia  
import webbrowser  #for opening applications
import randfacts  
import random
import subprocess  #for note-making
import requests    #for weather details


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def talk(text):
#Primary Function that makes our bot to talk
   engine.say(text)
   engine.runAndWait()


for i in range(1):
    def wishME():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            talk('Good Morning')
        if hour>=12 and hour<18:
            talk('Good Afternoon')
        else:
            talk('Good evening')
        talk('I am Zira,  how may I help you Sir?')
    wishME()


def take_command():
#it takes mic input and gives string output.
    try:
        with sr.Microphone() as source:
            listener = sr.Recognizer()
            listener.energy_threshold = 8000
            listener.adjust_for_ambient_noise(source, 1)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'zira' in command:
                command = command.replace('zira','')
                print(command)
    except sr.UnknownValueError:
        pass
    return command


def say_hello(text):
#it will greet back to us
    greet = ["hi", "hello", "hey there"]
    responses = ["hi ", "hello", "what's up", "hey. there", "greetings!"]
    if text in greet:
        b = random.choice(responses) 
        print(b)
        talk(b)


def calculate():
#for calculation purpose
    u = "please select any of the following operation you want to perform: "
    talk(u)
    operation = input(u +  '+ , - , * , / , **')
    talk("enter first number")
    num1 = int(input('Enter first no. '))
    talk("enter second number")
    num2 = int(input('Enter second no. '))
    
    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
        talk(num1 + num2)
    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)
        talk(num1 - num2)
    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
        talk(num1 * num2)
    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)
        talk(num1 / num2)
    elif operation == '**':
        print('{} ** {} = '.format(num1, num2))
        print(num1 ** num2)
        talk(num1 ** num2)
    else:
        print("Sorry, Operation not available")
        talk("Sorry, Operation not available")


def note(text):
#used for adding something on a note 
    date = datetime.datetime.now()
    filename = str(date).replace(":","-") + "-note.txt"
    with open(filename,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", filename])  


#weather details from an external API
key = 'dd75d3d51242e459cb1b7f92b7b1c363'
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=' + key
json_data = requests.get(api_address).json()
def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description = json_data["weather"][0]["description"]
    return description


def run_zira():
    command = take_command()
    print(command)
    if 'introduce' in command:
        a ='Hello, my name is Zira. This Project is a Virtual Voice Assistant, made by using python.'
        print(a)
        talk(a)

    elif 'name' in command:
        intro = 'I am Zira, your Virtual Voice Assistant'
        print(intro)
        talk(intro)

    elif 'how are you' in command:
        talk('i am fine......,   how about you')

    elif 'hello' in command:
        say_hello(command)   #func called at line 61

    elif 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
        print(time)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk(date)
        print("Today's date is: ",date)

    elif 'temperature' in command or 'weather' in command:
        talk("temperature in new delhi is " + str(temp()) + "degrees celsius" + "and with" +str(des()))
        print(temp()+'*C')
        print(des())

    elif 'calculate' in command or 'calculation' in command:
        calculate()  #func called at line 71

    elif 'what is' in command:
        search_wiki = command.replace('what is','')
        info = wikipedia.summary(search_wiki,1)
        talk('According to Wikipedia')
        print(info)
        talk(info)

    elif 'fact' in command:
        x = randfacts.get_fact()
        print(x)
        talk("did you know that, " + x)   

    elif 'note' in command:
        talk("sure,  what would you like me to write down?")
        note_text = take_command()
        note(note_text)           #func called at line 107
        talk("i have made the note successfully")

    elif 'thank you' in command:
        thank_u_list = ['always welcome', 'you are welcome', 'any time']
        thanking = random.choice(thank_u_list)        
        talk(thanking)

    elif 'open YouTube' in command:
        talk("opening")
        webbrowser.open("youtube.com") 

    elif 'open Google' in command:
        talk("opening")
        webbrowser.open("google.com")

    else:
         talk("sorry.... i could not answer your query, please try other commands")


run_zira()