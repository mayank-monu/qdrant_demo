# Import client library
from qdrant_client import QdrantClient
from qdrant_client import models

qdrant_client = QdrantClient(host='localhost', port=6333)

qdrant_client.recreate_collection(
  collection_name='genAI',
  vectors_config=models.VectorParams(size=768, distance="Cosine")
)