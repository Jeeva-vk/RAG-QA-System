import faiss
import numpy as np

class Retriever:

    def __init__(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            np.array(embeddings)
        )

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        distances, indices = self.index.search(
            np.array(query_embedding),
            top_k
        )

        return indices[0]