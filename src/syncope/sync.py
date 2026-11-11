import inspect, textwrap
from . import errs
from .decaf import decompose
from .donut import log, lockdown, unresponsed
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

def sign(target) -> None:
    if not callable(target):
        log.error(errs.msf3)
        return None

    frame = inspect.stack()[1]
    seen = frame.frame.f_locals
    contain = frame.frame.f_globals
    key = (inspect.getsourcefile(target), target.__name__)

    with lockdown:
        if key in unresponsed:
            log.warning(errs.msg23)
            return None
        unresponsed.add(key)

    try:
        codeobj = decompose(target)
        if codeobj is None:
            log.error(errs.msg4)
            return None
        exec(codeobj, contain, seen)
    finally:
        with lockdown:
            unresponsed.discard(key)
