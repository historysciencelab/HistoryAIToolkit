# Getting Started

## Prerequisites

HistoryAIToolkit is confirmed to work with Python 3.10 and 3.11 on recent versions of Mac OSX and Linux. 

!!! Note "If you are on another version of Python or Windows"

    Please try out the project on your platform and let us know how it goes by [opening an issue](https://github.com/historysciencelab/HistoryAIToolkit/issues).


## For most Python users

As of now the project isn't on PyPI, so you'll have to install it from source. 

1. Fork the project on GitHub
2. Clone it to your computer
3. In your terminal, run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[test]'
```

## For Pyenv users

1. Create a Python virtual environment with Pyenv
2. Activate the virtual environment
3. Clone the project repository and navigate to the project directory
4. Install the project from source in editable mode with test dependencies

```bash
pyenv virtualenv <python_version> <env_name>
pyenv activate <env_name>
pip install -e '.[test]'
```

For example:

```bash
pyenv virtualenv 3.11.4 histkit-env
pyenv activate histkit-env
pip install -e '.[test]'
```

## Downloading the data

At minimum you'll need a short audio file to test the code with, which can be:

* Something you record yourself, or
* A snippet of an audio oral history interview such as an mp3 file from https://github.com/historysciencelab/example-oral-history-interviews or
* An audio file from the [Oral History Audio Interviews](https://www.kaggle.com/datasets/audreyfeldroy/oral-history-audio-interviews) dataset on Kaggle, if you want a longer file

### Very Optional: For Advanced Users

Most people won't need to do this, but if you need 1 GB of real oral history interviews, these commands download the entire dataset from Kaggle and put it in the `data` directory:

```
mkdir data
cd data
kaggle datasets download -d oral-history-audio-interviews
```


## Using the CLI

Once you've installed the project, you can run the command-line interface with:

```
(.venv) ❯ hist --help

 Usage: hist [OPTIONS] COMMAND [ARGS]...
╭─ Options ─────────────────────────────────────────────────────────────
│ --install-completion        [bash|zsh|fish|powershell|pwsh]
│ --show-completion           [bash|zsh|fish|powershell|pwsh]
│ --help                      Show this message and exit.
╰───────────────────────────────────────────────────────────────────────
╭─ Commands ────────────────────────────────────────────────────────────
│ generate-questions    Generates questions from a transcript.
│ slice                 Slices an audio file into smaller audio files.
│ transcribe            Transcribes an audio file into text.
│ version               Lists the package version.
╰────────────────────────────────────────────────────────────────────────
```

To transcribe an mp3 file you would type:

```
hist transcribe data/2023-10-06_Mat.mp3 data/
```

Once it's done, the transcript will be saved in data/ with the same name but a `.txt` extension.
