# hfc-search

## Summary

Many aspects of the coding challenge called for retrieval based on the semantic intent of the search query -- while implementing basic heuristics would have been the "quick and dirty" method of completing the task I instead attempted to implement a true semantic retrieval mechanism through a series of experiments. Recent advancements in LLMs and embedding models has lowered the bar for implementing such a system.

The code found in this repo implments an in-memory cosine similarity search using OpenAI embeddings.

## Dependencies

- `docker` & `docker-compose`

## Setup

```bash
unzip DataEngCodeTest.zip
mv DataEngCodeTest/* site/backend/data/
```

## run

```bash
cd site/
docker compose up --build --remove-orphans
cd backend
bash ../scripts/load-sql.sh
```

OR

```bash
make up
```

## References

- [List of academic databases and search engines - Wikipedia](https://en.wikipedia.org/wiki/List_of_academic_databases_and_search_engines)
- [Specify which fields are indexed in ElasticSearch - Stack Overflow](https://stackoverflow.com/questions/13626617/specify-which-fields-are-indexed-in-elasticsearch)
- [Run Elasticsearch locally in Docker (without security) | Elasticsearch Guide [8.14] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html)
- [Semantic search using Elasticsearch and OpenAI | OpenAI Cookbook](https://cookbook.openai.com/examples/vector_databases/elasticsearch/elasticsearch-semantic-search)
- [How to Build a Semantic Search Engine With Transformers and Faiss | by Kostas Stathoulopoulos | Towards Data Science](https://towardsdatascience.com/how-to-build-a-semantic-search-engine-with-transformers-and-faiss-dcbea307a0e8)
