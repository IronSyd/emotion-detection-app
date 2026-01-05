# Emotion Detection Application

A Python-based web application that detects emotions in user-provided text using
**IBM Watson NLP Emotion Detection**. The application exposes a REST API using
**Flask** and returns emotion scores along with the dominant emotion.

---

## Features

- Detects emotions:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Identifies the dominant emotion
- Handles invalid or blank input gracefully
- REST API built with Flask
- Unit tested using `unittest`
- Static code analysis compliant (PyLint 10/10)
- Packaged as a reusable Python module

---
## Project Structure
final_project/
│
├── EmotionDetection/
│ ├── init.py
│ └── emotion_detection.py
│
├── server.py
├── test_emotion_detection.py
├── .gitignore
└── README.md


---

## Installation

### Prerequisites
- Python 3.8+
- pip

### Install dependencies
```bash
pip install flask requests pylint
Running the Application

From the final_project directory:
python3 server.py

The application runs on: http://localhost:5000

API Usage
Endpoint
GET /emotionDetector

Query Parameter
textToAnalyze: Text to analyze for emotions

Example Request: curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20my%20life"

Example Response: For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002,
'fear': 0.009, 'joy': 0.968 and 'sadness': 0.049.
The dominant emotion is joy.

Error Handling

If the input text is blank or invalid, the application responds with: Invalid text! Please try again!

Unit Testing
Run unit tests with: python3 -m unittest test_emotion_detection.py

Static Code Analysis
Run PyLint: pylint server.py

Expected score: 10.00/10

Technologies Used:
- Python
- Flask
- IBM Watson NLP
- Requests
- PyLint
- Git & GitHub

Author
Created by IronSyd
As part of an IBM / Coursera Emotion Detection project.

License
This project is for educational purposes.
