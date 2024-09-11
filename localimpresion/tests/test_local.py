from django.test import TestCase, Client
from django.urls import reverse
from gestion_impresoras.models import Local
from usuarios.models import Usuario
from django.db import IntegrityError

class LocalUnitTest(TestCase):
    #creamos el objeto local de prueba 
    def setUp(self):
        Local.objects.create(
            nombre = 'Local 1',
            direccion = 'Lugar 1',
        )
    
    def test_model(self):
        # recuperamos el primer objeto de la base de datos 
        local = Local.objects.first()
        # verificamos que tenga como nombre local
        self.assertEqual(local.nombre, 'Local 1')
    
class LocalTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        # Se crea un cliente 
        self.client = Client()
        # Un usuario super admin
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')
        # se crean los locales
        Local.objects.create(
            nombre = 'Local 1',
            direccion = 'Lugar 1',
        )
        
        Local.objects.create(
            nombre = 'Local 2',
            direccion = 'Lugar 2',
        )
                
    def test_get_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_locales')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK son los estados Http
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'locales/lista_locales.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        locales_en_contexto = response.context['locales']
        self.assertEqual(len(locales_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'Local 1')
        self.assertContains(response, 'Local 2')
        
    def test_form_post(self):
        self.client.login(username='admin', password='admin')
        
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'nombre': 'Local 3',
            'direccion': 'Lugar 3',
            'usuario_encargado': self.usuario.id
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('agregar_local')
        urlr = reverse('lista_locales')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Local.objects.filter(nombre='Local 3').exists()
        self.assertTrue(objeto_creado)