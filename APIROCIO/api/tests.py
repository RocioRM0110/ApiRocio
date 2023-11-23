# En tu archivo tests.py dentro de la aplicación que contiene tus modelos (por ejemplo, mi_app/tests.py)

from django.test import TestCase
from .models import Registro, Preguntas

class RegistroModelTest(TestCase):
    def setUp(self):
        Registro.objects.create(
            idRegistro=1,
            usuario='ejemplo_usuario',
            correo='usuario@example.com',
            password='secreto123'
        )

    def test_registro_str(self):
        registro = Registro.objects.get(idRegistro=1)
        self.assertEqual(str(registro), f'{registro.usuario} ({registro.correo})')

class PreguntasModelTest(TestCase):
    def setUp(self):
        Preguntas.objects.create(
            id_respuesta=1,
            descripcion='Pregunta 1',
            descripcion1='Pregunta 2',
            # ... completar con valores para las otras descripciones
        )

# tests.py



class PreguntasModelTest(TestCase):
    def test_preguntas_str(self):
        pregunta = Preguntas.objects.create(
            id_respuesta=1,
            descripcion='Pregunta 1',
            descripcion1='Pregunta 2',
            # ... completar con valores para las otras descripciones
        )
        self.assertEqual(str(pregunta), 'Pregunta 1')
