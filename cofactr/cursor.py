# Standard Modules
from itertools import islice
from typing import Callable
from urllib import parse


parse_query_params = lambda url: {
    k: v[0] for k, v in parse.parse_qs(parse.urlparse(url).query).items()
}

parse_paging_data = lambda paging: {
    "previous": parse_query_params(paging["previous"]),
    "next": parse_query_params(paging["next"]),
}

first = lambda xs, i: list(islice(xs, None, i))


class Cursor(object):
    def __init__(
        self,
        request: Callable,
        before,
        after,
        limit,
        batch_size,
        *args,
        **kwargs,
    ):

        self.request = request
        self.limit = limit
        self.batch_size = batch_size
        self.args = args
        self.kwargs = kwargs

        self.i = 0
        self.batch_i = self.i
        self.batch = self.request_batch(before=before, after=after)

    def request_batch(self, before=None, after=None, *args, **kwargs):
        return self.request(
            *self.args,
            **self.kwargs,
            before=before,
            after=after,
            limit=self.batch_size,
        )

    def __iter__(self):

        return self

    def __next__(self):

        if self.limit and self.i >= self.limit:
            raise StopIteration

        if self.batch is None or self.batch_i >= len(self.batch["data"]):
            paging = parse_paging_data(self.batch["paging"])

            next_batch = paging["next"]

            if not next_batch:
                raise StopIteration

            self.batch_i = 0
            self.batch = self.request_batch(**paging["next"])

        x = self.batch["data"][self.batch_i]

        self.i += 1
        self.batch_i += 1

        return x
