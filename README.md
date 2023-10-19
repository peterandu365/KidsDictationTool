
# KidsDictationTool

A specialized tool designed to aid kids' learning through auditory dictation. It takes phrases from a text file and converts them to concatenated dictation audio.

## Description

In the journey of language learning for kids, auditory dictation can play a pivotal role. The `KidsDictationTool` facilitates this by taking a list of phrases separated by new lines in a text file. Each phrase is then converted into an audio snippet using Google Text-to-Speech. To ensure repetition and retention, each phrase is reiterated three times with a 2-second interval. To maintain kids' attention and give them time to process, the playback interval between phrases is determined by the length of the phrase: for each character beyond the initial three in the phrase, the interval is augmented by one second. All these audio snippets are seamlessly concatenated into a single audio file, making it easy for kids to play and practice.

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

1. Tailor your dictation content and place your phrases in `input.txt`, with each phrase on a new line.
2. Run the script:
```bash
python3 KidsDictationTool.py
```
3. The resulting dictation audio will be saved as `final_output_audio.mp3`. Let your kids listen and write!

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, Kids Dictation Tool, https://github.com/peterandu365/KidsDictationTool, 2023
```

## License

MIT License. See [LICENSE](LICENSE) for more details.
