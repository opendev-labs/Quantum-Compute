from setuptools import setup, find_packages

setup(
    name="quantum-compute",
    version="0.1.0",
    description="Foundational Quantum Computing Library for Opendev Labs",
    author="Opendev Labs",
    packages=find_packages(),
    install_requires=[
        "pennylane>=0.30.0",
        "numpy",
        "torch"
    ],
    python_requires=">=3.8",
)
