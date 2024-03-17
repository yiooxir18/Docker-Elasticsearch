from elasticsearch import Elasticsearch
import sys


es = Elasticsearch(['http://localhost:9200'])

# Индексация файла
def index_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        response = es.index(index="blog", body={"content": content})
        print(f"Документ добавлен с ID: {response['_id']}")
    except Exception as e:
        print(f"Ошибка при индексации файла: {e}")

# Поиск фразы
def search_phrase(phrase):
    try:
        response = es.search(index="blog", body={
            "query": {
                "match": {
                    "content": phrase
                }
            }
        })
        for hit in response['hits']['hits']:
            print(f"Найден документ ID: {hit['_id']}, текст: {hit['_source']['content']}")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: search_engine.py [read|write] [файл|фраза]")
        sys.exit(1)
    
    mode = sys.argv[1]
    arg = sys.argv[2]

    if mode == "write":
        index_file(arg)
    elif mode == "read":
        search_phrase(arg)
    else:
        print("Неизвестный режим. Используйте 'read' или 'write'.")