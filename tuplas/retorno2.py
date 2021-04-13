from collections import namedtuple


def minha_lista():
    MyList = namedtuple('Compra', 'frutas local supermercados extras')
    return MyList(
        frutas=["maca", "uva", "abacate"],
        local=["rua do jasmin"],
        supermercados=2,
        extras={"doces": "chocolates", "sucos": "maracuja"}
    )


def minha_lista2():
    MyList = namedtuple('Compra', 'frutas local supermercados extras')
    return MyList(
        frutas=["maca", "uva", "abacate"],
        local=["rua das laranjeiras"],
        supermercados=2,
        extras={"doces": "chocolates", "sucos": "Morango"}
    )


lista = minha_lista()
lista2 = minha_lista2()
print(lista)
print(lista2)

