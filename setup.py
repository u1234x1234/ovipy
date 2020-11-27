import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ipyov",
    version="0.0.1",
    author="u1234x1234",
    author_email="u1234x1234@gmail.com",
    description=("ipyov"),
    license="MIT",
    keywords="",
    url="https://github.com/u1234x1234/ipyov",
    packages=["ipyov"],
    zip_safe=False,
    install_requires=["PyQt5>=5", "PyQtWebEngine>=5", "pandas>=1"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    scripts=["bin/read_file_ipyov"],
)
