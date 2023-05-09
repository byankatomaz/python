from conectar import conexaomagazine, cursor


def inserir_xiaomi(Model, valor):
    inserir_xiiaomi = f"""INSERT INTO xiaomi(Model, valor) 
    VALUES 
    ('{Model}', '{valor}');"""
    cursor.execute(inserir_xiiaomi)
    conexaomagazine.commit()


def inserir_apple(Model, valor):
    inserir_applle = f"""INSERT INTO apple(Model, valor) 
    VALUES 
    ('{Model}', '{valor}');"""
    cursor.execute(inserir_applle)
    conexaomagazine.commit()


def inserir_motorola(Model, valor):
    inserir_motto = f"""INSERT INTO motorola(Model, valor) 
    VALUES 
    ('{Model}', '{valor}');"""
    cursor.execute(inserir_motto)
    conexaomagazine.commit()


def inserir_lg(Model, valor):
    inserir_llg = f"""INSERT INTO lg(Model, valor) 
    VALUES 
    ('{Model}', '{valor}');"""
    cursor.execute(inserir_llg)
    conexaomagazine.commit()


def inserir_samsung(Model, valor):
    inserir_sam = f"""INSERT INTO samsung(Model, valor) 
    VALUES 
    ('{Model}', '{valor}');"""
    cursor.execute(inserir_sam)
    conexaomagazine.commit()