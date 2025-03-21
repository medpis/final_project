import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the Emotions analysis service
    url = https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the Emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the Emotions analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Return the text attribute of the response response object as received from the Emotion Detection function.
    return(response.text)

