import webbrowser

from speech import speak

# Load music library from music__datatype (or fallback to test module if present)
try:
    import music__datatype as music_data
except ImportError:
    try:
        import test as music_data
    except ImportError:
        music_data = None


def play_music(song_name: str) -> None:
    music_dict = getattr(music_data, "music", {}) if music_data else {}

    if song_name in music_dict:
        music_url = music_dict[song_name]
        speak(f"Playing {song_name}")
        webbrowser.open(music_url)
    else:
        speak(f"I could not find {song_name} in your music list.")