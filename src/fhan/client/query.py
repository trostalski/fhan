class Search(ResourceQueryMixin):
    def __init__(self):
        pass


if __name__ == "__main__":
    query = Search.Patient.param("active")
