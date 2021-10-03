#imported python text to speech module 
import pyttsx3


#created variable with name engine and seld intialized pyttsx2 to engine
engine=pyttsx3.init()



#created a function with name speak
#which will simply convert your text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#created user input
user_input=input("Enter something geeks:")

#called speak() function
speak(user_input)
