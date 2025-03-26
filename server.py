''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def emot_detector():
    ''' Analyse user statment using watdson API '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyse user statement and get emotion set in the requiered format
    emotion_set = emotion_detector(text_to_analyze)
    # case of server 400
    if emotion_set['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    # remove "{ and }" from displayed text
    emotion_set_text = str(emotion_set)[1:-1]
    txt1 = "For the given statement, the system response is {}. The dominant emotion is {}."
    return txt1.format(emotion_set_text, emotion_set['dominant_emotion'])
@app.route("/")
def render_index_page():
    ''' display page template for user imput ''' 
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
