import os
import json
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse, LlamaExtract, SourceText

from schema import Itens, ResumeProposal

load_dotenv()

class Ingestion:
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def parsed(self, path: str):
        parser = LlamaParse(api_key=self.api_key)

        result = parser.get_json_result(path)
        return result
    
    def extract_pages_content(self, result):
        pages_content = []

        for page in result[0].get("pages", []):
            pages_content.append(page.get("text", ""))

        return pages_content
    
    def extract_itens(self, pages_content: list):
        extractor = LlamaExtract(api_key=self.api_key)
        
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

def save_output_json(data, file_name: str):
    path = os.path.join(os.getcwd(), file_name)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Arquivo salvo em: {path}")

def main():
    API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
    PATH = "data/ARACAJU.2025.03 - Baixo Padrão (Moradas da Aruana) - Alumbox.pdf"
    
    ingestor = Ingestion(api_key=API_KEY)

    result = ingestor.parsed(PATH)
    
    contents = ingestor.extract_pages_content(result=result)
    
    itens = ingestor.extract_itens(pages_content=contents)
    
    save_output_json(data=itens, file_name='data/data.json')

if __name__ == "__main__":
    main()