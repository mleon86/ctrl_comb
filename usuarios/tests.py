from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class CustomUserTest(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username = "lll",
            email = "lll@lll.com",
            password = "123"
        )

        #Que esperamos
        self.assertEqual(usr.username,"lll")
        self.assertEqual(usr.email,"lll@lll.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username = "lll",
            email = "lll@lll.com",
            password = "123"
        )

        #Que esperamos
        self.assertEqual(usr.username,"lll")
        self.assertEqual(usr.email,"lll@lll.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)