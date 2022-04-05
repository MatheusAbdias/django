def validete_cpf(cpf):
    return len(cpf) == 11

def validate_nome(nome):
    return nome.isalpha()   

def validate_rg(rg):
    return len(rg) != 9
