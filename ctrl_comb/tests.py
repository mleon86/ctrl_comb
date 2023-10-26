from django.test import TestCase
from django.urls import reverse
from .models import Mark, Modelo


class ModeloTests(TestCase):
    @classmethod
    def setUpTestData(clase):
        clase.modelo = Modelo.objects.create(
            mark = Mark.objects.create(descript = "Toyota"),
            descript = "Rush"
        )
    
    def test_lista(self):
        self.assertEqual(self.modelo.descript, "Rush")
        self.assertEqual(self.modelo.mark.descript, "Toyota")


    def test_vista_modal(self):
        response = self.client.get(reverse("control:modelo_edit_modal", kwargs={'pk':self.modelo.id}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Rush")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")
    

    def test_vista_modelo(self):
        response = self.client.get(reverse("control:modelo_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Rush")
        self.assertTemplateUsed(response, "ctrl_comb/modelo.html") 


    def test_vista_mark(self):
        response = self.client.get(reverse("control:mark_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Toyota")
        self.assertTemplateUsed(response, "ctrl_comb/mark.html") 

    def test_crear_modelo_por_el_modal(self):
        response = self.client.get(reverse("control:modelo_new_modal"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Modal title")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")
        
        #sabemos que hay un solo elemento
        self.assertEqual(Modelo.objects.count(),1)
        
        #Creamos lo que se enviará por POST
        mark_pk = Mark.objects.get(pk=1).pk
        data = {
            "mark": mark_pk,
            "descript":"ookkr"
        }
        #lo enviamos por post
        response = self.client.post(reverse("control:modelo_new_modal"), data=data)
        
        #verificamos que nos redirecciona a otra pagina
        self.assertEqual(response.status_code, 302)
        
        #verificamos que ya hay dos elementos en la bd de test
        self.assertEqual(Modelo.objects.count(),2)

        