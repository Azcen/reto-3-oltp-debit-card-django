# Aplicación OLTP para Tarjeta de Débito con Django

## Autores

- Daniel Alejandro Ochoa Gutierrez

## Instrucciones de Ejecución

1. Clona el repositorio o descarga los archivos.
2. Crea un entorno virtual:

   En Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   

   En macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Installa dependencias
```
pip install -r requirements.txt
```
4. Ejecuta las migraciones(en caso de no tenerlas)
```
python manage.py migrate
```
5.Ejecuta el archivo main.py
```
python manage.py runserver
```
