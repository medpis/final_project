import requests  # Import the requests library to handle HTTP requests
import json # data formating

# This function submit user text to API for emotion analysis and 
# return a dic of couple 'emotion':score .
def emotion_detector(text_to_analyze):

    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    input_json_obj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json_obj, headers=header)
    print("Server status code", response.status_code)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    # Process response NOK
    if (response.status_code == 400):
        emotion_set = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion":None }
    else :
        # Emotion set 
        emotion_set = formatted_response['emotionPredictions'][0]['emotion']
        # Search for the highest score
        high_score = emotion_set['anger'] # assume it's however
        dominant_emotion = 'anger'
        if high_score < emotion_set['disgust']:
                high_score = emotion_set['disgust']
                dominant_emotion = 'disgust'    # disgust has temporarely the highest score
        if high_score < emotion_set['fear']:
                high_score = emotion_set['fear']
                dominant_emotion = 'fear'       # fear has temporarely the highest score
        if high_score < emotion_set['joy']:
                high_score = emotion_set['joy']
                dominant_emotion = 'joy'        # joy has temporarely the highest score
        if high_score < emotion_set['sadness']:
                high_score = emotion_set['sadness']
                dominant_emotion = 'sadness'    # sadness has the highest score
        # add the dominant emotion to the dictionary
        emotion_set["dominant_emotion"] = dominant_emotion        
        
    # Return formated the reponse: none or val
    return (emotion_set)
