import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from config import ROOTDIR, EXCLUDE


ext_modules = [
    #Extension("obfuscated_my_precious",  ["my_precious.py"]),
    Extension("main_optim", ["main_optim.py"])
    # Here you can add all the modules / packages you wanna hide
]

for root, subdirs, files in os.walk(ROOTDIR):
    for file_name in files:
        if file_name[-3:]==".py" and file_name not in EXCLUDE:
            file_to_change = root+'/'+file_name
            new_file_name = file_to_change[:-3]
            new_file_name = new_file_name.replace('/', '.')
            ext_modules.append(Extension(new_file_name, [file_to_change]))


# See the command in the Docker file
setup(
    name='QantEv',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
