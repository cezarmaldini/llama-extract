import os
import json
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse, LlamaExtract, SourceText

from schema import Itens

load_dotenv()
        

def output_json(data, file_name="data.json"):
    path = os.path.join(os.getcwd(), file_name)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Arquivo salvo em: {path}")

def parsed(api_key: str, path: str):
    parser = LlamaParse(api_key=api_key)

    result = parser.get_json_result(path)
    return result

def extract_pages_content(result):
    pages_content = []

    # O resultado vem como uma lista com um único objeto contendo "pages"
    for page in result[0].get("pages", []):
        pages_content.append(page.get("text", ""))

    return pages_content

def extract_itens(api_key: str, pages_content: list):
    extractor = LlamaExtract(api_key=api_key)
    
    agent_name = 'extract-agent'
    
    agents = extractor.list_agents()
    names = [a.name for a in agents]
    
    if agent_name in names:
        agent = extractor.get_agent(name=agent_name)
    else:
        agent = extractor.create_agent(
            name=agent_name, data_schema=Itens
        )
    
    results = []
    
    for content in pages_content:
        result = agent.extract(
            SourceText(text_content=content)
        )
        results.append(result.data)
    
    return results

def main():
    API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
    PATH = "data/ARACAJU.2025.03 - Baixo Padrão (Moradas da Aruana) - Alumbox.pdf"

    result = parsed(API_KEY, PATH)
    
    contents = extract_pages_content(result=result)
    
    itens = extract_itens(api_key=API_KEY, pages_content=contents)
    
    output_json(data=itens)

if __name__ == "__main__":
    main()