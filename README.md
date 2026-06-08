# Laboratorio 09 - Django

## Descripción

Implementación de:

- Relación Uno a Muchos (ForeignKey)
- Relación Muchos a Muchos (ManyToManyField)
- Generación de PDF con xhtml2pdf
- Envío de correos electrónicos con Django

## Tecnologías utilizadas

- Python
- Django
- SQLite
- xhtml2pdf
- Git y GitHub

## Instalación

```bash
git clone <URL_DEL_REPOSITORIO>
cd laboratorio09
python -m venv env
source env/Scripts/activate
pip install django xhtml2pdf
python manage.py migrate
python manage.py runserver
