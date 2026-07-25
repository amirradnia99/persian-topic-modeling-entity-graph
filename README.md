# Persian Topic Modeling and Entity Association Graph

![License](https://img.shields.io/badge/License-MIT-yellow.svg)

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
@misc{persian-topic-modeling-2026,
  title={Persian Topic Modeling and Entity Association Graph: A Reproducibility Study},
  author={Amir Radnia},
  year={2026},
  howpublished={\url{https://github.com/amirradnia99/persian-topic-modeling-entity-graph}}
}
```

## License

This project is licensed under the MIT License.
