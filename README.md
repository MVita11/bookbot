## BookBot

BookBot is a Python command-line application that analyzes text files and generates useful statistics about books and other written content.

Built as part of the Boot.dev backend development curriculum, this project helped strengthen my understanding of Python fundamentals, file handling, dictionaries, functions, and data processing.

---

## Features

- Count the total number of words in a text
- Analyze character frequency
- Sort and display character statistics
- Read and process `.txt` book files
- Simple command-line interface

---

## Technologies Used

- Python 3
- Command Line Interface (CLI)

---

## Project Structure

```bash
bookbot/
│
├── main.py
├── stats.py
├── books/
│   └── frankenstein.txt
└── README.md
```

## Installation & Setup

1. Clone the Repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/bookbot.git
   ```

2. Navigate into the Project Folder
   ```bash
   cd bookbot
   ```

3. Run the Application
   ```bash
   python3 main.py
   ```

## Example Output
```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 75767 total words

--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
...
```

## Skills Demonstrated

This project has helped me strengthen my understanding of:
 - Python fundamentals
 - Backend development concepts
 - File reading and processing
 - Dictionaries and sorting algorithms
 - Functional programming principles
 - Writing modular and maintainable code
 - Command-line application development
 - Data analysis basics

## Improvements Added Beyond the Guided Project

To continue developing the project beyond the original tutorial, future improvements may include:
  - User input support for custom book files
  - Exporting analysis results to JSON or CSV
  - Unit and integration testing
  - Web dashboard for visualisation
  - REST API version using Flask or FastAPI
  - Improved error handling and validation

## Acknowledgements

[Boot.dev](https://www.boot.dev/courses/build-bookbot-python) - This project is created as part of the Backend curriculum