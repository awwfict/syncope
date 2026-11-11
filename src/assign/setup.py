import codecs
import re
from encodings import utf_8

seepython = re.compile(
    r'^(\s*)assign\s+(.+?)\s+to\s+(.+?)\s+at\s+(\d+)(?:(?:\.\.|-|\s*,\s*)(\d+))?(.*)$',
    re.MULTILINE
)

def rename(match: re.Match) -> str: 
    indent, worker, action, startln, endln, tail = match.groups()
    if endln:
        return f"{indent}assign({worker}, to={action}, at=({startln}, {endln})){tail}"
    return f"{indent}assign({worker}, to={action}, at={startln}){tail}"

def apply(source: str) -> str: 
    return seepython.sub(rename, source)

def decoded(input_bytes: bytes, errors: str = 'strict') -> tuple[str, int]:
    text, length = utf_8.decode(input_bytes, errors)
    return apply(text), length 

def lookup(encoding_name: str):  
    if encoding_name.lower() in ('pysign', 'pyassign'):
        return codecs.CodecInfo(
            name=encoding_name,
            encode=utf_8.encode,
            decode=decoded, 
        )
    return None

def setup():#!
    codecs.register(lookup)
