s = 0
for c in range(0, 2):
    n = int(input('Digite uma nota: '))
    s += n
    m = s/2
print(s)
print('A media das duas notas é {:.1f}\n'.format(m))
if m <=6:
    print('Reprovado\n')

else:
    print('Você foi, Aprovado!!!\n')
