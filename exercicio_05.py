from exercicio_04 import somar_numeros

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    
    alunos = []

    notas =  [nota01, nota02, nota03]

    aluno =  {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": somar_numeros(notas)
    }
    alunos.append(aluno)
    
    return alunos

print(cadastrar_aluno("Ana Karolina", "00001129651459sp@al.educacao.sp.gov.br", "2TB", 10, 2, 9))

