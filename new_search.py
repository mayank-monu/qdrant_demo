from qdrant_client import QdrantClient
from time import time
from sentence_transformers import SentenceTransformer
from pprint import pprint

input = 'How long will a caregiver have access to my online account information?'

model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens', device='cpu')  # https://www.sbert.net/docs/pretrained_models.html
#vector = model.encode(input)


client = QdrantClient(host='localhost', port=6333)



def search(text: str):
        # Convert text query into vector
        vector = model.encode(text).tolist()
        start = time()
        # Use `vector` for search for closest vectors in the collection
        search_result = client.search(
            collection_name='genAI',
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            limit=1 # 5 the most closest results is enough
        )
        t = time() - start
        payloads = [hit.payload for hit in search_result]
        return payloads,t

def send_result(text):
    result,time = search(text)
    return result[0]['completion'],time 


        