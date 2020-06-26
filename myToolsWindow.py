import loginTools as lt
import configReader as cr
import tkinter as tk
from getCommits import getCommits, pullAll
from columnTools import defCs, configureColumns


def commitsFromInput():
    global nr_zad
    taskId = nr_zad.get()
    if taskId.strip() == '':
        return
    commits(taskId)

def commits(taskId: str):
    toClipboard(getCommits(taskId))
    
def cFromCols():
    global cols
    columns = cols.get(1.0, 'end')
    s = defCs(columns)
    toClipboard(s)

def confFromCols():
    global cols
    columns = cols.get(1.0, 'end')
    s = configureColumns(columns)
    toClipboard(s)

def toClipboard(x: str):
    global root
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(x)
    root.update()
    root.deiconify()

def setLoginPosition(e = None):
    cr.setLoginPos(e.x_root, e.y_root)

def main():
    cr.init()
    cr.readConfig()
    
    global root
    root = tk.Tk()
    for k in cr.getKeys():
        root.bind(f'<{k}>', lt.appLogin)
        root.bind(f'<Control-{k}>', lt.appLoginHere)
    root.bind('<s>', setLoginPosition)

    tk.Label(root, text="Nr zadania:").grid(row=0)
    global nr_zad
    nr_zad = tk.Entry(root, width = 23)
    nr_zad.grid(row = 0, column = 1, columnspan = 2)

    tk.Button(root, 
              text='Commity', 
              command=commitsFromInput).grid(row=1, 
                                        column=1)
    tk.Button(root, 
              text='PullAll', 
              command=pullAll).grid(row=1, 
                                        column=2)

    tk.Label(root, text="").grid(row = 2, column = 0)

    tk.Label(root, text="Kolumny").grid(row = 3, column = 0)
    global cols
    cols = tk.Text(root, height = 10, width = 23)
    cols.grid(row = 3, column = 1, columnspan = 2)

    tk.Button(root, 
              text='Zmień w .c()', 
              command=cFromCols).grid(row=4, 
                                        column=1)

    tk.Button(root, 
              text='Domyślny config', 
              command=confFromCols).grid(row=4, 
                                        column=2)

    tk.Label(root, text="").grid(row = 5, column = 0)

    loginKeys = ''
    for key in cr.getKeys():
        l, p = cr.getLogin(key)
        loginKeys += f'    {key} - logowanie na {l}\n'
        
    tk.Label(root,
             text='''INSTRUKCJA

    1. Commity, kolumny i konfiguracja są
    od razu skopiowane po kliknięciu

    2. Commity wyszukują po dowolnym ciągu znaków,
    ale polecam nr zadania

    3. Kolumny powinny być bez przecinków,
    jedna pod drugą żeby wszystko zadziałało

    4. Nie wpisujcie kolumn z palca, tylko wklejajcie,
    bo niektóre litery są skrótami

    5. Skróty do szybkiego logowania
    s - ustawianie i zapisanie pozycji
    (tam się przenosi myszka przed akcją)
''' + loginKeys + '''

    6. Wciśnięcie ctrl + litera pomija przenoszenie myszki''',
             justify='left').grid(row = 6, columnspan = 3)

    root.mainloop()

if __name__ == '__main__':
    main()
