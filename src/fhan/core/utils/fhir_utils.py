def is_bundle(input: dict):
    return "resourceType" in input and input["resourceType"] == "Bundle"


def is_empty_bundle(input: dict):
    return "entry" not in input or len(input["entry"]) == 0
