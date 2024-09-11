from django.test import TestCase, Client
from django.urls import reverse
from gestion_impresoras.models import Local, Impresora
from usuarios.models import Usuario
from django.db import IntegrityError

class ImpresoraUnitTest(TestCase):
    def setUp(self):
        local = Local.objects.create(
            nombre = 'Local 1',
            direccion = 'Lugar 1',
        )
    
        Impresora.objects.create(
                nombre = 'Impresora 1',
                tipo_conexion = 'USB',
                descripcion = 'Descripcion 1',
                localizacion = 'Lugar 1',
                marca = "Marca 1",
                modelo_fabricacion = 'Modelo 1',
                local = local
        )
        
    def test_model(self):
        # Configura el objeto de prueba
        impresora = Impresora.objects.first()
        self.assertEqual(impresora.nombre, 'Impresora 1')
        
    def test_impresora_sin_local(self):
        with self.assertRaises(IntegrityError):
            Impresora.objects.create(
                nombre = 'Impresora sin local',
                tipo_conexion = 'USB',
                descripcion = 'Descripcion 2',
                localizacion = 'Lugar 2',
                marca = "Marca 2",
                modelo_fabricacion = 'Modelo 2',
                #local = local.id
            )

class ImpresoraTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.client = Client()
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')
        
        local = Local.objects.create(
            nombre = 'Local 1',
            direccion = 'Lugar 1',
        )
                
        Impresora.objects.create(
                nombre = 'Impresora 2',
                tipo_conexion = 'USB',
                descripcion = 'Descripcion 2',
                localizacion = 'Lugar 2',
                marca = "Marca 2",
                modelo_fabricacion = 'Modelo 2',
                local = local
        )
        
        Impresora.objects.create(
                nombre = 'Impresora 1',
                tipo_conexion = 'USB',
                descripcion = 'Descripcion 1',
                localizacion = 'Lugar 1',
                marca = "Marca 1",
                modelo_fabricacion = 'Modelo 1',
                local = local
        )
                
    def test_get_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_impresoras')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'impresoras/lista_impresoras.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        impresoras_en_contexto = response.context['impresoras']
        self.assertEqual(len(impresoras_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'Impresora 1')
        self.assertContains(response, 'Impresora 2')
        
    def test_form_post(self):
        self.client.login(username='admin', password='admin')
        local = Local.objects.first()
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'nombre' : 'Impresora 4',
            'tipo_conexion' : 'USB',
            'descripcion' : 'Descripcion 4',
            'localizacion' : 'Lugar 4',
            'marca' : "Marca 4",
            'modelo_fabricacion' : 'Modelo 4',
            'local' : local.id
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('agregar_impresora')
        urlr = reverse('lista_impresoras')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Impresora.objects.filter(nombre='Impresora 4').exists()
        self.assertTrue(objeto_creado)