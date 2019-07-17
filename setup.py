from __future__ import absolute_import, print_function 

from setuptools import setup, Extension, find_packages
from pkg_resources import resource_filename

import os
import sys

# Specify genomicsdb install location via "--with-genomicsdb=<genomicsdb_install_path>" command line arg
GENOMICSDB_INSTALL_PATH="/usr/local"
args = sys.argv[:]
for arg in args:
	if arg.find('--with-genomicsdb=') == 0:
		GENOMICSDB_INSTALL_PATH = os.path.expanduser(arg.split('=')[1])
		sys.argv.remove(arg)

GENOMICSDB_INCLUDE_DIR = os.path.join(GENOMICSDB_INSTALL_PATH, "include")
GENOMICSDB_LIB_DIR = os.path.join(GENOMICSDB_INSTALL_PATH, "lib")
		
genomicsdb_extension=Extension(
	"genomicsdb",
	language="c++",
	sources=["src/genomicsdb.pyx", "src/genomicsdb_processor.cpp"],
	libraries=["tiledbgenomicsdb"],
	include_dirs=[GENOMICSDB_INCLUDE_DIR],
	library_dirs=[GENOMICSDB_LIB_DIR],
	extra_compile_args=["-std=c++11"]
)

setup(name='genomicsdb',
	description='Experimental Python Bindings to GenomicsDB',
	author='ODA Automation Inc.',
	license='MIT',
	ext_modules=[genomicsdb_extension], 
	setup_requires=['cython>=0.27'],
	install_requires=[
		'numpy>=1.7',
		'wheel>=0.30'],
	packages = find_packages(),
	keywords=['genomics', 'genomicsdb', 'variant'],
	classifiers=[
		'Development Status :: Experimental - pre Alpha',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: POSIX :: Linux',
		'Operating System :: MacOS :: MacOS X',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
)
