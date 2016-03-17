#! /usr/bin/python

import os
import yaml
from subprocess import call
import argparse

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument(
    'spec', help='Specification for pyenv virtual environment.')
args = parser.parse_args()
specfile = os.path.abspath(args.spec)
location = os.path.dirname(specfile)

spec = yaml.load(file(specfile, 'r').read())
spec['location'] = location
spec['py_env'] = '-'.join(
    [spec['package'], spec['version'], 'py' + spec['py_version']])
spec['requirement_list'] = ' '.join(spec['requirements'])
spec['lib_list'] = ' '.join(spec['libs'])

builder_script = file(
    os.path.join(BASE_DIR, 'builder_template.sh'), 'r').read().format(**spec)

p = call(builder_script, shell=True)
