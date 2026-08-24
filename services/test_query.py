from services.fuseki_service import execute_query
from services.sparql_queries import students_studying_semantic_web


query = students_studying_semantic_web()

result = execute_query(query)

print(result)

