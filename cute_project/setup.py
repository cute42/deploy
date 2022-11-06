#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Andreas Felix Haeberle",
    author_email='andreasfelixhaeberle@gmail.com',
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
    description="cute little project - cute?",
    entry_points={
        'console_scripts': [
            'cute_project=cute_project.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cute_project',
    name='cute_project',
    packages=find_packages(include=['cute_project', 'cute_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/42sol-eu/cute_project',
    version='2022.01',
    zip_safe=False,
)
