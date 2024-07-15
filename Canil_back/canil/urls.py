from django.urls import path
from canil.views import submit_form


urlpatterns = [
   path('api/submit/', submit_form, name='submit_form'),

]