from fhan.models.R4.Bundle import Bundle


class SearchBundle:
    def __init__(self, bundle: dict):
        self.bundle = Bundle.from_dict(bundle)
        self.resources = [e.resource for e in self.bundle.entry]

    def __repr__(self) -> str:
        return f"SearchBundle({self.bundle})"

    def get_next_page(self):
        pass
