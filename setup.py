from setuptools import setup, find_packages
setup(
   name='clishit',
   version='0.5',
   packages=find_packages(),
   install_requires=[
      'click','art',
   ],
   entry_points='''
      [console_scripts]
      namecall2=clishit.cli.namecall2:hello
      ''',
)