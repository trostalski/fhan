from fhan.client.generated.search_builder_mixin import SearchBuilderMixin


class SearchBuilder(SearchBuilderMixin):
    def __init__(self):
        self.search_string = ""
