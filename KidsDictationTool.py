import os
import sys  
from gtts import gTTS
from pydub import AudioSegment
import time

# Constants
SILENCE_DURATION = 3000
INTERVAL_PER_EXTRA_CHAR = 500

def get_first_letter(s):
    """
    Return the first alphabetical character from the string.
    
    Args:
        s (str): The input string.

    Returns:
        str: The first alphabetical character or an empty string if none found.
    """
    for char in s:
        if char.isalpha():
            return char
    return ''

def text_to_audio(phrase):
    """
    Convert given phrase to an audio file and return the filename.
    
    Args:
        phrase (str): Text to convert to audio.
        
    Returns:
        str: Filename of the generated audio.
    """
    first_letter = get_first_letter(phrase)
    filename = f"temp_audio_{first_letter}_{time.time()}.mp3"
    tts = gTTS(phrase, lang="en")
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

            for i in range(3):  # Repeat 3 times
                concatenated_audio += audio_segment
                if i == 2:
                    concatenated_audio += AudioSegment.silent(duration=SILENCE_DURATION + max(0, len(phrase) - 3) * INTERVAL_PER_EXTRA_CHAR)
                else:
                    concatenated_audio += AudioSegment.silent(duration=SILENCE_DURATION)

            os.remove(audio_filename)

    concatenated_audio.export(output_audio, format="mp3")

if __name__ == "__main__":
    # Check if a specific file is passed as an argument
    if len(sys.argv) == 2:
        input_txt_path = sys.argv[1]
        if not input_txt_path.endswith('.txt'):
            print(f"Error: {input_txt_path} is not a .txt file.")
            sys.exit(1)
        
        output_audio_path = os.path.splitext(input_txt_path)[0] + ".mp3"
        main(input_txt_path, output_audio_path)

    # If no specific file is passed, process all .txt files in the directory
    else:
        # Scan current directory for .txt files
        for file in os.listdir("."):
            if file.endswith(".txt"):
                input_txt_path = file
                output_audio_path = os.path.splitext(file)[0] + ".mp3"  # Change extension to .mp3
                main(input_txt_path, output_audio_path)
