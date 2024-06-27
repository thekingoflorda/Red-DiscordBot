import textwrap
from typing import Any

import pytest
import yaml
from schema import And, Optional, SchemaError

from redbot.cogs.trivia.schema import (
    ALWAYS_MATCH,
    MATCH_ALL_BUT_STR,
    NO_QUESTIONS_ERROR_MSG,
    TRIVIA_LIST_SCHEMA,
    format_schema_error,
)

branch_coverage = {
    1001: False,  # if list_names
    1002: False,  # except InvalidListError as exc
    1003: False,  # if isinstance(e, SchemaError)
    1004: False,  # if not isinstance(e, SchemaError)
    1005: False,  # if problem_lists
    2001: False,  # if not keys
    2002: False,  # if isinstance(current, And)
}

def set_branch_coverage(branch_id):
    branch_coverage[branch_id] = True

def _get_error_message(*keys: Any, key: str = "UNKNOWN", parent_key: str = "UNKNOWN") -> str:
        if not keys:
            set_branch_coverage(2001)
            return TRIVIA_LIST_SCHEMA._error

        current = TRIVIA_LIST_SCHEMA.schema
        for key_name in keys:
            if isinstance(current, And):
                set_branch_coverage(2002)
                current = current.args[0]
            current = current[key_name]
        return str(current._error).format(key=repr(key), parent_key=repr(parent_key))

def test_trivia_lists():
    from redbot.cogs.trivia import InvalidListError, get_core_lists, get_list

    list_names = get_core_lists()
    set_branch_coverage(1001)
    assert list_names

    # Manually adding invalid trivia list for testing
    list_names.append('invalid_trivia_list')
    
    problem_lists = []
    for l in list_names:
        try:
            get_list(l)
        except InvalidListError as exc:
            set_branch_coverage(1002)
            e = exc.__cause__
            if isinstance(e, SchemaError):
                set_branch_coverage(1003)
                problem_lists.append((l.stem, f"SCHEMA error:\n{format_schema_error(e)}"))
            else:
                set_branch_coverage(1004)
                problem_lists.append((l.stem, f"YAML error:\n{e!s}"))

    if problem_lists:
        set_branch_coverage(1005)
        msg = "\n".join(
            f"- {name}:\n{textwrap.indent(error, '    ')}" for name, error in problem_lists
        )
        raise TypeError("The following lists contain errors:\n" + msg)

    # Testing _get_error_message function with different inputs to trigger the branches
    _get_error_message()
    _get_error_message('some_key')
    _get_error_message('some_key', key='test_key', parent_key='parent_key')
    _get_error_message('some_key', 'nested_key', key='test_key', parent_key='parent_key')

    with open("branch_coverage_report.txt", "w") as f:
        for branch_id, was_taken in branch_coverage.items():
            f.write(f"Branch {branch_id}: {'Taken' if was_taken else 'Not Taken'}\n")

@pytest.mark.parametrize(
    "data,error_msg",
    (
        ("text", _get_error_message()),
        ({"AUTHOR": 123}, _get_error_message(Optional("AUTHOR"), key="AUTHOR")),
        ({"CONFIG": 123}, _get_error_message(Optional("CONFIG"), key="CONFIG")),
        (
            {"CONFIG": {"key": "value"}},
            _get_error_message(Optional("CONFIG"), ALWAYS_MATCH, key="key", parent_key="CONFIG"),
        ),
        (
            {"CONFIG": {"bot_plays": "wrong type"}},
            _get_error_message(
                Optional("CONFIG"), Optional("bot_plays"), key="bot_plays", parent_key="CONFIG"
            ),
        ),
        ({"AUTHOR": "Correct type but no questions."}, NO_QUESTIONS_ERROR_MSG),
        ({"Question": "wrong type"}, _get_error_message(str, key="Question")),
        ({"Question": [{"wrong": "type"}]}, _get_error_message(str, key="Question")),
        ({123: "wrong key type"}, _get_error_message(MATCH_ALL_BUT_STR, key="123")),
    ),
)
def test_trivia_schema_error_messages(data: Any, error_msg: str):
    with pytest.raises(SchemaError) as exc:
        TRIVIA_LIST_SCHEMA.validate(data)

    assert format_schema_error(exc.value) == error_msg

def test_trivia_lists_empty_list_names():
    from redbot.cogs.trivia import get_core_lists, get_list

    def mock_get_core_lists():
        return []

    original_get_core_lists = get_core_lists
    get_core_lists = mock_get_core_lists

    try:
        test_trivia_lists()
    except AssertionError:
        pass
    finally:
        get_core_lists = original_get_core_lists

def test_trivia_lists_invalid_list_error_yaml():
    from redbot.cogs.trivia import InvalidListError, get_core_lists, get_list

    def mock_get_core_lists():
        return ["mock_list"]

    def mock_get_list(name):
        e = Exception("YAML error")
        raise InvalidListError() from e

    original_get_core_lists = get_core_lists
    original_get_list = get_list
    get_core_lists = mock_get_core_lists
    get_list = mock_get_list

    try:
        test_trivia_lists()
    except TypeError:
        pass
    finally:
        get_core_lists = original_get_core_lists
        get_list = original_get_list

def test_trivia_lists_invalid_list_error_schema():
    from redbot.cogs.trivia import InvalidListError, get_core_lists, get_list

    def mock_get_core_lists():
        return ["mock_list"]

    def mock_get_list(name):
        e = SchemaError("Schema error")
        raise InvalidListError() from e

    original_get_core_lists = get_core_lists
    original_get_list = get_list
    get_core_lists = mock_get_core_lists
    get_list = mock_get_list

    try:
        test_trivia_lists()
    except TypeError:
        pass
    finally:
        get_core_lists = original_get_core_lists
        get_list = original_get_list
