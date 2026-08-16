# NLP Text Analyzer

A Tkinter desktop app with login/register that lets users run basic NLP tasks on text: Named Entity Recognition, Sentiment Analysis, and Language Detection.

## Features

- Login/Register (stored locally in `data.json`)
- **NER** — powered by GLiNER (`urchade/gliner_base`), search for a specific entity type in your text
- **Sentiment Analysis** — powered by VADER, classifies text as Positive/Negative/Neutral
- **Language Detection** — powered by `langdetect`

## What can it do ?

- **Named Entity Recognition (NER)**
  - Detects entities from a given sentence.
  - For example, it can identify things such as names, locations, organizations, etc.

- **Language Detection**
  - Detects the language of the entered text.
  - Supports languages such as English, French, Spanish, German, Hindi, Japanese, Chinese, and more.

- **Sentiment Analysis**
  - Determines whether the given text is:
    - Positive
    - Negative
    - Neutral

## Setup

```
pip install -r requirements.txt
python app.py
```

Make sure `images/favicon.ico` exists in the project folder (used as the window icon).

## Files

- `app.py` — main GUI app
- `my_db.py` — handles login/register, reads & writes `data.json`
- `data.json` — local storage for user accounts

## Note

`data.json` is a simple local file, not a real database — passwords are stored in plain text, so this is for practice/demo purposes only.

## Author

Sanskar Lupane — [GitHub](https://github.com/lupanesanskar)
