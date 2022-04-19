from cofactr.graph import GraphAPI
from cofactr.cursor import first

g = GraphAPI()

cursor = g.get_products(batch_size=1, external=False)

print(first(cursor, 2))
