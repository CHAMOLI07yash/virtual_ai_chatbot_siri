# Voice Assistant using Python

This is a simple voice assistant script written in Python that interacts with the user through speech recognition and text-to-speech capabilities. The assistant is activated by saying "Alexa" and can perform various tasks like playing songs on YouTube, telling the time, retrieving information from Wikipedia, cracking jokes, and more.

## Dependencies

Make sure you have the following Python libraries installed:

- speech_recognition
- pyttsx3
- pywhatkit
- datetime
- wikipedia
- pyjokes

You can install them using the following command:

```bash
pip install speech_recognition pyttsx3 pywhatkit wikipedia pyjokes
```

## Usage

1. Run the `voice_assistant.py` script using your Python interpreter.

2. Once the script is running, say "Alexa" to activate the assistant.

3. Issue commands following the activation keyword "Alexa."

## Functionality

- **Playing Songs**: You can ask the assistant to play a song by saying "play \<song name\>."

- **Time**: The assistant can tell you the current time. Just say "What's the time?"

- **Wikipedia**: You can ask the assistant about a person by saying "Who the heck is \<person name\>?" It will provide a brief summary using Wikipedia.

- **Relationship Status**: Try asking the assistant if it's in a relationship to get some humorous responses.

- **Jokes**: Ask the assistant for a joke, and it will tell you a random joke using the pyjokes library.

- **Default Response**: If the assistant doesn't recognize your command, it will ask you to repeat the command.

## Note

- Make sure your microphone is connected and properly set up to ensure accurate speech recognition.

- The assistant listens for the activation keyword "Alexa." You can modify this keyword in the `take_command()` function.

- The script is designed to run indefinitely (`while True:`) to continuously listen for commands. You can stop the script manually.

- The assistant's voice can be modified by changing the `voices` property in the `setProperty()` function of the `pyttsx3` library.

---

Feel free to customize and expand the functionality of this voice assistant as needed. If you have any questions or suggestions, feel free to reach out!
