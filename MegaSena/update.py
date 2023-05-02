from conectar import conexaomega, cursor


def inserir_jogos(idSorteio, dataAno, num1, num2, num3, num4, num5, num6):
    inserir_jogos = f"""insert into sorteios(idSorteio, dataAno, num1, num2, num3, num4, num5, num6)
    value
    ('{idSorteio}', '{dataAno}', '{num1}', {num2}, '{num3}', '{num4}', '{num5}', '{num6}');"""
    cursor.execute(inserir_jogos)
    conexaomega.commit()


