End-to-End Video based rag project 


# How to use this RAG AI Teaching assistent on your own data 
## step-1 Collect your videos
Move all your video files to the videos folder

## step-2 Convert to mp3
Convert all the video files to mp3 by running Video_to_mp3

## step-3 Convert mp3 to json
Convert all the video mp3 files to json by running mp3_to_json

## step-4 Convert the json Files to Vectors
Use the File preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## step-5 Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevent prompt as per the user query and feed it to the LLM    

