# qdrant_demo
## Steps to run the app

1. Install Docker
2. Run the following commands in your directory where code is saved
  1. docker pull qdrant/qdrant
  2. docker run -p 6333:6333 \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  qdrant/qdrant
  3. python qdrant_instantiate.py
  4. python population.py
  5. streamlit run stlit.py
