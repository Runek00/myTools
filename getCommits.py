from git import Repo
from tkinter import Tk
from concurrent.futures import ThreadPoolExecutor
import configReader as cr

def onEachRepo(func):
    def wrapper(*args, **kwargs):
        outstr = ''
        with ThreadPoolExecutor() as executor:
            results = [executor.submit(func, Repo(adr), name, *args, **kwargs) for adr, name in cr.getRepos().items()]  
            for r in results:
                outstr += r.result()
        print('\ndone')
        return outstr
    return wrapper

@onEachRepo
def getCommits(repo, name, taskId, commits_back=50):
    outstr = ''
    fffc = filter(
        lambda c: (str(taskId) in c.message),
        list(repo.iter_commits(repo.active_branch, max_count=commits_back)))
    for c in fffc:
        out = eval(cr.getCommitOutput())
        outstr += out + '\n'
        print(out)
    return outstr

@onEachRepo
def pullAll(repo, name):
    outstr = ''
    print(f'{name}\n')
    remote = repo.remote()
    out = remote.pull()
    for n in out:
        if len(n.note) > 0:
            outstr += n.note + ''
    return outstr
