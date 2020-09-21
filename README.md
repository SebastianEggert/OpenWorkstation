[![DOI](https://zenodo.org/badge/222942681.svg)](https://zenodo.org/badge/latestdoi/222942681)

# OpenWorkstation

OpenWorkstation democratizes access to laboratory automation by providing an open-source and modular framework to design and build your own technology.

This repository contains an overview of the project, the source code for the OpenWorkstation API and addition tips on getting started. It's released and the projects remains under active development. Have fun exploring, hacking and building upon the project!

 * [Overview](#overview)
 * [OpenWorkstation API](#api)
 * [Contributing](#contributing)
 * [Getting Started](#getting_started)



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

<a name="contributing"></a>
## Contributing

The OpenWorkstation project is an active open-source project. I, Sebastian (https://twitter.com/se_eggert) started with this idea during my PhD project at the Queensland University of Technology (Australia) and will continue with it as a Postdoctoral Researcher at the Chair of Medical Materials and Implants (https://www.mw.tum.de/mmi/home/) at the Technical University of Munich (Germany). The concept was initially developed to manufacture hydrogels in an automated and reproducible fashion. Given the open-source character and the modularity, I believe that the OpenWorkstation could become an enabling tool for life science research, empowering scientists to build, share, and replicate the experimental setups.

This repository is always a work in progress and everyone is encouraged to help us build something that is useful to the many. Next, I am planning to set up a contributing guidelines and a development plan.

We are looking for contributors!

At the moment, support for the following areas would be appreciated very much:
- checking repository and documentation
- software engineers for the API and interface
- mechanical engineers to develop new modules
- early adopters to test the interface, API, single modules or functionality of entire platform

Please do no hesitate to [get in touch](mailto:sebastian.eggert@tum.de) with me to provide feedback, discuss potential applications or just to say hello.

<a name="getting_started"></a>
## Getting started

The documentation is divided into the following sections:

 * [Concept](documentation/concept.md) for general information
 * [Pre-requisites and installation](documentation/installation.md) describes what you will need to install the OpenWorkstation API
 * [Programming](documentation/programming.md) provides detailed instructions on writing scripts to operate the modules
 * [Developed module files](https://github.com/SebastianEggert/OpenWorkstation_hardware) are available for the present workstation
 * [CAD part library](https://github.com/SebastianEggert/OpenWorkstation_hardware) is provided to accelerate the development process for new module
 * [Development plan](documentation/dev_plan.md) outlines future work packages




[Get in touch](mailto:sebastian.eggert@tum.de)
