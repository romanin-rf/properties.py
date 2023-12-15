import re
import ast
from typing import Optional, Union, IO, Dict, Tuple, Any
# > Local Imports
from .functional import (
    is_pass,
    is_comment
)

# ! Name
class Decoder:
    def __init__(self, io: IO[Union[str, bytes]]) -> None:
        assert not io.closed
        assert io.readable()
        self.io = io
    
    def decode(
        self,
        line: Union[str, bytes, bytearray, memoryview],
        encoding: str,
        errors: str
    ) -> Optional[Tuple[str, Any]]:
        if isinstance(line, (bytes, bytearray, memoryview)):
            line: str = bytes(line).decode(encoding, errors)
        if is_pass(line) or is_comment(line):
            return None
        key, value = re.sub(r"^\s+|\n|\r|\s+$", '', line).split('=', 1)
        key, value = key.strip(' '), ast.literal_eval(value.strip(' '))
        return key, value
    
    def load(self, encoding: str, errors: str) -> Dict[str, Any]:
        data = {}
        for line in self.io.readlines():
            d = self.decode(line, encoding, errors)
            if d is not None:
                data[d[0]] = d[1]
        return data