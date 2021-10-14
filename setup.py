from setuptools import setup

setup(name='dev_aberto_brunoacpc',
    version='0.1',
    packages=['dev_aberto'],
    scripts=['scripts/hello.py'],
    install_requires=[
        'requests',
        'babel'
    ]
)