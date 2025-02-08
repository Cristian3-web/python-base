#!/c/Users/bueno/AppData/Local/Programs/Python/Python313/python

"""
hello world multi línguas.

depedendo da língua  configurada no mesmo ambiente o progama exibe correposdente.


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

current_language = "pt_BR"
msg = "hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
 elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg)
