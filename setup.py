#!/usr/bin/env python

from distutils.core import setup

setup(name='clrxdisasm_wrapper',
      version='0.1.0',
      description='clrxdisasm wrapper for code object V4 support',
      author='Dmitry "RubyUmbra" Gromov',
      author_email='rubyumbra@gmail.com',
      url='https://github.com/RubyUmbra/clrxdisasm-wrapper-py',
      license='MIT',
      packages=['clrxdisasm_wrapper', ],
      install_requires=['argparse', 'construct', 'ormsgpack', 'pyelftools', ],
      )
