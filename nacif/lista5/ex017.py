numPedido=1
data=0
preco=0
quantidade=0
valorCompra=0
while(numPedido!=0):
    numPedido = int(input())
    if(numPedido!=0):
        data = int(input())
        preco = float(input())
        quantidade = int(input())
        valorCompra += preco * quantidade
print(valorCompra)