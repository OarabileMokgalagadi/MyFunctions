from setuptools import setup, find_packages

setup(
    name='Hackathon Project',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My hackathon project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<oarabile96>/<Hackathon Project>',
    author='<Oarabile Mokgalagadi>',
    author_email='<oarabilemokgalagadi@g@gmail.com>'
)
