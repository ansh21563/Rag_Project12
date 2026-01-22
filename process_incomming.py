import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import requests
from openai import OpenAI
from config import api_key

client = OpenAI(api_key=api_key)
# from read_chunks import create_embedding


def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model": "bge-m3",
        "input":text_list
    })      

    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate",json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })     

    response = r.json()
    print(response)
    return response

def inference_openai(prompt):
    print("Thinking....")
    response = client.responses.create(
    model="gpt-4.1",
    input=prompt    
    )
    
    return response.output_text


df = joblib.load('embeddings.joblib')

incoming_query =  input(" Ask a question: ")
question_embedding = create_embedding([incoming_query])[0] 
# print(question_embedding)
# print(my_dicts)
# a = create_embedding("cat sat on the mat")
# print(a)


# find similarities of question_embedding with other embeddings
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding'].shape))
similarities = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
# print(similarities)
top_results = 3
max_indx = similarities.argsort()[::-1][0:top_results]
print(max_indx)
new_df = df.loc[max_indx]
# print(similarities.argsort()) 
# print(new_df[["title","number","text"]])

prompt = f''' This course is about the  machine learning for the health care which is conducted my the MIT professors.Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text" ]].to_json(orient="records")}
----------------------------------------
{incoming_query}
User asked this question related to the video chunks, you have to answer where and how much content is taught in which video (in which video and what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

# response = inference(prompt)["response"]
# print(response)

response = inference_openai(prompt)
print(response)

with open("response.txt","w",encoding="utf-8") as f:
    f.write(response)

# for index, item in new_df.iterrows():
#     print(index,item["title"],item["number"],item["text"],item["start"],item["end"])            