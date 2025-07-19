import os
import django

# Configura Django con el nombre correcto del módulo de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.erp.models import Category

data = [
    'Leche y derivados',
    'Carnes, pescados y huevos',
    'Patatas, legumbres, frutos secos',
    'Verduras y Hortalizas',
    'Frutas',
    'Cereales y derivados, azúcar y dulces',
    'Grasas, aceite y mantequilla'
]

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))
