import sys
from pathlib import Path

header = "# coding: pysign\n"
allowed = ("# coding: pysign", "# coding: pyassign", "# coding: syncope", "# coding: egg")

def sticker(path: str) -> None:
    path = Path(path)
    if not path.exists() or path.suffix != ".py":
        print(f'✕ File «{path}» not found or not a .py')
        return

    content = path.read_text(encoding="utf-8")
    if content.lower().startswith(allowed):
        print(f'𝒊 Syntax already active in «{path}»')
        return

    path.write_text(header + content, encoding="utf-8")
    print(f'✦ Activated ! Header added to «{path}»')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('𝒊 Check up your usage you can by «python -m syncope «yourfile.py»')
    else:
        for target in sys.argv[1:]:
            sticker(target)
