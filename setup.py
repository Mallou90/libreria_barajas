# Este archivo setup.py se utiliza para empaquetar la librería

from setuptools import setup, find_packages

setup(
    name="barajas",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="David Mallou",
    author_email="davidmallouacebal@gmail.com",
    description="Una librería de barajas de cartas para Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mallou90/proyecto_barajas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 