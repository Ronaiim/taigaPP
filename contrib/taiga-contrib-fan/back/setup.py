#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="taiga-contrib-fan",
    version="0.0.1",
    description="The Taiga plugin for list projects which user is fan",
    long_description="",
    keywords="taiga, project, fan",
    author="Simon Leblanc",
    author_email="contact@leblanc-simon.eu",
    url="https://github.com/leblanc-simon",
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)

