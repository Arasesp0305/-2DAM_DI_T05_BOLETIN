
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Documentacion de T05_DOC_PRUEBAS'
copyright = '2025, Grupo 03'
author = 'Grupo 03'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Importamos módulos para configurar rutas y extensiones
import os  # Módulo para gestionar rutas del sistema operativo
import sys  # Módulo para modificar el path de búsqueda de Python
import sphinx_rtd_theme  # Tema para mejorar el diseño visual de la documentación

# Configurar la ruta al directorio raíz del proyecto
# os.path.abspath('../') obtiene la ruta absoluta del directorio superior al actual
# sys.path.insert(0, ...) añade esta ruta al inicio de sys.path, que es donde Python busca los módulos
sys.path.insert(0, os.path.abspath('../'))


# Lista de extensiones activadas en Sphinx
extensions = [
    'sphinx.ext.autodoc',  # Genera documentación automáticamente desde docstrings
    'sphinx.ext.napoleon',  # Interpreta docstrings en formatos Google y NumPy
    'sphinx.ext.viewcode',  # Agrega enlaces al código fuente desde la documentación
    'sphinx_rtd_theme',  # Tema visual basado en Read the Docs
    'myst_parser',  # Habilita soporte para archivos Markdown
]

# Ruta de las plantillas personalizadas
templates_path = ['_templates']

# Patrón para excluir ciertos archivos o directorios de la generación de la documentación
exclude_patterns = []

# Configuración del idioma de la documentación
language = 'es'  # Idioma español

# Configuración para soportar múltiples tipos de archivos fuente
source_suffix = {
    '.rst': 'restructuredtext',  # Archivos en formato reStructuredText
    '.md': 'markdown',  # Archivos en formato Markdown
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Tema visual para la salida HTML
html_theme = 'sphinx_rtd_theme'

# Directorio para recursos estáticos personalizados (CSS, JS, imágenes, etc.)
html_static_path = ['_static']