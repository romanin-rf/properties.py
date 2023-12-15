from typing import Union

# ! Types
class PropertiesValueObject:
    def __properties_str__(self) -> str:
        return ""

PropertiesValueType = Union[PropertiesValueObject, object]

# ! Checking Methods
def is_pass(line: str) -> bool:
    if "=" not in line:
        return True
    elif line.replace(" ", "") == "":
        return True
    return False

def is_comment(line: str) -> bool:
    c = 0
    for i in line:
        if i != " ":
            if (i == "#") and (c == 0):
                return True
            else:
                c += 1
    return False

# ! Other Methods
def to_string(obj: PropertiesValueType) -> str:
    if hasattr(obj, "__properties_str__"):
        return obj.__properties_str__()
    if isinstance(obj, str):
        return f"\"{obj}\""
    return repr(obj)