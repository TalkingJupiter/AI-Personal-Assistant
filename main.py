import os
import pygame

def speak(text):
    voice  = "es-EN-SteffanNeural"  #Select the voice

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"' #Command to text-to-speach

    os.system(command) #Execute the command

    #Start the pygame
    pygame.init()
    pygame.mixer.init()

    

    try:
        pygame.mixer.music.load('output.mp3') #Load the output
        pygame.mixer.music.play() #Play the output

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

speak("Hello boss! How can I assist you today?")