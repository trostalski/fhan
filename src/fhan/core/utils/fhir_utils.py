def is_bundle(input: dict):
    if not isinstance(input, dict):
        return False
    return "resourceType" in input and input["resourceType"] == "Bundle"


def is_empty_bundle(input: dict):
    return "entry" not in input or len(input["entry"]) == 0
