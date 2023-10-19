import os
from gtts import gTTS
from pydub import AudioSegment
import time

# Constants
SILENCE_DURATION = 2000
INTERVAL_PER_EXTRA_CHAR = 1000

def text_to_audio(phrase):
    """
    Convert given phrase to an audio file and return the filename.
    
    Args:
        phrase (str): Text to convert to audio.
        
    Returns:
        str: Filename of the generated audio.
    """
    tts = gTTS(phrase, lang="en")
    filename = f"{phrase[:10]}_{time.time()}.mp3"
    tts.save(filename)
    return filename

def main(input_txt, output_audio):
    """
    Convert phrases in input_txt to audio and concatenate them.
    
    Args:
        input_txt (str): Path to the input text file.
        output_audio (str): Path to the output audio file.
    """
    concatenated_audio = AudioSegment.empty()
    
    with open(input_txt, 'r') as f:
        for line in f:
            phrase = line.strip()
            if not phrase:
                continue

            audio_filename = text_to_audio(phrase)
            audio_segment = AudioSegment.from_mp3(audio_filename)

            extra_interval = max(0, len(phrase) - 3) * INTERVAL_PER_EXTRA_CHAR

            for _ in range(3):  # Repeat 3 times
                concatenated_audio += audio_segment
                concatenated_audio += AudioSegment.silent(duration=SILENCE_DURATION + extra_interval)

            os.remove(audio_filename)

    concatenated_audio.export(output_audio, format="mp3")

if __name__ == "__main__":
    main("input.txt", "final_output_audio.mp3")
