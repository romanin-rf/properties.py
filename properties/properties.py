from io import TextIOWrapper, StringIO
from typing import Dict, Any
#@ Local Import's
from .functional import is_comment_line, conv, is_pass_line

def loads(text: str) -> Dict[str, Any]:
    d = {}
    for line in StringIO(text).readlines():
        if (not is_comment_line(line)) and (not is_pass_line(line)):
            key, value, em = "", "", 0
            for s in line:
                if em == 0:
                    if s == "=": em = 1
                    elif s == " ": pass
                    else: key += s
                elif em == 1:
                    if (len(value) == 0) and (s == " "): pass
                    else: value += s
            d[key] = conv(value)
    return d

def load(fp: TextIOWrapper) -> Dict[str, Any]:
    d = {}
    for line in fp.readlines():
        if (not is_comment_line(line)) and (not is_pass_line(line)):
            key, value, em = "", "", 0
            for s in line:
                if em == 0:
                    if s == "=": em = 1
                    elif s == " ": pass
                    else: key += s
                elif em == 1:
                    if (len(value) == 0) and (s == " "): pass
                    else: value += s
            d[key] = conv(value)
    return d

def dumps(data: Dict[str, Any]) -> str:
    fp = StringIO("")
    fp.writelines([f"{i}={data[i]}\n" for i in data])
    fp.flush()
    fp.seek(0)
    return fp.read()

def dump(data: Dict[str, Any], fp: TextIOWrapper) -> None:
    path = fp.name ; fp.close() ; fp = open(path, "w", encoding=fp.encoding, errors=fp.errors)
    fp.writelines([f"{i}={data[i]}\n" for i in data])
    fp.flush()
