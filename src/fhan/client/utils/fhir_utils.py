def is_bundle(input: dict):
    if not isinstance(input, dict):
        return False
    return "resourceType" in input and input["resourceType"] == "Bundle"


def is_empty_bundle(input: dict):
    """This does not check if the input is a bundle."""
    return "entry" not in input or len(input["entry"]) == 0


def safe_get(target, *attrs):
    """
    Try to get the item from the target safely.
    If any item in the chain is missing, return None.
    """
    for attr in attrs:
        try:
            # Check if the target is a dict or list, and then attempt to access the item.
            if isinstance(target, dict) and attr in target:
                target = target[attr]
            elif (
                isinstance(target, list)
                and isinstance(attr, int)
                and attr < len(target)
            ):
                target = target[attr]
            else:
                # If the attr is not a valid index/key, or the target is not a dict/list, return None
                return None
        except (TypeError, IndexError, KeyError):
            # If any exception occurred due to invalid indexing/key, return None
            return None
    return target
