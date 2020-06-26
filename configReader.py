from typing import List

def init() -> None:
    global delay
    global logins
    global waitTimes
    global repos
    global position
    global commitOutput
    global readingDict
    delay = 0.25
    logins = {}
    waitTimes = {}
    repos = {}
    position = (0,0)
    commitOutput = "f'{name}.git/{c.hexsha}'"
    readingDict = {'position' : readPosition,
                   'delay' : readDelay,
                   'commitOutput' : readCommitOutput,
                   'repo' : readRepo,
                   'key' : readKey}

def readConfig() -> None:
    global readingDict
    with open('config.txt', 'r') as conf:
        for line in conf.readlines():
            l = line.strip('\n').split(':', 1)
            if len(l) < 2:
                continue
            readingDict.get(l[0], lambda x: None)(l[1])

def readPosition(s: str) -> None:
    ss = s.split(',')
    global position
    position = int(ss[0]), int(ss[1])

def readDelay(s: str) -> None:
    global delay
    delay = float(s)

def readCommitOutput(s: str) -> None:
    global commitOutput
    commitOutput = s

def readRepo(s: str) -> None:
    name, addr = s.split('::', 1)
    global repos
    repos[addr.replace('\\', '/')] = name

def readKey(s: str) -> None:
    ss = s.split(':')
    if len(ss) != 4:
        return
    key, login, wt, password = ss
    global logins
    if key == 'p' or key in logins.keys():
        return
    waitTime = float(wt) if len(wt) > 0 else 0.0
    logins[key] = (login, password)
    global waitTimes
    waitTimes[key] = waitTime

def setLoginPos(x: int, y: int) -> None:
    with open('config.txt', 'r') as conf:
        lines = conf.readlines()
    if len(lines) > 0:
        linefound = False
        for idx, line in enumerate(lines):
            if line.startswith('position:'):
                lines[idx] = f'position: {x},{y}\n'
                linefound = True
                break
        if not linefound:
            lines.append(f'\nposition: {x},{y}')
    else:
        lines.append(f'\nposition: {x},{y}')
    with open('config.txt', 'w') as conf:
        conf.writelines(lines)
    global position
    position = x, y

def getLogin(key: str) -> str:
    return logins[key]

def getWaitTime(key: str) -> float:
    return waitTimes[key]

def getKeys() -> List[str]:
    return logins.keys()
