# handshaker - Handshake quick apply bot made using Selenium

A script that automatically applies to jobs for me. Web scrapes the BYU Handshake website when you search for any job and applies to all the jobs with quick apply. Written in Python using Selenium.

## Demo Video

[![Demo Video](https://img.youtube.com/vi/34GiNbJ4ECc/0.jpg)](https://youtu.be/34GiNbJ4ECc)

[Watch on YouTube](https://youtu.be/34GiNbJ4ECc)

## Installation

```
touch .env
```

> Make sure to fill `.env` with correct contents (see [`.env.example`](/.env.example)).

## Usage

```
python script.py -q "Web developer"
```

`-q` or `--query` is the flag where you can enter the job you're interested in.
