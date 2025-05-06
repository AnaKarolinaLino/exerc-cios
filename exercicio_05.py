def cadastrar_aluno(nome, email, serie):
    
    alunos = []

    aluno =  {
        "nome": nome,
        "email": email,
        "serie": serie
    }
    alunos.append(aluno)
    return alunos

print(cadastrar_aluno("Ana Karolina", "00001129651459sp@al.educacao.sp.gov.br", "2TB"))