from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    Extension("obfuscated_my_precious",  ["my_precious.py"]),
    # Here you can add all the modules / packages you wanna hide
]


setup(
    name='QantEv',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
