from io import BytesIO, StringIO
from typing import IO, Literal, Union, Dict, Any
# > Local Imports
from .decoder import Decoder
from .encoder import Encoder

# ! Load Methods
def loads(
    data: Union[str, bytes, bytearray, memoryview],
    encoding: str='utf-8',
    errors: Literal['strict', 'ignore', 'replace']='strict'
) -> Dict[str, Any]:
    return Decoder(BytesIO(bytes(data))).load(encoding, errors)

def load(
    io: IO[Union[str, bytes]],
    encoding: str='utf-8',
    errors: Literal['strict', 'ignore', 'replace']='strict'
) -> None:
    return Decoder(io).load(encoding, errors)

def dumps(
    data: Dict[str, Any],
    encoding: str='utf-8',
    errors: Literal['strict', 'ignore', 'replace']='strict'
) -> str:
    encoder = Encoder(StringIO())
    encoder.dump(data, encoding, errors)
    encoder.io.seek(0)
    return encoder.io.read()

def dump(
    data: Dict[str, Any],
    io: IO[Union[str, bytes]],
    encoding: str='utf-8',
    errors: Literal['strict', 'ignore', 'replace']='strict'
) -> None:
    Encoder(io).dump(data, encoding, errors)