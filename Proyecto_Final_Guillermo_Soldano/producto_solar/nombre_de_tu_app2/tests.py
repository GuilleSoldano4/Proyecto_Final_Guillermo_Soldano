from django.test import TestCase
from django.contrib.auth import get_user_model

class UsuarioTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(username='usuario_test', email='test@example.com', password='password123')

    def test_usuario_creacion(self):
        User = get_user_model()
        usuario = User.objects.get(username='usuario_test')
        self.assertEqual(usuario.email, 'test@example.com')
        self.assertTrue(usuario.check_password('password123'))
