import requests
import os
import json

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model": "bge-m3",
        "input":text_list
    })

    embedding = r.json()['embeddings']
    return embedding




jsons = os.listdir("jsons") # List all the jsons 
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content = json.load(f)
    embediings = create_embedding([c['text'] for c in content ['chunks']])    
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embeddings'] = (chunk['text'])
        chunk_id += 1
        my_dicts.append(chunk)
        print(chunk)   
    break

print(my_dicts)
# a = create_embedding("cat sat on the mat")
# print(a)
