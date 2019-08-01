from setuptools import setup

setup(
    name='tagcounter',
    version='1.0',
    author='Domioedition',
    packages=['tagcounter'],
    description='Count tags application',
    package_data={'': ['*.yaml']},
    install_requires=['requests', 'bs4', 'sqlalchemy'],
    entry_points={'console_scripts': ['tagcounter = tagcounter.tagcounter:main']}
)
