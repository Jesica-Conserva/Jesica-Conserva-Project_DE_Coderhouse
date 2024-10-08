# Jesica-Conserva-Project_DE_Coderhouse

## Forma de ejecución

Los pasos a seguir para ejecutar el aplicativo son:

- Se debe modificar los datos en .env.template:

DB_NAME=<< nombre de la base de datos>>
DB_USER=<< nombre de usuario de la base de datos>>
DB_PASSWORD=<< contraseña del usuario para ingresar a la base de datos >>
DB_HOST= <<  servidor donde se encuentra ubicada la base de datos>>
DB_PORT= << puerto para ingresar a Amazon Redshift. Por defecto, es el nro 5439>>
ALERT_EMAIL= << email que recibirá las alertas>>

 con el fin de poder ingresar y correr el script.
- Levantar el contenedor situado en la carpeta raíz del proyecto (docker compose up )
- Ya que la imagen de Airflow utilizada es una versión standalone, la misma brinda una contraseña con el fin de autenticarse en la UI; esa contraseña será visible en los logs del contenedor.
- La UI sirve por defecto en http://localhost:8080 (el nombre de usuario es admin; definido en el script del file start.sh)
- Una vez ingresado en la UI, reanudar el DAG definido como *'daily_script_execution'* o dispararlo manualmente.

## Alertas
-La aplicación tiene un sistema de alertas que informa el resultado; ya sea correcto o incorrecto, de la ejecución del DAG mediante envío de emails. 
-En el archivo ./config/airflow.cfg se encuentran las configuraciones del servidor SMTP. Deberán ser reemplazadas con las del servidor SMTP que sea utilizado.