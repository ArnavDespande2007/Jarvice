"""
main.py

Main entry point for the JARVIS voice assistant.
Orchestrates the core interaction loop:
Listen -> Understand query -> Check existing commands -> Execute command -> Generate response -> Speak response
"""

import sys

from speech import speak, listen
from commands import is_command, execute_command
from responses.response_handler import generate_response


def main():
    speak("Initializing Jarvis")
    speak("Jarvis is ready. Say Jarvis, then say your command.")

    while True:
        # 1. Listen for wake word
        wake_input = listen("Waiting for the wake word...")

        if not wake_input or "jarvis" not in wake_input:
            continue

        # 2. Understand query (extract command or prompt if empty)
        query = wake_input.replace("jarvis", "", 1).strip()

        if not query:
            speak("Yes?")
            query = listen("Listening for your command...")

        if not query:
            continue

        # 3. Check existing commands
        if is_command(query):
            # 4. Execute command (Web, Music, System)
            should_continue = execute_command(query)
            if not should_continue:
                break
        else:
            # 5. Generate response (routes to response_handler / future AI)
            response = generate_response(query)

            # 6. Speak response
            speak(response)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJARVIS stopped.")
        sys.exit(0)