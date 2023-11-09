import pytest
from fhan.core.utils.path_utils import (
    is_choice_path,
    replace_choice_string,
    get_nth_part,
    remove_n_parts_from_start,
    remove_n_parts_from_end,
    get_path_length,
    is_root_path,
    join_paths,
)


@pytest.mark.parametrize(
    "path, expected",
    [("path.to.element[x]", True), ("path.to.element", False), ("", False)],
)
def test_is_choice_path(path, expected):
    assert is_choice_path(path) == expected


@pytest.mark.parametrize(
    "path, replace, expected",
    [
        ("path.to.element[x]", "String", "path.to.elementString"),
        ("path.to.element", "String", "path.to.element"),
        ("", "String", ""),
    ],
)
def test_replace_choice_string(path, replace, expected):
    assert replace_choice_string(path, replace) == expected


@pytest.mark.parametrize(
    "path, n, expected",
    [
        ("path.to.element", 0, "path"),
        ("path.to.element", 1, "to"),
        ("path.to.element", 2, "element"),
    ],
)
def test_get_nth_part(path, n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_nth_part(path, n)
    else:
        assert get_nth_part(path, n) == expected


@pytest.mark.parametrize(
    "path, n, expected",
    [
        ("path.to.element", 1, "to.element"),
        ("path.to.element", 2, "element"),
        ("path.to.element", 3, ""),
    ],
)
def test_remove_n_parts_from_start(path, n, expected):
    assert remove_n_parts_from_start(path, n) == expected


@pytest.mark.parametrize(
    "path, n, expected",
    [
        ("path.to.element", 1, "path.to"),
        ("path.to.element", 2, "path"),
        ("path.to.element", 3, ""),
    ],
)
def test_remove_n_parts_from_end(path, n, expected):
    assert remove_n_parts_from_end(path, n) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        ("path.to.element", 3),
        ("path", 1),
        (
            "",
            1,
        ),  # Depending on the definition, an empty string could have 0 parts. Adjust if needed.
    ],
)
def test_get_path_length(path, expected):
    assert get_path_length(path) == expected


@pytest.mark.parametrize(
    "path, expected", [("path", True), ("path.to", False), ("", False)]
)
def test_is_root_path(path, expected):
    assert is_root_path(path) == expected


@pytest.mark.parametrize(
    "paths, expected",
    [
        (("path", "to", "element"), "path.to.element"),
        (("path", ""), "path."),
        (("", ""), "."),
        (("path",), "path"),
        (tuple(), ""),
    ],
)
def test_join_paths(paths, expected):
    assert join_paths(*paths) == expected
