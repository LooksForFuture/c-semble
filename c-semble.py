from sys import argv
from os import system
from json import loads

if len(argv) != 2:
    print('You should give the name of your project\'s json file!')
    quit(-1)

with open(argv[1]) as file:
    conf = loads(file.read())

name = conf['name']
entry = conf['entry']

include = ''
if 'include-dirs' in conf:
    includes = conf['include-dirs']
    for x in includes:
        include += ' -I "{}"'.format(x)

lib = ''
if 'lib-dirs' in conf:
    lib_dirs = conf['lib-dirs']
    for x in lib_dirs:
        lib += ' -L "{}"'.format(x)

libs = ''
if 'libs' in conf:
    lib_names = conf['libs']
    for x in lib_names:
        libs += ' -l{}'.format(x)

pre_args = ''
args = ''
if 'c++' in conf:
    pre_args += ' -std=c++{}'.format(conf['c++'])
if 'pre-args' in conf:
    pre_args += ' ' + conf['pre-args']
if 'args' in conf:
    args += ' ' + conf['args']

cmd = 'g++'
if pre_args != '':
    cmd += pre_args + ' '

cmd += '-o {} {}'.format(name, entry)

if include != '':
    cmd += include

if lib != '':
    cmd += lib

if libs != '':
    cmd += libs

if args != '':
    cmd += args

print(cmd)
system(cmd)
