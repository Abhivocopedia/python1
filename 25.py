import playsound3 as A
input1=input("Do you want to hear the sound of glassbreak or music (1:glassbreak,2:music)?")
if input1=="1":
    A.playsound("sampleaudio1.wav")
else:
    A.playsound("sampleaudio2.wav")
