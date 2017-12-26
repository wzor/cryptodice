from setuptools import setup, find_packages

setup(
    name="CryptoDice",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    #entry_points={
        #'console_scripts': [],
        #'gui_scripts': []
    #}
    author="Mattia Terenzi",
    author_email="mterenzi@openhedge.network",
    description="A dice game based on smart contract.",
    url="http://cryptodice.github.io"
)
