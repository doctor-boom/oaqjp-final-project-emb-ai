import unittest

from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        response = emotion_detector(text)['dominant_emotion'][0]
        self.assertEqual(response, 'joy')

    def test_anger(self):
        text = "I am really mad about this"
        response = emotion_detector(text)['dominant_emotion'][0]
        self.assertEqual(response, 'anger')

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        response = emotion_detector(text)['dominant_emotion'][0]
        self.assertEqual(response, 'disgust')

    def test_sadness(self):
        text = "I am so sad about this"
        response = emotion_detector(text)['dominant_emotion'][0]
        self.assertEqual(response, 'sadness')

    def test_fear(self):
        text = "I am really afraid that this will happen"
        response = emotion_detector(text)['dominant_emotion'][0]
        self.assertEqual(response, 'fear')

    
if __name__ == '__main__':
    unittest.main()