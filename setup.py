#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.rst", "rt") as inf:
    readme = inf.read()

setup(
        name="genpy",
        version="2016.1.3",
        description="AST-based generation of Python source code",
        long_description=readme,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Other Audience',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development :: Libraries',
            'Topic :: Utilities',
            ],

        author="Andreas Kloeckner",
        author_email="inform@tiker.net",
        license="MIT",
        url="http://documen.tician.de/genpy/",

        packages=["genpy"],
        install_requires=[
            "pytools>=2015.1.2",
            "numpy>=1.6",
            ])
