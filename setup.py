from setuptools import setup


setup(name='strong-mnemonic-passwords',
      version='0.1',
      description='Mnemonic (pronounceable) password generator',
      long_description='Generator for pronounceable passwords with reminder phrases that are fairly simple to memorize.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Office/Business :: Security'
      ],
      keywords='password mnemonic security',
      url='https://github.com/codiersklave/python-mnemonic-passwords',
      author='codiersklave',
      author_email='codiersklave@yahoo.de',
      license='MIT',
      packages=['mnemonic_passwords'],
      install_requires=['num2words', 'pyperclip'],
      zip_safe=False,
      entry_points={'console_scripts': [
          'new-password=mnemonic_passwords.cli:one_password',
          'new-passwords=mnemonic_passwords.cli:many_passwords'
      ]})
