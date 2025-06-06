# Este archivo setup.py se utiliza para empaquetar la librería


from setuptools import setup, find_packages

setup(
    name="baraja",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author="David Mallou Acebal",
    description="Una librería de ejemplo para sacar una carta de la baraja española",
    python_requires=">=3.9"
)