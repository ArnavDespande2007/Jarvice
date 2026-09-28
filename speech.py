import pyttsx3
import speech_recognition as sr


def create_speech_engine():
    try:
        speech_engine = pyttsx3.init("sapi5")
        speech_engine.setProperty("rate", 175)
        speech_engine.setProperty("volume", 1.0)

        voices = speech_engine.getProperty("voices")

        if voices:
            speech_engine.setProperty("voice", voices[0].id)

        return speech_engine

    except Exception as error:
        print(f"Text-to-speech could not start: {error}")
        return None


engine = create_speech_engine()
recognizer = sr.Recognizer()






def speak(text):
    try:
        if engine:
            engine.say(text)
            engine.runAndWait()

    except Exception as error:
        print("Voice error:", error)
        print("JARVIS:", text)


def listen(prompt="Listening..."):
    try:

        with sr.Microphone() as source:

            print(prompt)

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio).lower()

        print(f"You said: {command}")

        return command

    except sr.WaitTimeoutError:
        print("No speech was detected.")

    except sr.UnknownValueError:
        print("I could not understand that.")

    except sr.RequestError as error:
        print(f"Speech recognition service error: {error}")

    except OSError as error:
        print(f"Microphone error: {error}")

    return None