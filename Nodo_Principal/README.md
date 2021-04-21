# Nodo Principal

### Primero se crea un entorno virtual 
```
python -m venv venv
```

### Se activa el entorno virtual
```
venv\Scripts\activate
```

### Se instalan algunas dependencias necesarias
```
pip install requests lxml autopep8
```

### Se actualiza pip
```
python -m pip install pip --upgrade
```

### Beautifulsoup4
```
pip install beautifulsoup4
```

### Selenium
```
pip install selenium
```

### Verificamos las dependencias del proyecto
```
pip freeze
```

## Selenium necesita un driver para poder generar una interfaz con el navegador. Dependiendo el navegador que uses, deberás descargar un driver distinto. Acá te dejo un listado de los links de descarga para los distintos navegadores. Asegurate de descargar el que corresponda con la versión de tu navegador:

- **Chrome**: https://sites.google.com/a/chromium.org/chromedriver/downloads

- **Edge**: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

- **Firefox**: https://github.com/mozilla/geckodriver/releases

- **Safari**: https://webkit.org/blog/6900/webdriver-support-in-safari-10/