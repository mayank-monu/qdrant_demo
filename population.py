import numpy as np
import json
from qdrant_client import QdrantClient

fd = open('./anthem_json/depr.json')
qdrant_client = QdrantClient(host='localhost', port=6333)

# payload is now an iterator over startup data
payload = map(json.loads, fd)

# Here we load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if we don't want to load all data into RAM
vectors = np.load('./anthem_json/vectors.npy')

# And the final step - data uploading
qdrant_client.upload_collection(
  collection_name='genAI',
  vectors=vectors,
  payload=payload,
  ids=None,  # Vector ids will be assigned automatically
  batch_size=256  # How many vectors will be uploaded in a single request?
)
