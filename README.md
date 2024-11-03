# Repositorio de ejemplo de PyQt6

PyQt6 requiere versión 3.9 de Python

- Documentación oficial de Anaconda: https://docs.anaconda.com/
- Comandos de conda: https://conda.io/docs/_downloads/conda-cheatsheet.pdf

Anaconda te permite instalar varias versiones de Python en el mismo entorno, lo que es útil cuando necesitas trabajar con proyectos que requieren versiones antiguas de Python. Aquí te presento los pasos para instalar versiones antiguas de Python en Anaconda:

1. **Crear un entorno virtual**: Utiliza el comando `conda create --name <nombre_entorno> python=<versión_python>` para crear un entorno virtual con la versión de Python deseada. Por ejemplo, para crear un entorno con Python 2.7, escribe `conda create --name py27 python=2.7`.
2. **Activar el entorno virtual**: Utiliza el comando `conda activate <nombre_entorno>` para activar el entorno virtual recién creado. Por ejemplo, `conda activate py27`.
3. **Verificar la versión de Python**: Utiliza el comando `python --version` para verificar que la versión de Python deseada se ha instalado correctamente.

## **Comandos a usar en este caso**
- Instalar Python 3.9: `conda create --name calculadora python=3.9`
- Activar el entorno calculadora: `conda activate calculadora`
- Verificar la versión de Python en el entorno calculadora: `python --version`

**Nota**: Asegúrate de que Anaconda tenga acceso a las versiones antiguas de Python que deseas instalar. Puedes verificar las versiones disponibles en el repositorio de Anaconda mediante el comando `conda search python`.

### Una vez tengamos la versión correcta de Python podemos instalar PyQt6

```bash
pip install pyqt6
pip install pyqt6-tools
```

- Además, en linux, hay que ejecutar la instalación del `designer`. En Windows no es necesario.
    
    ```bash
    sudo apt-get install libqt6designer6
    ```

### Lanzar el diseñador:

```bash
pyqt6-tools designer
```

Instalar dependencias desde requirements.txt

Para instalar las dependencias listadas en el archivo requirements.txt en tu entorno virtual, puedes usar el siguiente comando:

```bash
pip install -r requirements.txt
```
