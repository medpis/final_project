import requests  # Import the requests library to handle HTTP requests
import json # data formating
 # This function submit user text to API for emotion analysis and return a text.
def emotion_detector(text_to_analyze):

    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    input_json_obj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json_obj, headers=header)
    
    # format the response text
    formatted_response = json.loads(response.text)

    dicofull = formatted_response['emotionPredictions']
    
    print (dicofull)


    # Return the text attribute of the reponse
    return (formated_response)
    