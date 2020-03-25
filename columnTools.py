def quotes(x):
    xs = x.split('\n')
    for s in xs:
        print('"'+s+'",')

def singleQuotes(x):
    xs = x.split('\n')
    for s in xs:
        print("'"+s+"',")
    
def outQuotes(x, pref = '', qType = '"', lines = True):
    out = ''
    xs = x.split('\n')
    for s in xs:
        out = out + qType+pref+s+qType + ','
        if lines:
            out += '\n'
    if lines:
        return out[:-2]
    else:
        return out[:-1]

def quotesWithPref(x, pref = ''):
    xs = x.split('\n')
    for s in xs:
        print(f'"{pref}{s}",')

def prefAndComma(x, pref = ''):
    xs = x.split('\n')
    for s in xs:
        print(f'{pref}{s},')

def defCols(src, tabAlias='', isColAlias = True):
    if tabAlias != '':
        tabAlias = tabAlias + '.'
    toColumns(outQuotes(src, tabAlias), isColAlias)

def toColumns(src, isColAlias = True):
    toFunc(src, 'aColumn(', '),', isColAlias)

def toCs(src, isColAlias = True):
    toFunc(src, '.c(', ')', isColAlias)

def toFunc(src, pref, suf, isColAlias = True, hideId = False):
    ss = src.split(',\n')
    outstr =''
    for s in ss:
        out = ''
        if s == '""':
            continue
        if hideId and (s == '"id"' or s == '"gid"'):
            out = f'hide({s});'
        else:
            out = f'{pref}{s}'
            if isColAlias:
                out = f'{out}, {s}'
            out = f'{out}{suf}'
        print(out)
        outstr += out + '\n'
    return outstr

def defCs(src, tabAlias = '', isColAlias = False):
    if tabAlias != '':
        tabAlias = tabAlias + '.'
    return toFunc(outQuotes(src, tabAlias), '.c(', ')', isColAlias)

def configureColumns(src, width = '100', hideId = True):
    suf = ', "' + width + 'px");'
    return toFunc(outQuotes(src), 'configure(', suf, hideId = hideId)
