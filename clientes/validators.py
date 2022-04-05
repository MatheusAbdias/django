import re
from validate_docbr import CPF

def validete_cpf(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)

def validate_nome(nome):
    return nome.isalpha()   

def validate_rg(rg):
    return len(rg) == 9

def validate_celular(celular):
    """Verfica se o celular é valido"""
    exemple = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response =  re.findall(exemple, celular)
    return response