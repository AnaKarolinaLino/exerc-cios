def cadastrar_aluno(nome, email, serie, nota01, nota02, nota03):
    
    alunos = []

    aluno =  {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": [nota01, nota02, nota03]
    }
    alunos.append(aluno)
    return alunos

print(cadastrar_aluno("Ana Karolina", "00001129651459sp@al.educacao.sp.gov.br", "2TB", 7, 9, 10))

