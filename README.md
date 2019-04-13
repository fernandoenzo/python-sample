# Proyecto Sample

Con este programa de ejemplo puedes ver una plantilla básica para crear cualquier proyecto Python fácilmente instalable y sin problemas de importación.

### Empaquetamiento

Para empaquetar el programa lo primero es instalar *autopackage*, que podemos hacerlo en un virtualenv.

```
pip install autopackage
```

Tras lo cual ejecutamos la siguiente instrucción para crear un autoejecutable en la carpeta *releases* (si quitas la opción *-p* generarás un archivo *whl* instalable).

```
autopackage -s setup.py -p
```

El autoejecutable lanzará el archivo *\_\_main\_\_.py* sin más. El instalable se puede instalar fácilmente así:

```
pip install --user sample-1.0.0-py3-none-any.whl
```

Tras lo cual, podremos lanzar desde el terminal *bin1* y *bin2* sin más, que son los scripts definidos en el archivo *setup.py*

El flag **zip_safe** del archivo *setup.py* es relevante únicamente para el programa autoejecutable, no para el instalable. Lo tenemos desactivado en este caso porque estamos haciendo uso de archivos 
estáticos en el programa.