import inspect, textwrap
from . import errs
from .decaf import decompose
from .donut import log, lockdown, unresponsed
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

def sign(startln: int, endln = None) -> None:
    quickcheck = lambda: 1 if not startln or type(startln) is not int or startln < 1 else 0

    if quickcheck() == 1: log.error(errs.msf3); return None
    else:
        quickcheck = lambda: 1 if not endln else 0
        if quickcheck() == 1: endln = startln
        quickcheck = lambda: 1 if type(endln) is not int  or endln < 1 else 0
        if quickcheck() == 1: endln = startln; log.warning(errs.mss22)
    
    frame = inspect.stack()[1]
    whereami = frame.filename #current file
    seen = frame.frame.f_locals #params inside the calling func
    contain = frame.frame.f_globals #imports, scripts etc
    getlines = (whereami, startln)
    
    with lockdown:
        if getlines in unresponsed:
            log.warning(errs.msg23)
            return None
        unresponsed.add(getlines)

    try:
        code_obj = decompose(whereami, startln, endln)
        if code_obj is None:
            log.error(errs.msg4)
            return None
        exec(code_obj, contain, seen)
        
    finally:
        with lockdown:
            unresponsed.discard(getlines)
