import re
from typing import Any, Union, Iterable, TypeVar, List

T, NT = TypeVar("T"), TypeVar("NT")

def is_comment_line(line: str) -> bool:
    c = 0
    for i in line:
        if i != " ":
            if (i == "#") and (c == 0): return True
            else: c += 1
    return False

def is_pass_line(line: str) -> bool:
    if "=" not in line:
        return True
    elif line.replace(" ", "") == "":
        return True
    return False

def stendel(text: str): return re.sub(r"^\s+|\n|\r|\s+$", '', text)

def conv(value: str) -> Union[Any, str]:
    try: return eval(stendel(value))
    except: pass
    return stendel(value)

def removes(l: Iterable[Union[T, NT]], d: Iterable[NT]) -> List[T]:
    dl = []
    for i in l:
        if i not in d:
            dl.append(i)
    return dl