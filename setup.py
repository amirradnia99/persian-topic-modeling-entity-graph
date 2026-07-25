from setuptools import setup, find_packages

setup(
    name="persian-topic-modeling-entity-graph",
    version="1.0.0",
    description="Reproducibility pipeline for Persian topic modeling and entity association graph",
    author="Amir Radnia",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=0.24.0",
        "bertopic>=0.12.0",
        "stanza>=1.4.0",
        "networkx>=2.6.0"
    ],
    python_requires=">=3.8",
)
