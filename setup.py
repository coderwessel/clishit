from setuptools import setup, find_packages
setup(
   name='clishit',
   version='0.1',
   packages=find_packages(),
   install_requires=[
      'click',
   ],
   entry_points='''
      [console_scripts]
      namecall2=clishit.namecall2:hello
      ''',
)