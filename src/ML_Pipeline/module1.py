import json
JSON_File_Path="C:/Users/aiswa/OneDrive/Data Science/ProjectPro/NLP Project to build Resume Parser using SpaCy/Resume+Parsing/env/input/training/Entity Recognition in Resumes.json"
def convert_data_to_SPacy2(JSON_File_Path):
    try:
        training_data=[]
        lines=[]
    
        with open(JSONFilePath,"r",encoding='utf-8') as f:
            lines=f.readlines()
        
        for line in lines:
            data= json.load(line)
            text= data["Content"]
            entities=[]
            for annotation in data["annotation"]:
                point= annotation["points"]
                label= annotation["labels"]
                if not isinstance(labels, list):
                    labels = [labels]

            for label in labels:
                    
                    entities.append((point['start'], point['end'] + 1 ,label))
        
            training_data.append((text, {"entities" : entities}))

        return training_data
    except Exception as e: # in case of exception print-
        logging.exception("Unable to process " + JSON_FilePath + "\n" + "error = " + str(e))
        return None