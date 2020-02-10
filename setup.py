#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from pathlib import Path

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = Path('requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Taher Chegini",
    author_email='cheginit@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Hydrodata downloads climate data for a USGS station as well as land use, land cover data for the corresponding watershed.",
    entry_points={
        'console_scripts': [
            'hydrodata=hydrodata.cli:main',
        ],
    },
    install_requires=read_requirements(),
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hydrodata',
    name='hydrodata',
    packages=find_packages(include=['hydrodata', 'hydrodata.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cheginit/hydrodata',
    version='0.2.0',
    zip_safe=False,
)
