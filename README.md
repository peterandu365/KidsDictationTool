# KidsDictationTool

A specialized tool designed to aid kids' learning through auditory dictation. It takes phrases from a text file and converts them to concatenated dictation audio.

## Description

In the journey of language learning for kids, auditory dictation can play a pivotal role. The `KidsDictationTool` facilitates this by taking a list of phrases separated by new lines in a text file. Each phrase is then converted into an audio snippet using Google Text-to-Speech.

**Changes in the new version:**
- The pause interval between phrases has been increased to 3 seconds.
- The extra interval added for each character beyond the initial three in a phrase has been reduced to half a second.
- The generated audio filenames now have the first alphabetical character of the phrase as a prefix, providing more context to the generated files.
- The script now supports processing a specific text file passed as an argument. If no specific file is passed, it processes all `.txt` files in the directory, creating an audio file for each.

To ensure repetition and retention, each phrase is reiterated three times. The first two repetitions are followed by a 3-second pause, while the third repetition is followed by a pause that considers the length of the phrase.

## Requirements

- Python 3
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [pydub](https://pypi.org/project/pydub/)
- FFmpeg (for pydub)

## Installation

1. Install the required packages:
```bash
pip install gtts pydub
```
2. Ensure FFmpeg is installed on your system. For macOS, you can use Homebrew:
```bash
brew install ffmpeg
```

## Usage

1. Tailor your dictation content. If you have a specific text file, pass it as an argument:
```bash
python3 KidsDictationTool.py your_file.txt
```
Otherwise, the script will process all `.txt` files in the current directory.

2. The resulting dictation audio will be saved with the same name as the text file but with an `.mp3` extension. Let your kids listen and write!

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, Kids Dictation Tool, https://github.com/peterandu365/KidsDictationTool, 2023
```

## License

MIT License. See [LICENSE](LICENSE) for more details.