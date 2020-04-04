def init():
    global delay
    global logins
    global waitTimes
    global repos
    global position
    global commitOutput
    delay = 0.25
    logins = {}
    waitTimes = {}
    repos = {}
    position = (0,0)
    commitOutput = "f'{name}.git/{c.hexsha}'"

def readConfig():
    with open('config.txt', 'r') as conf:
        for line in conf.readlines():
            if line.startswith('position:'):
                s = line.split('position:', 1)[1].strip('\n')
                ss = s.split(',')
                global position
                position = int(ss[0]), int(ss[1])
            elif line.startswith('delay:'):
                s = line.split('delay:',1)[1]
                global delay
                delay = float(s)
            elif line.startswith('commitOutput:'):
                s = line.split('commitOutput:', 1)[1].strip('\n')
                global commitOutput
                commitOutput = s
            elif line.startswith('repo:'):
                s = line.split('repo:',1)[1].strip('\n')
                ss = s.split('::')
                name = ss[0]
                addr = ss[1]
                branch = 'master'
                if len(ss) > 2:
                    branch = ss[2]
                global repos
                repos[addr] = name
            elif line.startswith('key:'):
                s = line.split('key:',1)[1].strip('\n')
                ss = s.split(':')
                if len(ss) < 4:
                    continue
                key = ss[0]
                login = ss[1]
                password = ss[3]
                waitTime = 0.0
                if len(ss[2]) > 0:
                    waitTime = float(ss[2])
                global logins
                if key in logins.keys() or key == 'p':
                    continue
                logins[key] = (login, password)
                global waitTimes
                waitTimes[key] = waitTime


def setLoginPos(x, y):
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

def getDelay():
    return delay

def getPosition():
    return position

def getCommitOutput():
    return commitOutput

def getRepos():
    return repos

def getLogin(key):
    return logins[key]

def getWaitTime(key):
    return waitTimes[key]

def getKeys():
    return logins.keys()
