import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import requests
# from read_chunks import create_embedding


def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model": "bge-m3",
        "input":text_list
    })      

    embedding = r.json()['embeddings']
    return embedding

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


for index, item in new_df.iterrows():
    print(index,item["title"],item["number"],item["text"],item["start"],item["end"])            