# from qdrant_client import QdrantClient
# from app.core.config import settings

# qdrant_client = QdrantClient(
#     host=settings.qdrant_host,
#     port=settings.qdrant_port,
# )
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://6b24ab4a-19c4-4b0f-a49a-dae14c989412.eu-central-1-0.aws.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.gdcq72AhajStXQmYd9Gcn4MdN-Y7VI2OckKe8i_f_Hg",
)

# print(qdrant_client.get_collections())