from langchain_community.document_loaders import PyPDFLoader
from qdrant_client import QuadrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, StrictFloat
import asyncio

async def read():
    file_path = ( "./instruction_yaris.pdf" )

    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    print(len(pages))

    for page in pages:
        print(f"{page.metadata}\n")
        #print(page.page_content)


asyncio.run(read())