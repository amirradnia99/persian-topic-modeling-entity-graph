# Persian Topic Modeling and Entity Association Graph

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626.svg?&logo=Jupyter&logoColor=white)](https://jupyter.org/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21555696.svg)](https://doi.org/10.5281/zenodo.21555696)

A comprehensive reproducibility pipeline for topic modeling and entity association graph analysis on Persian Wikipedia.

## Overview

This repository contains a reproducibility pipeline for:

- BERTopic, LDA, NMF, and CTM topic models
- Persian named entity recognition using Stanza
- Entity co-occurrence graph construction
- Link prediction evaluation

## Repository Structure

```text
.
├── README.md
├── pipeline.ipynb
├── requirements.txt
├── setup.py
├── LICENSE
├── .gitignore
└── CITATION.cff
```

## Installation

```bash
git clone https://github.com/amirradnia99/persian-topic-modeling-entity-graph.git
cd persian-topic-modeling-entity-graph
pip install -r requirements.txt
jupyter notebook pipeline.ipynb
```

## Citation

```bibtex
@software{radnia2026pwner,
  author = {Radnia, Amir and Keshvari, Saman and Naderi, Hassan},
  title = {Persian Topic Modeling and Entity Association Graph},
  year = {2026},
  publisher = {Zenodo},
  version = {v1.0.0-silver},
  doi = {10.5281/zenodo.21555696},
  url = {https://github.com/amirradnia99/persian-topic-modeling-entity-graph}
}
```

## License

- Code: MIT License
- Source corpus: external dataset under original license
- Derived inventories: Silver-standard research artifact

## Contact

Repository:
https://github.com/amirradnia99/persian-topic-modeling-entity-graph

DOI:
https://doi.org/10.5281/zenodo.21555696
