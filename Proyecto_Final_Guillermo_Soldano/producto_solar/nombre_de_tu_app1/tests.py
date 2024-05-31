from django.test import TestCase
from .models import ProductoSolar

class ProductoSolarTestCase(TestCase):
    def setUp(self):
        ProductoSolar.objects.create(nombre="Panel Solar", descripcion="Panel solar de alta eficiencia", precio=299.99, stock=10)
        ProductoSolar.objects.create(nombre="Batería Solar", descripcion="Batería para almacenamiento de energía solar", precio=199.99, stock=5)

    def test_productos_solar(self):
        panel = ProductoSolar.objects.get(nombre="Panel Solar")
        bateria = ProductoSolar.objects.get(nombre="Batería Solar")
        self.assertEqual(panel.descripcion, "Panel solar de alta eficiencia")
        self.assertEqual(bateria.precio, 199.99)
