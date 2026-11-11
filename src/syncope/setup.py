import re
import sys
import importlib.abc, importlib.util
seepython = re.compile(
    r'^(\s*)assign\s+(.+?)\s+to\s+(.+?)\s+at\s+(\d+)(?:(?:\.\.|-|\s*,\s*)(\d+))?(.*)$',
    re.MULTILINE
)

def rename(match: re.Match) -> str:
    indent, worker, action, startln, endln, tail = match.groups()
    cleansy = worker.strip().strip('"\'')
    if endln:
        return f'{indent}assign("{cleansy}", to={action}, at=({startln}, {endln})){tail}'
    return f'{indent}assign("{cleansy}", to={action}, at={startln}){tail}'


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

        transformed = apply(raw)
        return transformed.encode("utf-8")


class SyncopeFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname.startswith("syncope"): return None
            
        spec = importlib.util.PathFinder.find_spec(fullname, path, target)
        if spec and spec.origin and spec.origin.endswith(".py"):
            spec.loader = SyncopeLoader(fullname, spec.origin)
            return spec
        return None


def activate():
    if not any(isinstance(f, SyncopeFinder) for f in sys.meta_path):
        sys.meta_path.insert(0, SyncopeFinder())
