from setuptools import setup

setup(
    name='foobar',
    version='1.0',
    author='Author',
    packages=['foobar'],
    description='Description',
    package_data={'': ['*.txt', '*.yaml']},
    install_requires=['requests', 'bs4', 'sqlalchemy'],
    entry_points={'console_scripts': ['foobar = foobar.foobaz:main']}
)
