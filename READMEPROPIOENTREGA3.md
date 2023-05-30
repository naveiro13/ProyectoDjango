1- Si no tienes el entorno virtual creado, puedes abrir el archivo requirements.txt con Visual Studio Code y hacer clic en Crear ambiente, luego elegir Venv, luego el intérprete Python (última versión).

2-
Migraciones
python manage.py makemigrations

Crea las migraciones, que son archivos Python encargados de la base de datos

python manage.py migrate

Ejecuta las migraciones, para que se realicen los cambios en la base de datos

3-
python manage.py createsuperuser

Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

4-
Servidor
python manage.py runserver
(Ejecutado el servidor. Para pararlo: control + c (cmd + c en Mac))

NOTA: Por falta de tiempo disponible y no dejar de entregar el trabajo, tuve que dejar la plantilla de bootstrap, inclusive las dos app ya creadas en clase.
En la de "productos" genere una formulario que cree al producto, en mi caso seria un automotor. Y en la de "ventas" se ve reflejado los productos ingresados.
Modifique los parrafos y la imagen a modo de vista y para practicar su funcionamiento.
Por ultimo cree una nueva app, llamada copyrigth, entiendo que no es de demasiada utilidad, ya que solo dirige a un parrafo (tendria que haber sido solo un html nuevo, pero fue para crear una app desde consola y ver que pasaba si tocaba el footer).
Espero cumplir con los objetivos, aunque me quedo en la cabeza cuando el profe dijo "que tratemos de desafiarnos a nosotros mismos". No le eh podido dedicar el tiempo que se merece, este finde largo estuve tapado de trabajo, creo que en los commits figura que las modificaciones se produjeron el martes a la madrugada, fue todo el tiempo que le pude dedicar. De ser necesario podria modificar o mejorarlo, sino, pondre lo mejor de mi para mejorar el proyecto final.

