delay = [0.25]
logins = {}
waitTimes = {}
repos = {}
position = [(0,0)]
commitOutput = ["f'{name}.git/{c.hexsha}'"]
read = False

def readConfig():
    read = True
    with open('config.txt', 'r') as conf:
        for line in conf.readlines():
            if line.startswith('position:'):
                s = line.split('position:', 1)[1].strip('\n')
                ss = s.split(',')
                position[0] = int(ss[0]), int(ss[1])
            elif line.startswith('delay:'):
                s = line.split('delay:',1)[1]
                delay[0] = float(s)
            elif line.startswith('commitOutput:'):
                s = line.split('commitOutput:', 1)[1].strip('\n')
                commitOutput[0] = s
            elif line.startswith('repo:'):
                s = line.split('repo:',1)[1].strip('\n')
                ss = s.split('::')
                name = ss[0]
                addr = ss[1]
                branch = 'master'
                if len(ss) > 2:
                    branch = ss[2]
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
                if key in logins.keys() or key == 'p':
                    continue
                logins[key] = (login, password)
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
    position[0] = x, y

def getDelay():
    return delay[0]

def getPosition():
    return position[0]

def getCommitOutput():
    return commitOutput[0]

def getRepos():
    return repos

def getLogin(key):
    return logins[key]

def getWaitTime(key):
    return waitTimes[key]

def getKeys():
    return logins.keys()
