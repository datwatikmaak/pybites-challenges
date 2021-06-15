import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    Any = pprint.pformat(str, width=60, compact=True, depth=2, sort_dicts=True)
    return Any


pretty_string(Any)
