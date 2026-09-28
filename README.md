# JARVIS Voice Assistant

A modular Python-based voice assistant built with speech recognition, text-to-speech, and an architecture ready for future AI integration.

---

## Architecture Overview

JARVIS is designed with clean modularity. It maintains fast execution for local built-in commands (web, music, time, exit) while providing a dedicated response pipeline prepared for future AI models (e.g., local LLMs or AI APIs) without cluttering `main.py`.

```text
MegaProject1-JARVIS/
│
├── main.py                     # Main loop (Listen -> Understand -> Check -> Execute -> Respond -> Speak)
├── speech.py                   # Speech recognition (STT) and text-to-speech (TTS)
├── commands.py                 # Command detection and execution (web, music, system)
├── music.py                    # Music player logic
├── music__datatype.py          # Music library dictionary (song URLs)
│
├── responses/                  # Response handling layer
│   ├── __init__.py
│   └── response_handler.py     # Orchestrates responses & bridges to AI handler
│
├── ai/                         # Future AI integration layer
│   ├── __init__.py
│   └── ai_handler.py           # Dedicated placeholder for AI models
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## Interaction Flow

`main.py` follows a clear 6-step loop:

```text
Listen (Microphone / STT)
   ↓
Understand query (Strip wake word & normalize)
   ↓
Check existing commands (is_command)
   ↓
Execute command (execute_command: Web / Music / System)
   ↓
Generate response (generate_response: Fallback or Future AI)
   ↓
Speak response (TTS / pyttsx3)
```

1. **Listen**: Listens for the wake word (`"jarvis"`).
2. **Understand query**: Cleans input. If only `"jarvis"` was spoken, prompts `"Yes?"` and listens for the command.
3. **Check existing commands**: Determines if the query matches a built-in command (`is_command(query)`).
4. **Execute command**: If recognized, runs the appropriate action (Google, YouTube, music, time, exit).
5. **Generate response**: If unrecognized, delegates to `responses/response_handler.py`.
6. **Speak response**: Converts the response to audio via `speech.py`.

---

## Existing Commands

- **Web**:
  - `"open google"`: Opens Google in default web browser.
  - `"open youtube"`: Opens YouTube in default web browser.
- **Music**:
  - `"play <song>"`: Plays song from `music__datatype.py` library.
- **System**:
  - `"time"`: Reports current time.
  - `"exit"` / `"quit"` / `"stop"`: Exits JARVIS.

---

## Future AI Integration

When you are ready to connect an AI model:

1. Open [`ai/ai_handler.py`](file:///D:/WINDOWS%20D/python/MegaProject1-JARVIS/ai/ai_handler.py).
2. Inside `get_ai_response(query)`:
   - Call your chosen AI model or service.
   - Return the generated response string.
3. You do **not** need to touch `main.py`, `speech.py`, or `commands.py`!
   - `responses/response_handler.py` automatically queries `get_ai_response(query)`.
   - If a valid response is returned, JARVIS speaks it.
   - If `None` is returned, JARVIS gracefully falls back to the default message.

---

## Installation & Setup

1. **Activate your Python environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run JARVIS**:
   ```bash
   python main.py
   ```
