import inspect
import textwrap
from functools import lru_cache
# ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

@lru_cache(maxsize=256)
def decompose(func):
    try:
        lines, _ = inspect.getsourcelines(func)
        path = inspect.getsourcefile(func) or "<syncope>"
    except (TypeError, OSError):
        return None

    body = []
    headerdone = False
    for line in lines:
        stripped = line.lstrip()
        if not headerdone:
            if stripped.startswith("def ") and stripped.rstrip().endswith(":"):
                headerdone = True
            continue
        body.append(line)

    if not body:
        return None

    clean = textwrap.dedent("".join(body))
    return compile(clean, path, "exec")


def cleanertool() -> None:
    decompose.cache_clear()

