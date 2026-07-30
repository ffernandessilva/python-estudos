# ============================
# .format() usando a ordem
# ============================

a = 'AAAAA'
b = 'BBBBB'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)

print()


# ============================
# .format() usando índices
# ============================

string = 'a={1} b={0} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)

print()


# ============================
# .format() usando nomes
# ============================

string = 'a={nome1} b={nome2} c={nome3:.2f}'

formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c
)

print(formato)