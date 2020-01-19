# OpenWorkstation
 An open source and modular workstation concept for life science automation.

 * [Overview](#overview)
 * [OpenWorkstation API](#api)
 * [Development Status](#development_status)
 * [Getting Started](#getting_started)
 * [Contributing](#contributing)


 <a name="overview"></a>
## Overview

We present a general Open Source Hardware concept to develop scientific equipment. The general setup can be customized to fit diverse experimental requirements by adding different numbers and kinds of hardware modules to execute the desired functionality. Within these modules, each hardware module as well as the configuration of the hardware modules can be specifically customized according to the experimental requirements. This ‘drag and drop’ approach enables a high degree of versatility, since the components as well as their configuration can be customized to fit the given requirements.

Specifically, the OpenWorkstation concept provides the following features:

 * Modularity to combine different open source projects
 * Simple and fast development of customized hardware modules
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

The OpenWorkstation project is an open source project. The concept was developed in the labs of the [ARC Industrial Transformation Training Centre in Additive Biomanufacturing](http://additivebiomanufacturing.org) to simplify the design and development of automated solutions. The OpenWorkstation project remains under active development and new software as well as hardware features continue to be integrated.

Please do no hesitate to [get in touch](mailto:s.eggert@qut.edu.au) to provide feedback and discuss potential applications.

<a name="getting_started"></a>
## Getting started

The documentation is divided into the following sections:

 * [Concept](documentation/concept.md) for general information
 * [Pre-requisites and installation](documentation/installation.md) describes what you will need to install the OpenWorkstation API
 * [Programming](examples/programming.md) provides detailed instructions on writing scripts to operate the modules
 * [Developed module files](hardware/README.md) are available for the present workstation
 * [CAD part library](hardware/README.md) is provided to accelerate the development process for new module
 * [Development plan](documentation/dev_plan.md) outlines future work packages


<a name="contributing"></a>
## Contributing

We are looking for contributors!

[Get in touch](mailto:s.eggert@qut.edu.au)
