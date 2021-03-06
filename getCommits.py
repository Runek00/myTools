from git import Repo
from tkinter import Tk
from concurrent.futures import ThreadPoolExecutor
import configReader as cr
from functools import wraps
from typing import Callable, Optional

def onEachRepo(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        outstr = ''
        with ThreadPoolExecutor() as executor:
            results = [executor.submit(func, Repo(adr), name, *args, **kwargs) for adr, name in cr.repos.items()]  
            for r in results:
                outstr += r.result()
        print('\ndone')
        return outstr
    return wrapper

@onEachRepo
def getCommits(repo: Repo, name: str, taskId: int, commits_back: Optional[int] = 50) -> str:
    outstr = ''
    fffc = filter(
        lambda c: (str(taskId) in c.message),
        list(repo.iter_commits(repo.active_branch, max_count=commits_back)))
    for c in fffc:
        out = eval(cr.commitOutput)
        outstr += out + '\n'
        print(out)
    return outstr

@onEachRepo
def pullAll(repo: Repo, name: str) -> str:
    outstr = ''
    print(f'{name}\n')
    remote = repo.remote()
    out = remote.pull()
    for n in out:
        if len(n.note) > 0:
            outstr += n.note + ''
    return outstr
