# syncope
⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

**syncope** is a lightweight, zero-dependency Python library for line-level code routing and isolated fragment execution. Jump to specific lines synchronously or dispatch isolated code blocks into background threads to test and run parts of your script independently ^_<

## Installation

```bash
pip install syncope
```

## Quick Start

### 1. Synchronous Routing with `sign`
Execute specific lines immediately inside your live calling scope without running the rest of the file:

```python
from syncope import sign

# Jump to line 20 and execute it in the current context
sign(20)

# Execute a range of lines (from line 20 to 35)
sign(20, 35)
```

### 2. Isolated Async Execution with `assign`
Run a code fragment in an isolated snapshot of your environment in a background thread! Nice for testing parts of a script separately or running tasks in parallel:

```python
from syncope import assign

def start():
    print("program started!")

# Chain syntax
task1 = 
task = assign("task1").to(start).at(33, 35)

# String syntax
task = assign("task1 to start at 20..35")

# Get the returned result or modified local variables
output = task.result()
```

### 3. Natural Space-Separated Syntax
Enable clean space-separated commands like `assign Y to X at Z` without extra parentheses or quotes. First, activate the header in your script via terminal:

```bash
python -m syncope your_script.py
```

Then write directly in your file:

```python
from syncope import assign

assign "task1" to start at 20..35
```

## Cache Management

**syncope** compiles code fragments into bytecode and caches them in memory for maximum speed. If you modify the source file at runtime, clear the cache with:

```python
from syncope import cleanertool

cleanertool()
```

## License

Apache-2.0
