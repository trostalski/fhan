from fhan.client.generated._search_builder_mixin import SearchBuilderMixin


class SearchBuilder(SearchBuilderMixin):
    def __init__(self):
        self.search_string = "?"

    def get_search_string(self):
        return self.search_string
