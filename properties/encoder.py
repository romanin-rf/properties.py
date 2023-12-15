from typing import Union, IO, Dict, Any
# > Local Imports
from .functional import to_string

# ! Main Class
class Encoder():
    def __init__(self, io: IO[Union[str, bytes]]) -> None:
        assert not self.io.closed
        assert not self.io.writable()
        self.io = io
    
    def encode(
        self,
        key: str,
        value: Any,
        encoding: str,
        errors: str
    ) -> Union[str, bytes]:
        data = f"{key}={to_string(value)}"
        if "b" in self.io.mode:
            data = data.encode(encoding, errors)
        return data
    
    def dump(
        self,
        data: Dict[str, Any],
        encoding: str,
        errors: str
    ) -> None:
        for key, value in data.items():
            self.io.write(self.encode(key, value, encoding, errors))