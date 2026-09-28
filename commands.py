"""
commands.py

Handles detection and execution of built-in JARVIS commands:
- Web commands (Google, YouTube)
- Music playback commands (play <song>)
- System commands (current time, exit/quit/stop)

Queries that are not built-in commands are routed through responses/response_handler.py.
"""

from datetime import datetime
import webbrowser

from speech import speak
from music import play_music
from responses.response_handler import generate_response


# =====================================================================
# COMMAND DETECTION
# =====================================================================

def is_command(command: str) -> bool:
    """
    Checks whether the user's spoken input matches an existing built-in command.

    Args:
        command (str): Spoken input from the user (lowercased).

    Returns:
        bool: True if input matches a known command, False otherwise.
    """
    cmd = command.lower().strip()

    # Web commands
    if "open google" in cmd or "open youtube" in cmd:
        return True

    # Music commands
    if cmd.startswith("play "):
        return True

    # Time command
    if "time" in cmd:
        return True

    # Exit / Stop commands
    if "exit" in cmd or "quit" in cmd or "stop" in cmd:
        return True

    return False


# =====================================================================
# COMMAND EXECUTION
# =====================================================================

def execute_command(command: str) -> bool:
    """
    Executes a recognized built-in command.

    Args:
        command (str): Spoken input from the user.

    Returns:
        bool: False if the command was an exit command (signals JARVIS to stop),
              True to continue listening.
    """
    cmd = command.lower().strip()

    # 1. Web Commands - Google
    if "open google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    # 2. Web Commands - YouTube
    if "open youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    # 3. Music Commands
    if cmd.startswith("play "):
        song_name = cmd.replace("play ", "", 1).strip()
        play_music(song_name)
        return True

    # 4. System Commands - Current Time
    if "time" in cmd:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return True

    # 5. System Commands - Exit / Stop
    if "exit" in cmd or "quit" in cmd or "stop" in cmd:
        speak("Goodbye")
        return False

    return True


# =====================================================================
# UNIFIED HANDLER (Backward Compatible)
# =====================================================================

def handle_command(command: str) -> bool:
    """
    Unified entry point for backward compatibility.
    If the command is recognized, it is executed.
    If unrecognized, it delegates response generation to responses/response_handler.py.

    Args:
        command (str): Spoken input from the user.

    Returns:
        bool: False if JARVIS should terminate, True otherwise.
    """
    if is_command(command):
        return execute_command(command)

    # If not a recognized command, route to response_handler
    response = generate_response(command)
    speak(response)
    return True