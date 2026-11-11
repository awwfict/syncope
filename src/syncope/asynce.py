import inspect
from concurrent.futures import ThreadPoolExecutor, Future
from . import errs
from .decaf import decompose
from .donut import log
#  ⠁⠂⠄⠄⠂⠁୨ৎ ⠁⠂⠄⠄⠂⠁
bash = ThreadPoolExecutor(max_workers=4, thread_name_prefix="syncopated")


def desolate(fragment: str, action, startln: int, endln, caller) -> Future | None:
    quickcheck = lambda: 1 if not startln or type(startln) is not int or startln < 1 else 0

    if quickcheck() == 1: log.error(errs.msf3); return None
    else:
        quickcheck = lambda: 1 if not endln else 0
        if quickcheck() == 1: endln = startln
        quickcheck = lambda: 1 if type(endln) is not int or endln < 1 else 0
        if quickcheck() == 1: endln = startln; log.warning(errs.mss22)

    whereami = caller.f_code.co_filename
    cut = decompose(whereami, startln, endln) #compiled script's part
    if cut is None:
        log.error(errs.msg4)
        return None

    snapnow = dict(caller.f_globals) #snapshot of local params which exists inside all current file
    locals = dict(caller.f_locals) #snapshot of all the elements directly in calling func
    listexist = set(locals.keys()) #snapshot of params which exists before a cutted script's piece was creted
    locals["_process__"] = fragment

    def todo():
        if callable(action):
            action()
        exec(cut, snapnow, locals)
        if "result" in locals and "result" not in listexist:
            return locals["result"]
        return {k: v for k, v in locals.items() if k != "_process__"}

    return bash.submit(todo)


def assign(target: str, to = None, at = None):
    caller = inspect.stack()[1].frame

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

        dodo = caller.f_locals.get(watchadoin) or caller.f_globals.get(watchadoin)
        return desolate(process, dodo, startlne, endlne, caller)

    if to is not None and at is not None:
        if isinstance(at, tuple):

            return desolate(target, to, at[0], at[1], caller)
        return desolate(target, to, at, None, caller)
    log.error(errs.msf3)
    return None
