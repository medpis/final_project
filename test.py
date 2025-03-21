import json

response = '{"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'
#print(response)
#print("\n")
formatted_response = json.loads(response)
#print("\n")
#print(formatted_response)
#print("\n")
emotion_set = formatted_response['emotionPredictions'][0]['emotion']
#print(emotion_set) 

# find the highest score
high_score = emotion_set['anger']
print("hi sc =",high_score)
dominant_emotion = "anger"
#print (emotion_set['disgust'])
if high_score < emotion_set['fear']:
        high_score = emotion_set['fear'] # fear has temporary high score
        dominant_emotion = "fear"



if high_score < emotion_set['disgust']:
        high_score = emotion_set['disgust'] # disgust has temporary high score
        dominant_emotion = 'disgust'
if high_score < emotion_set['fear']:
        high_score = emotion_set['fear'] # fear has temporary high score
        dominant_emotion = 'fear'
if high_score < emotion_set['joy']:
        high_score = emotion_set['joy'] # fear has temporary high score
        dominant_emotion = 'joy'
if high_score < emotion_set['sadness']:
        high_score = emotion_set['sadness'] # fear has temporary high score
        dominant_emotion = 'sadness'

print(emotion_set) 
# add the dominant emotion to the dictionary
emotion_set["dominant_emotion"] = high_score

print(emotion_set) 
print(emotion_set['anger'])

print (emotion_set['disgust'])

print (emotion_set['fear'])

print (emotion_set['joy'])

print (emotion_set['sadness'])
print(dominant_emotion, " is dominant with score = ",high_score )
#print(dico_frep['emotion'])
#print(dico_frep['emotion']['anger'])

#print (frep[0]['emotion']['disgust'])

#print (frep[0]['emotion']['fear'])

#print (frep[0]['emotion']['joy'])

#print (frep[0]['emotion']['sadness'])
