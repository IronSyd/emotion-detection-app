import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertIn("dominant_emotion", result)
                self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
