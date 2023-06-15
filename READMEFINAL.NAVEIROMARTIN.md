1- Si no tienes el entorno virtual creado, puedes abrir el archivo requirements.txt con Visual Studio Code y hacer clic en Crear ambiente, luego elegir Venv, luego el intérprete Python (última versión).
Nota: Se le actualizaron bibliotecas en el requirements para el correcto uso del proyecto.

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

De la tercer pre entrega a esta, se le mejoro la vista en general usando etiquetas de html. Se le creo un avatar que lo podemos encotrar en el nabvar en el lado superior izq, el mismo contiene un enlace que nos devuelve a la pagina de inicio.
En el nabvar tambien encontramos un "login" que nos lleva directamente al admin de superuser donde podemos crear, modificar o eliminar cualquier producto. Tambien encontramos un enlace rapido "creador de productos" al cual ingresamos si o si con previo registro, y podemos generar un producto, en este caso automotores, con alguna foto.
En el listado de automotores tenemos un filtro que nos permite buscar por Tipo de vehiculo, marca, modelo y año. Se busco esta forma de filtrado, ya que al no haber creado funciones con claves foraneas uno puede puede poner, por ejemplo, en tipo de vehiculo, 1000 veces auto y se repetiria, me hubiese encantado hacerlo de la otra forma, pero al correr los dias y no poder ponerme de lleno con la entrega lo deje como la pre-entrega3, mil disculpas.
Los templates quienes somos y contactanos son practicamente de relleno en cuestion de funcionalidades, aunque no pueden faltar en un blog.
Por ultimo, si no me olvido de nada, en la app de copyrigth, la cual en principio fue creada para probar como se hacia, ya que si bien esto es una continuacion de la preentrega3, creo que el proyecto arranco con lo hecho en clase, alla por la clase 19/20, y se le trato de asemejar a todo lo que se fue viendo en las ultimas 5 clases que los cambios eran a pasos agigantados... Como decia, en la app de copyrigth que ingresamos desde el footer, podemos encontrar un enlace "acerca de mi" y alli encontrar algo de info personal, foto, agradecimientos, el "por que?" del formato del proyecto y las ganas de nuevos desafios!
Espero cumplir con las espectativas, y quedo a la espera de cualquier recomendacion y/o mejora que deba hacer para aprobar el proyecto. Les estoy adeudando el video, espero pronto poder armarlo y subirlo, me baje el programa pero todavia no pude investigarlo del todo.
Aprovecho nuevamente para agradecerles, a todo el equipo coder, obviamente en especial a Esteban y tutores. De todas maneras espero cruzarlos pronto, ya que estoy terminando de decidir con que curso seguir. Me han hecho descubrir practicamente un mundo nuevo y estoy ansioso por seguir explorandolo...
Saludos!

Naveiro Martin