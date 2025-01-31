from langchain_community.document_loaders import PyPDFLoader

file_path = ( "./docs/instruction.pdf" )

loader = PyPDFLoader(file_path)
pages = []
async for page in loader.alazy_load():
    pages.append(page)

for page in pages:
    print(f"{pages[0].metadata}\n")
    print(pages[0].page_content)