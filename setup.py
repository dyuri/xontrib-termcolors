#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-termcolors',
    version='0.2.0',
    license='MIT',
    author='Gyuri Horak',
    author_email='dyuri@horak.hu',
    description="Set terminal colors based on selected xonsh theme.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py']},
    platforms='any',
    url='https://github.com/dyuri/xontrib-termcolors',
    project_urls={
        "Documentation": "https://github.com/dyuri/xontrib-termcolors/blob/master/README.md",
        "Code": "https://github.com/dyuri/xontrib-termcolors",
        "Issue tracker": "https://github.com/dyuri/xontrib-termcolors/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
