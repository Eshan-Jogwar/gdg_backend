import json
import os
path = os.path.abspath(os.path.dirname("topics1.json")) + "/gdg_backend/topics1.json"
#/home/shrihari_006/programming/Ai_study_Buddy/gdg_backend
def fetchTopics():
    file = open(path, "r")
    result = json.load(file)
    file.close()
    return result