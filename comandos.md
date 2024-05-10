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
* Creando el modelo que guardará los datos de los Usuarios:  En la carpeta forms, en el archivo models.py
* Después de la creación de nuestro modelo, realizamos las migraciones:
* python manage.py makemigrations
* python manage.py migrate
* Con estos comandos ya tenemos nuestra base de datos db.sqlite3 en nuestro proyecto lista para usarse. Ahora sí!! Creamos nuestro form: Dentro de la carpeta forms, creamos un archivo forms.py
* En esta parte del código, (gracias a Django) le estamos diciendo al html que por cada variable (field) que declaramos en nuestra form (en forms.py), tiene que mostrar e variable como un <input> con su respectiva <label>. También vemos el {% csrf_token %} que es una llave que utiliza Django para protegernos de Cross Site Request Forgery.
* Aregando Django widgets a nuestros inputs:  Para evitar que nuestro <input> de fecha sea un type=”text”, tenemos que agregarle un widget a las variables de nuestra form. Modificamos nuestro archivo forms.py (de la carpeta forms) para que cada variable (input) tenga un widget del tipo que corresponda:
* Ya quedó!!! Estilo y estructura!  Pero… ¿qué hacemos con la información de la form?, ¿cómo la guardamos en la base de datos?
* A continuación, mostraré cómo podemos guardar la información de nuestra form con una función declarada dentro de su estructura. Primero importamos datetime (para trabajar con fechas) y definimos esta función: