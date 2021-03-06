#!/usr/bin/python
##############################################################################
#
# File:    setup.py
#
# Purpose: Driver script for the fko module.
#
# Fwknop is developed primarily by the people listed in the file 'AUTHORS'.
# Copyright (C) 2009-2014 fwknop developers and contributors. For a full
# list of contributors, see the file 'CREDITS'.
#
##############################################################################
#
from distutils.core import setup, Extension

# The fko extension module.
#
fko_ext = Extension(
    '_fko',
    define_macros = [('MAJOR_VERSION', '1'), ('MINOR_VERSION', '5')],
                    include_dirs = ['../lib/'],
                    library_dirs = ['../lib/.libs'],
                    libraries = ['fko'],
                    sources = ['fkomodule.c']
)

setup (
    name = 'fko',
    version = '1.5',
    description = 'Wrapper for Fwknop library (libfko)',
    author = 'Damien S. Stuart',
    author_email = 'dstuart@dstuart.org',
    license = 'GPL',
    long_description = '''
Python module that wraps the fwknop library to provide the ability to
generate, decode, parse, and process SPA formatted messages.
''',
    ext_modules = [fko_ext],
    py_modules = ['fko']
)

###EOF###
