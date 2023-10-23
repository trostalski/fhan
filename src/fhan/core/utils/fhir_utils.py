def is_bundle(input: dict):
    if not isinstance(input, dict):
        return False
    return "resourceType" in input and input["resourceType"] == "Bundle"


def is_empty_bundle(input: dict):
    return "entry" not in input or len(input["entry"]) == 0


def safe_get(target, *attrs):
    """
    Try to get attribute from the target safely.
    If any attribute in the chain is missing, return None.
    """
    for attr in attrs:
        if isinstance(attr, str):
            if hasattr(target, attr):
                target = getattr(target, attr)
            else:
                return None
        elif isinstance(attr, int):
            if len(target) > attr:
                target = target[attr]
            else:
                return None
    return target
