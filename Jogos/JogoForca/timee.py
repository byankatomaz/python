from threading import Timer
import os


def start_thread():
    tempoini = Timer(30, Termino)
    tempoini.start()
    return tempoini


def cancel_thread(tempoini):
    tempoini.cancel()


def Termino():
    print('\nAcabou o seu tempo!!')
    pid = os.getpid()
    os.kill(pid, 0)


def start_thread2():
    tempoini2 = Timer(20, Termino)
    tempoini2.start()
    return tempoini2


def cancel_thread2(tempoini2):
    tempoini2.cancel()


def Termino3():
    print('\nAcabou o seu tempo!!')
    pid = os.getpid()
    os.kill(pid, 0)
