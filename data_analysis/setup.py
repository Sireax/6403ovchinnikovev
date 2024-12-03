from setuptools import setup, find_packages

setup(
    name='Distutils',
    version='1.0',
    description='python lab2',
    author='OvchinnikovEV',
    author_email='ee.ovchinnikov@yandex.ru',
    url='https://github.com/Sireax/6403ovchinnikovev',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
        'numpy',
        'jupyterlab',
    ],
    python_requires='>=3.12',
)
