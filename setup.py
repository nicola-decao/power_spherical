import os
from setuptools import setup
from setuptools import find_packages

setup(
    name="power_spherical",
    version="0.1.0",
    author="Nicola De Cao",
    author_email="nicola.decao@gmail.com",
    description="Pytorch implementation of the Power Spherical distribution",
    license="MIT",
    keywords="pytorch machine-learning deep-learning manifold-learning",
    url="https://nicola-decao.github.io",
    download_url="https://github.com/nicola-decao/power_spherical",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    install_requires=["torch>=1.5.0"],
    packages=find_packages(),
)
