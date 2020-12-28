# Response Whatsapp Bot

Este bot responde a mensajes entrantes de Whatsapp

Hay que descargar el driver de la siguiente pagina y ubicarla en la carpeta del proyecto
https://sites.google.com/a/chromium.org/chromedriver/downloads

## Instalación de ChatterBot

Para instalar ChatterBot en MacOS Catalina tuve que descargarlo desde github https://github.com/gunthercox/ChatterBot e instalarlo con el comando python setup.py install estando dentro del entorno virutal.

ChatterBot utiliza una dependencia llamada spacy que al parecer el proyecto instalado anteriormente no lo instala, por lo que tuve que instalarlo manualmente a como lo especifica la pagina oficial de [spaCy](https://spacy.io/usage):

```
$ pip install -U pip setuptools wheel
$ pip install -U spacy
```

Tambien es necesario un modulo de spacy que encontre las instrucciones en https://clay-atlas.com/us/blog/2020/05/12/python-en-package-spacy-error/ y basicamente es utilizar el modulo spacy para instalarla:

```
$ sudo python3 -m spacy download en
```

Nota: Tuve que reiniciar la terminal.

Descargar chatterbot_corpus y ubicarlos en el directorio del home que es como un diccionario de IA para diferentes lenguajes.
