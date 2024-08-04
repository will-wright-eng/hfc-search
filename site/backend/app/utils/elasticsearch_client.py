from elasticsearch import Elasticsearch

es = Elasticsearch(["http://elasticsearch:9200"])


def create_index(index_name):
    es.indices.create(index=index_name, ignore=400)


def index_data(index_name, data):
    es.index(index=index_name, body=data)


def search_index(index_name, query):
    return es.search(index=index_name, body={"query": {"match": {"content": query}}})
