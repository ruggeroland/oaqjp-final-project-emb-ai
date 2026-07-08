"""Unit tests for the emotion detection application."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion detector."""

    def test_emotion_detector(self):
        """Test dominant emotions for known input sentences."""
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy",
        )
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger",
        )
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")[
                "dominant_emotion"
            ],
            "disgust",
        )
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"],
            "sadness",
        )
        self.assertEqual(
            emotion_detector("I am afraid that this will happen")[
                "dominant_emotion"
            ],
            "fear",
        )


if __name__ == "__main__":
    unittest.main()
