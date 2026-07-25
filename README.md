# Persian Topic Modeling and Entity Association Graph

A comprehensive reproducibility pipeline for topic modeling and entity association graph analysis on Persian text data.

## Overview

This repository contains the complete reproducibility pipeline for analyzing Persian Wikipedia data using topic modeling techniques and entity association graph construction. The pipeline includes:

- Topic Modeling: Implementation of BERTopic, LDA, NMF, and CTM models
- Named Entity Recognition: Using Stanza for Persian NER
- Entity Graph Analysis: Construction and analysis of entity co-occurrence graphs
- Link Prediction: Evaluation of various link prediction methods

## Repository Structure

`	ext
.
â”œâ”€â”€ README.md
â”œâ”€â”€ pipeline.ipynb
â”œâ”€â”€ evidence.json
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ setup.py
â”œâ”€â”€ LICENSE
â”œâ”€â”€ .gitignore
â”œâ”€â”€ figures/
â”‚   â”œâ”€â”€ figure_1_topic_model_trajectories.png
â”‚   â”œâ”€â”€ figure_2_multimetric_encoder_comparison.png
â”‚   â”œâ”€â”€ figure_3_link_prediction.png
â”‚   â”œâ”€â”€ figure_4_entity_distribution.png
â”‚   â””â”€â”€ figure_5_graph_structure.png
â””â”€â”€ CITATION.cff
`

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook/Lab
- Git

### Installation

1. Clone the repository:
   `ash
   git clone https://github.com/amirradnia99/persian-topic-modeling-entity-graph.git
   cd persian-topic-modeling-entity-graph
   `
2. Install dependencies:
   `ash
   pip install -r requirements.txt
   `
3. Launch the pipeline:
   `ash
   jupyter notebook pipeline.ipynb
   `

## Results Summary

### Topic Modeling Performance (K=30)

| Model | C_v Coherence | NPMI | Diversity | Stability |
|---|---:|---:|---:|---:|
| BERTopic | 0.5460 +/- 0.0118 | 0.0825 | 0.8126 | 0.8156 |
| LDA | 0.5215 +/- 0.0150 | 0.0623 | 0.7167 | 0.3787 |
| NMF | 0.4977 +/- 0.0080 | 0.1629 | 0.5456 | 0.7853 |
| CTM | 0.4722 +/- 0.0095 | -0.0728 | 0.6911 | 0.2215 |

### Entity Distribution

- Location: 31,997 mentions (34.3%)
- Person: 30,035 mentions (32.2%)
- Organization: 14,671 mentions (15.7%)
- Product: 6,067 mentions (6.5%)
- Facility: 3,590 mentions (3.8%)
- Event: 3,240 mentions (3.5%)

### Link Prediction Performance

| Method | ROC-AUC | Average Precision |
|---|---:|---:|
| Topic-K200 | 0.6387 +/- 0.0021 | 0.6166 +/- 0.0033 |
| Topic-K100 | 0.6376 +/- 0.0025 | 0.6225 +/- 0.0037 |
| Topic-K300 | 0.6359 +/- 0.0025 | 0.6196 +/- 0.0029 |
| DeepWalk | 0.6358 +/- 0.0039 | 0.6254 +/- 0.0046 |
| Node2Vec | 0.6297 +/- 0.0044 | 0.6170 +/- 0.0064 |
| Adamic-Adar | 0.6173 +/- 0.0014 | 0.6288 +/- 0.0022 |
| Jaccard | 0.6021 +/- 0.0020 | 0.6009 +/- 0.0032 |
| Pref. Attachment | 0.5693 +/- 0.0004 | 0.5954 +/- 0.0018 |
| Random | 0.4987 +/- 0.0026 | 0.4999 +/- 0.0025 |

## Figures

All figures are available in the igures/ directory.

## Citation

`ibtex
@misc{persian-topic-modeling-2026,
  title={Persian Topic Modeling and Entity Association Graph: A Reproducibility Study},
  author={Amir Radnia},
  year={2026},
  howpublished={\url{https://github.com/amirradnia99/persian-topic-modeling-entity-graph}}
}
`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request.

## Contact

For questions or issues, please open an issue on GitHub.

> Note: This repository contains the complete reproducibility pipeline and results from the study. The evidence.json file contains all raw results, provenance data, and integrity checks.
