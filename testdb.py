import json

with open('content.json') as json_file:
    data = json.load(json_file)
    for p in data['subject_marker']:
        print(p)