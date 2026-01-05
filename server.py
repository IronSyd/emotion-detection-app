"""
Flask server for the EmotionDetection package.

Exposes an HTTP endpoint that accepts input text and returns emotion scores
and the dominant emotion in a human-readable format.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)

INVALID_TEXT_MSG = "Invalid text! Please try again!"
HOME_MSG = "Emotion Detection service is running. Use /emotionDetector?textToAnalyze=..."


@APP.route("/", methods=["GET"])
def home():
    """Health-check endpoint to confirm the server is running."""
    return HOME_MSG


# The project requires this exact route and function name.
# pylint: disable=invalid-name
@APP.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    """Analyze text from the query string and return a formatted emotion response."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return INVALID_TEXT_MSG

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


def main():
    """Run the Flask development server on localhost:5000."""
    APP.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
