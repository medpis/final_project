from SentimentAnalysis.sentiment_analysis import  sentiment_analyzer
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case if joy is the  dominant emotion
        result_1 = sentiment_analyzer('I am glad this happened')
        print(result_1)
        self.assertEqual(result_1['Dominant_emotion'], 'joy')
    
        # Test case if joy is the  dominant emotion
        result_1 = sentiment_analyzer('I am glad this happened')
        print(result_2)
        self.assertEqual(result_1['Dominant_emotion'], 'joy')
    
        # Test case if joy is the  dominant emotion
        result_1 = sentiment_analyzer('I am glad this happened')
        print(result_1)
        self.assertEqual(result_1['Dominant_emotion'], 'joy')

        # Test case if joy is the  dominant emotion
        result_1 = sentiment_analyzer('I am glad this happened')
        print(result_1)
        self.assertEqual(result_1['Dominant_emotion'], 'joy')

if __name__ == "__main__":
    unittest.main()