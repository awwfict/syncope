import inspect
from concurrent.futures import ThreadPoolExecutor, Future
from . import errs
from .decaf import decompose
from .donut import log
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁

bash = ThreadPoolExecutor(max_workers=4, thread_name_prefix="syncopated")


class smart:
    __slots__ = ("process", "do", "nowsnapshot")

    def __init__(self, worker: str, callernowsnapshot):
        self.process = worker
        self.do = None
        self.nowsnapshot = callernowsnapshot

    def to(self, action) -> "smart":
        self.do = action
        return self

    def at(self, startln: int, endln = None) -> Future | None:
        return desolate(self.process, self.do, startln, endln, self.nowsnapshot)
    

def desolate(worker: str, action, startln: int, endln, callernowsnapshot) -> Future | None:
    quickcheck = lambda: 1 if not startln or type(startln) is not int or startln < 1 else 0
    if quickcheck() == 1: log.error(errs.msf3); return None
    else:
        quickcheck = lambda: 1 if not endln else 0
        if quickcheck() == 1: endln = startln
        quickcheck = lambda: 1 if type(endln) is not int or endln < 1 else 0
        if quickcheck() == 1: endln = startln; log.warning(errs.mss22)

    whereami = callernowsnapshot.f_code.co_filename
    code_obj = decompose(whereami, startln, endln)
    if code_obj is None:
        log.error(errs.msg4)
        return None

    iso_globals1 = dict(callernowsnapshot.f_globals)
    iso_locals1 = dict(callernowsnapshot.f_locals)
    before_keys1 = set(iso_locals1.keys())
    iso_locals1["_process__"] = worker

    def todo():
        if callable(action):
            action()
        exec(code_obj, iso_globals1, iso_locals1)
        if "result" in iso_locals1 and "result" not in before_keys1:
            return iso_locals1["result"]
        return {k: v for k, v in iso_locals1.items() if k != "_process__"}

    return bash.submit(todo)


def assign(target: str, to = None, at = None):
    callernowsnapshot = inspect.stack()[1].frame

    if isinstance(target, str) and " to " in target and " at " in target and to is None:
        parts = target.split(" to ", 1)
        process = parts[0].strip()
        watchadoin, line_part = parts[1].rsplit(" at ", 1)
        watchadoin = watchadoin.strip()
        line_part = line_part.strip()

        if ".." in line_part:
            sets, sete = line_part.split("..", 1)
            startlne = int(sets) if sets.strip().isdigit() else sets
            endlne = int(sete) if sete.strip().isdigit() else sete
        else:
            startlne = int(line_part) if line_part.isdigit() else line_part
            endlne = None

        dodo = callernowsnapshot.f_locals.get(watchadoin) or callernowsnapshot.f_globals.get(watchadoin)
        return desolate(process, dodo, startlne, endlne, callernowsnapshot)

    if to is not None and at is not None:
        if isinstance(at, tuple):
            return desolate(target, to, at[0], at[1], callernowsnapshot)
        return desolate(target, to, at, None, callernowsnapshot)

    return smart(target, callernowsnapshot)
