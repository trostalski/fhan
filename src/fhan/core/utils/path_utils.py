def is_choice_path(path: str):
    return "[x]" in path


def replace_choice_string(path: str, replace: str):
    return path.replace("[x]", replace)


def get_nth_part(path: str, n: int):
    return path.split(".")[n]


def remove_n_parts_from_start(path: str, n: int):
    return ".".join(path.split(".")[n:])


def remove_n_parts_from_end(path: str, n: int):
    return ".".join(path.split(".")[:-n])


def get_path_length(path: str):
    return len(path.split("."))


def is_root_path(path: str):
    if not path:
        return False
    return "." not in path


def join_paths(*paths: str):
    return ".".join(paths)
