import itertools

from cofactr.graph import GraphAPI

g = GraphAPI()

cursor = g.get_products(batch_size=1, external=False)

first = lambda xs, i: list(itertools.islice(cursor, None, i))

print(first(cursor, 2))
