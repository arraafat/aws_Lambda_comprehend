import os, boto3


escalation_intent_name = os.getenv('ESCALATION_INTENT_NAME', None)

client = boto3.client('comprehend')

def lambda_handler(event, context):
    entities=client.detect_pii_entities(Text=event['inputTranscript'],LanguageCode='en')
    dict_pairs = entities.items()
    pairs_iterator = iter(dict_pairs)
    first_pair = next(pairs_iterator)
    Entities =first_pair[1]
    index = 0
    detected_Entitie= []
    while index < len(Entities):
        item =Entities[index]['Type']
        #print(item)
        detected_Entitie.append(item)
        index += 1
    #print (detected_Entitie)
    index2 = 0
    inputTranscript_detected_list= []
    while index2 < len(Entities):
        BeginOffset=Entities[index2]['BeginOffset']
        EndOffset =Entities[index2]['EndOffset']
        inputTranscript_detected = Text=event['inputTranscript'] [BeginOffset:EndOffset]
        inputTranscript_detected_list.append(inputTranscript_detected)
        index2 += 1
    #print (inputTranscript_detected_list)
    detected_Entitie_dict= dict(zip(detected_Entitie,inputTranscript_detected_list ))
    print (detected_Entitie_dict)
    return(Entities)
    
    
    




