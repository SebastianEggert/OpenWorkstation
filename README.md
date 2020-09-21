[![DOI](https://zenodo.org/badge/222942681.svg)](https://zenodo.org/badge/latestdoi/222942681)

# OpenWorkstation

OpenWorkstation democratizes access to laboratory automation by providing an open-source and modular framework to design and build your own technology.

This repository contains an overview of the project, the source code for the OpenWorkstation API and addition tips on getting started. It's released and the projects remains under active development. Have fun exploring, hacking and building upon the project!

 * [Overview](#overview)
 * [OpenWorkstation API](#api)
 * [Development Status](#development_status)
 * [Getting Started](#getting_started)
 * [Contributing](#contributing)


 <a name="overview"></a>
## Overview

We present a general Open Source Hardware concept to develop scientific equipment. The general setup can be customized to fit diverse experimental requirements by adding different numbers and kinds of hardware modules to execute the desired functionality. Within these modules, each hardware module as well as the configuration of the hardware modules can be specifically customized according to the experimental requirements. This ‘drag and drop’ approach enables a high degree of versatility, since the components as well as their configuration can be customized to fit the given requirements.

Specifically, the OpenWorkstation concept provides the following features:

 * Simple and fast development of customized hardware modules
 * Modularity to combine different open source projects
 * Available API to operate modules
 * Hardware and software files are freely accessible




 <p align="center">
 <img src="documentation/images/workstation_setup_v0.1.tif" width="700"/></p>



<a name="api"></a>
## OpenWorkstation API

Building upon the [Opentrons API](https://github.com/Opentrons/opentrons), the OpenWorkstation API is a simple Python framework designed to allow the operation of hardware modules.

If you are familiar with python and comfortable running ``pip``, you can install OpenWorkstation API by running:

```
pip install openworkstation
```

<a name="development_status"></a>
## Development status

The OpenWorkstation project is an open-source project. The concept was developed to simplify the design and development of automated solutions for experimental workflows. The OpenWorkstation project remains under active development and new software as well as hardware features continue to be integrated.

Please do no hesitate to [get in touch](mailto:sebastian.eggert@tum.de) to provide feedback and discuss potential applications.

<a name="getting_started"></a>
## Getting started

The documentation is divided into the following sections:

 * [Concept](documentation/concept.md) for general information
 * [Pre-requisites and installation](documentation/installation.md) describes what you will need to install the OpenWorkstation API
 * [Programming](documentation/programming.md) provides detailed instructions on writing scripts to operate the modules
 * [Developed module files](https://github.com/SebastianEggert/OpenWorkstation_hardware) are available for the present workstation
 * [CAD part library](https://github.com/SebastianEggert/OpenWorkstation_hardware) is provided to accelerate the development process for new module
 * [Development plan](documentation/dev_plan.md) outlines future work packages


<a name="contributing"></a>
## Contributing

We are looking for contributors!

[Get in touch](mailto:sebastian.eggert@tum.de)
