from EmotionDetection.emotion_detection import  emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case if joy is the  dominant emotion
        result_1 = emotion_detector('I am glad this happened')
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')
    
        # Test case if joy is the  dominant emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
    
        # Test case if joy is the  dominant emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case if joy is the  dominant emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

if __name__ == "__main__":
    unittest.main()