import inspect, textwrap
from  functools import lru_cache
from concurrent.futures import ThreadPoolExecutor, Future
from . import errs, donut
from errs import *
from donut import *
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
def redirect(startln: int, endln = None) -> None:
    quickcheck = lambda: 1 if not startln or type(startln) is not int or startln < 1 else 0

    if quickcheck() == 1: log.error(errs.msf3); return None
    else:
        quickcheck = lambda: 1 if not endln else 0
        if quickcheck() == 1: endln = startln
        quickcheck = lambda: 1 if type(endln) is not int  or endln < 1 else 0
        if quickcheck() == 1: endln = startln; log.warning()
    
    frame = inspect.stack()[1]
    whereami = frame.filename #current file
    seen = frame.frame.f_locals #params inside the calling func
    contain = frame.frame.f_globals #imports, scripts etc
    line_key = (whereami, startln)
    
        with lockdown:
            if line_key in unresponded:
                log.warning(errs.msr23)
                return None
            unresponded.add(line_key)
    
        try:
            code_obj = decompose(whereami, startln, endln)
            if code_obj is None:
                log.error(errs.msr4)
                return None
            exec(code_obj, contain, seen)
            
        finally:
            with lockdown:
                unresponded.discard(line_key)
    # with open(whereami, "r", encoding="utf-8") as file:
    #     ln = file.readlines()

    # selected = ln[startln - 1 : endln]
    # clean = textwrap.dedent("".join(selected))
    # exec(clean, contain, seen)
