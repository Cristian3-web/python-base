"""
!usr/bin/env
hello world multi línguas.
depedendo da língua  configurada no mesmo ambiente o programa 
exibe correposdente.



Como usar:

tenha a varíavel lang devidamente configurada ex:


export LANG:pt_BR


execução:
python3 hello.py
ou ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Cristian"
__lincense__ = "Unlicense"


import os
current_language = os.getenv("LANG","en_US")[:5 ]
msg = "Hello, World!"


if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour le monde"


print(msg)
