# AI Email Generator

A lightweight CLI tool that generates professional emails using the Groq API and LLaMA 3.1.

## Features

- Generates complete emails with subject line and body
- Supports multiple tones: `professional`, `friendly`, `urgent`
- Adapts content based on the recipient type (client, boss, team, etc.)
- Powered by `llama-3.1-8b-instant` via Groq for fast generation

## Requirements

- Python 3.7+
- Groq API key — get one free at [console.groq.com](https://console.groq.com)

## Setup

```bash
pip install groq
```

Set your API key:

```powershell
# Windows (PowerShell)
$env:GROQ_API_KEY = "your_groq_api_key"
```

```bash
# Mac/Linux
export GROQ_API_KEY="your_groq_api_key"
```

## Usage

```bash
python email_generator.py
```

You will be prompted for:

| Prompt | Example Input |
|--------|--------------|
| Email topic | `Project deadline update` |
| Tone | `professional` / `friendly` / `urgent` |
| Recipient | `client` / `boss` / `team` |

## Example Output

```
Subject: Project Deadline Update

Hi [Client Name],

I wanted to give you a quick update on the project timeline...
```
