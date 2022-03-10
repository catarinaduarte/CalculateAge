

from datetime import date

hoje = date.today()
data_nasc = input("Introduza ano, mes e dia de nascimento separados por um espaço: ")
data_nasc = data_nasc.split()
ano_nasc = int(data_nasc[0])
mes_nasc = int(data_nasc[1])
dia_nasc = int(data_nasc[2])

# Alternativamente:
#   ano_nasc, mes_nasc, dia_nasc = [int(p) for p in data_nasc.split()]

idade = hoje.year - ano_nasc
if hoje.month < mes_nasc or hoje.month == mes_nasc and hoje.day < dia_nasc:
    idade -= 1
print(f"Idade: {idade} anos")

# a -= 3   <=>   a = a - 3
# idade -= (hoje.month < mes_nasc or hoje.month == mes_nasc and hoje.day < dia_nasc)