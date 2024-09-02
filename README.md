# Jesica-Conserva-Project_DE_Coderhouse

## Forma de ejecución

Los pasos a seguir para ejecutar el aplicativo son:

- Levantar el contenedor situado en la carpeta raíz del proyecto (docker compose up )
- Ya que la imagen de Airflow utilizada es una versión standalone, la misma brinda una contraseña con el fin de autenticarse en la UI; esa contraseña será visible en los logs del contenedor.
- La UI sirve por defecto en http://localhost:8080 (el nombre de usuario es admin; definido en el script del file start.sh)
- Una vez ingresado en la UI, reanudar el DAG definido como *'daily_script_execution'* o dispararlo manualmente.