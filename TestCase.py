import unittest
import collections
from OrdenaPedidos import ordenaPedidos

class MyTestCase(unittest.TestCase):
    def test_ordenacao(self):
        precos = [25,30,40,50,60]
        fretes = [20,25,40,45,50]
        totais = [50,60,70,100,105]
        resultado = collections.OrderedDict()
        item1 = collections.OrderedDict()
        item2 = collections.OrderedDict()
        item3 = collections.OrderedDict()
        item4 = collections.OrderedDict()
        item5 = collections.OrderedDict()
        item1["frete"] = 25
        item1["preco_itens"] =  25
        item1["total"] = 50
        resultado["pedido1"] = item1
        item2["frete"] = 20
        item2["preco_itens"] =  40
        item2["total"] = 60
        resultado["pedido2"] = item2
        item3["frete"] = 40
        item3["preco_itens"] =  30
        item3["total"] = 70
        resultado["pedido3"] = item3
        item4["frete"] = 50
        item4["preco_itens"] =  50
        item4["total"] = 100
        resultado["pedido4"] = item4
        item5["frete"] = 45
        item5["preco_itens"] =  60
        item5["total"] = 105
        resultado["pedido5"] = item5

        self.assertEqual(ordenaPedidos(precos,fretes,totais), resultado)

if __name__ == '__main__':
    unittest.main()
