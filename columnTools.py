from typing import Optional

def quotes(x: str) -> None:
    xs = x.split('\n')
    for s in xs:
        print('"'+s+'",')

def singleQuotes(x: str) -> None:
    xs = x.split('\n')
    for s in xs:
        print("'"+s+"',")
    
def outQuotes(x: str, pref: Optional[str] = '', qType: Optional[str] = '"', lines:Optional[bool] = True) -> str:
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

def quotesWithPref(x: str, pref: Optional[str] = '') -> None:
    xs = x.split('\n')
    for s in xs:
        print(f'"{pref}{s}",')

def prefAndComma(x: str, pref: Optional[str] = '') -> None:
    xs = x.split('\n')
    for s in xs:
        print(f'{pref}{s},')

def defCols(src: str, tabAlias: Optional[str] = '', isColAlias: Optional[bool] = True) -> None:
    if tabAlias != '':
        tabAlias = tabAlias + '.'
    toColumns(outQuotes(src, tabAlias), isColAlias)

def toColumns(src: str, isColAlias: Optional[bool] = True) -> None:
    toFunc(src, 'aColumn(', '),', isColAlias)

def toCs(src:str, isColAlias: Optional[bool] = True) -> None:
    toFunc(src, '.c(', ')', isColAlias)

def toFunc(src: str, pref: str, suf: str, isColAlias: Optional[bool] = True, hideId: Optional[bool] = False) -> str:
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

def defCs(src: str, tabAlias: Optional[str] = '', isColAlias: Optional[bool] = False) -> str:
    if tabAlias != '':
        tabAlias = tabAlias + '.'
    return toFunc(outQuotes(src, tabAlias), '.c(', ')', isColAlias)

def configureColumns(src: str, width: Optional[str] = '100', hideId: Optional[bool] = True) -> str:
    suf = ', "' + width + 'px");'
    return toFunc(outQuotes(src), 'configure(', suf, hideId = hideId)
