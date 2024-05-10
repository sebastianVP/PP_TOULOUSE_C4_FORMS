# Comandos de Proyecto

* Instalar o crear el entorno virtual.
* Ubicados en el directorio  C:\Users\soporte\Documents\PP_TOULOUSE_C4\PP_TOULOUSE_C4_FORMS
* conda create -n app_pp_c4 python=3.11
* conda activate app_pp_c4
* pip install -r requirements.txt
* django-admin startporject mysite
* Ubicados en el directorio  C:\Users\soporte\Documents\PP_TOULOUSE_C4\PP_TOULOUSE_C4_FORMS\mysite
* python manage.py startapp forms
* Añadir forms dentro de INSTALLED_APPS en settings.py
* Eliminamos comentarios e importamos include y creamos el path hacia los urls de nuestra app forms. Le diremos a la aplicación que al no leer ningún path en el navegador, se dirija a algún url que definiremos más adelante dentro de urls.py de la carpeta forms.
* Para propósitos del tutorial, más adelante crearemos un modelo de “Usuarios” para guardar la información que enviemos en los posts de nuestros forms en la base de datos.
* En la carpeta forms, creamos una carpeta templates y dentro de esta, una carpeta llamada forms (en django es buena práctica crear nuestros html templates así).
* Dentro de forms/templates/forms/ creamos un archivo llamado mi_form.html que se encargará de mostrar nuestra form y todos los Usuarios que vayamos creando.
* En la carpeta forms en el archivo views.py creamos nuestra view llamada index.
