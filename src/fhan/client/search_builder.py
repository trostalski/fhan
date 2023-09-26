from fhan.client.generated._search_builder_mixin import SearchBuilderMixin


class SearchBuilder(SearchBuilderMixin):
    def __init__(self):
        self.search_string = "?"

    def build(self, validate: bool = False):
        return self.search_string
