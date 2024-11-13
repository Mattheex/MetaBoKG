# MetaBoKG

MetaBoKG is a project dedicated to building a metabolomic feature-based ontology and a platform for creating and storing RDF graphs based on this ontology. The goal of MetaBoKG is to facilitate the integration, storage, and querying of metabolomics data through semantic web technologies, leveraging a structured ontology and linked data principles.

## Project Overview

The MetaBoKG project includes the following core components:

1. **Ontology Development**: A custom ontology designed to represent metabolomic features and their relationships, providing a formal structure for metabolomics data in RDF format. This ontology is a foundational piece for semantic annotations and for organizing metabolomics data in a knowledge graph.

2. **RDF Graph Generation**: Tools to convert metabolomics data from standard formats (MzTab and MGF files) into RDF graphs that align with the ontology. The RDF graphs enable advanced querying, data interoperability, and integration with other datasets and ontologies.

3. **Web-Based Platform (Future Development)**: A Dockerized platform hosting a web interface that interacts with a Jena-based RDF database. This platform will allow users to upload MzTab and MGF files, automatically converting them into RDF graphs and storing them in the database.

## Components

### 1. Ontology

The ontology is under development and is specifically designed for metabolomics data. It aims to represent metabolomic features, relationships, and other relevant concepts, providing a structured format for storing and querying metabolomics information.

### 2. Python Scripts for RDF Conversion

Python scripts are being developed to convert data from MzTab and MGF files into RDF graphs that adhere to the metabolomic ontology. These scripts will be able to:
- Parse MzTab and MGF files.
- Map parsed data to ontology terms.
- Generate RDF triples and populate an RDF graph.

### 3. Dockerized Web Platform (Upcoming)

The planned platform will be packaged as a Docker container, containing:
- **A web interface**: To allow users to upload MzTab and MGF files, configure graph settings, and visualize data.
- **RDF storage and querying**: A backend that communicates with a Jena database for RDF data storage and SPARQL querying.
- **RESTful API**: Enabling programmatic access to the platform for integration with other tools.

## Future Roadmap

- **Complete Ontology Development**: Finalize the metabolomic ontology for efficient representation of metabolomics data.
- **Develop and Test RDF Conversion Scripts**: Ensure reliable parsing of MzTab and MGF files and accurate RDF graph generation.
- **Dockerize the Platform**: Set up a Docker container that includes the web interface and necessary dependencies.
- **Integrate with Jena Database**: Connect the platform’s backend to a Jena database for RDF storage and SPARQL querying.
- **Build Web Interface**: Develop a user-friendly web interface for data upload, graph generation, and visualization.

## Getting Started

### Prerequisites

- **Docker** (for running the platform, in future versions)
- **Python 3.8+** (for RDF conversion scripts)
- **Apache Jena** (for RDF storage and SPARQL querying)

### Setup Instructions

Since the Dockerized platform and web interface are still in development, users can start by working with the Python scripts and ontology files.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MetaBoKG.git
   cd MetaBoKG
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run RDF Conversion Scripts**:
   - Update `config.yaml` (or equivalent configuration file) with paths to your MzTab and MGF files.
   - Run the script:
     ```bash
     python convert_to_rdf.py
     ```

### Usage (Planned for Future Versions)

The future web platform will allow users to:
- Upload metabolomics data files (MzTab, MGF).
- Convert data into RDF graphs stored in the Jena database.
- Perform SPARQL queries and visualize results through the web interface.

## Contributing

Contributions are welcome! If you’d like to contribute to the ontology, Python scripts, or future web platform, please open a pull request or start a discussion in the repository.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please contact Matthieu Feraud (mailto:matthieuferaud31@gmail.com).
