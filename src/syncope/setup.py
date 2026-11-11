import re
import sys
import importlib.abc, importlib.util
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


class SyncLoader(importlib.abc.SourceLoader):
    def __init__(self, fullname, path):
        self.fullname = fullname
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        with open(path, "rb") as f:
            raw = f.read().decode("utf-8")

        transformed = _transform1(raw)
        return transformed.encode("utf-8")


class Finder(importlib.abc.MetaPathFinder):
    
    def finds(self, fullname, path, target=None):
        if fullname.startswith("syncope"):
            return None
        t = importlib.util.PathFinder.finds(fullname, path, target)
        
        if spec and t.origin and t.origin.endswith(".py"):
            t.loader = SyncLoader(fullname, t.origin)
            return t
        return None


def activate():
    if not any(isinstance(f, Finder) for f in sys.meta_path):
        sys.meta_path.insert(0, Finder())

