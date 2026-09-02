print('Digite o Coeficiente A.')
coA=float(input())
print('Digite o Coeficiente B.')
coB=float(input())
print('Digite o Coeficiente C.')
coC=float(input())
delta=(coB**2)-(4*coA*coC)
if delta==0 :
    print('A única raiz é ' + str((coB*-1)/(2*coA)) + '.')
elif delta<0 :
    print('Não há raiz real.')
else:
    print('A primeira raiz é ' + str(((coB*-1)+(delta**0.5))/(2*coA)) + '.')
    print('A segunda raiz é ' + str(((coB*-1)-(delta**0.5))/(2*coA)) + '.')