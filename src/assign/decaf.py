import textwrap
from functools import lru_cache
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

@lru_cache(maxsize=64)
def getlines(path: str) -> tuple[str, ...]:
    with open(path, "r", encoding="utf-8") as file:
        return tuple(file.readlines())


@lru_cache(maxsize=256)
def decompose(path: str, startln: int, endln: int):
    lines = getlines(path)
    if startln > len(lines):
        return None
    selected = lines[startln - 1 : endln]
    clean = textwrap.dedent("".join(selected))
    return compile(clean, path, "exec")


def cleanertool() -> None:
    getlines.cache_clear()
    decompose.cache_clear()
