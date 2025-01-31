from langchain_community.document_loaders import PyPDFLoader
import requests
import asyncio

url = "http://127.0.0.1:8000/document" 

async def read():
    file_path = ( "./instruction_yaris.pdf" )

    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    print(len(pages))

    for page in pages:
        print(f"{page.metadata}\n")
        data = {"content": page.page_content}
        response = requests.post(url, json=data) 

        if response.status_code == 200:
            print(f"Success: {response.json()}")
        else:
            print(f"Error {response.status_code}: {response.text}") 


asyncio.run(read())