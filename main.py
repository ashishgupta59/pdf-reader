import pyttsx3
speaker = pyttsx3.init()
text = input("enter text")
speaker.say(text)
speaker.runAndWait()