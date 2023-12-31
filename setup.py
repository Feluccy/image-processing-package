from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    

setup(
    name='image-processing-package',
    version='0.0.3',
    author='Fernanda Lucio',
    author_email='feluccy@hotmail.com',
    description='Pacote criado durante o bootcamp Python Developer da DIO',
    long_description= page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Feluccy/image-processing-package.git',
    packages= find_packages(),
    install_requires = requirements,
    python_requires = '>=3.8'
    
)