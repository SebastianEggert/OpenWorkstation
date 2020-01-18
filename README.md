# OpenWorkstation
 An open source and modular workstation concept for life science automation.

 * [Overview](#overview)
 * [OpenWorkstation API](#api)
 * [Development Status](#development_status)
 * [Getting Started](#getting_started)
 * [Contributing/Building](#contributing)


 <a name="overview"></a>
 ## Overview

 We present a general Open Source Hardware (OSH) concept to develop scientific equipment. This general set up can be customized to fit diverse experimental requirements by adding different numbers and kinds of modules to execute the desired functionality. Within these modules, each hardware module as well as the configuration of the hardware modules can be specifically customized according to the experimental requirements. This ‘drag and drop’ approach enables a high degree of versatility, since the components as well as their configuration can be customized to fit the given requirements, including the option to remove components from the platform non-destructively without interfering with the functional operation of the other modules.

 Specifically, the OpenWorkstation concept provides the following features:

 * Modularity
 * feature 2
 * feature 3
 * feature 4

 <p align="center">
 <img src="documentation/images/workstation_setup.tiff" width="700"/></p>

 <a name="api"></a>
 ## OpenWorkstation API

 Building upon the [Opentrons API](https://github.com/Opentrons/opentrons), the OpenWorkstation API is a simple Python framework designed to allow the operation of hardware modules. Basic commands are written in the [Gcode language](https://en.wikipedia.org/wiki/G-code) to enable custimzation and make it accessible to anyone with basic programming skills.

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

 * [Concept](documentation/concept.md) provides additional information on the concept.
 * [Hardware files](hardware/README.md) are available for the present workstation and a part library is provided to accelerate the development process for new module.
 * [Control Board Module: Smoothieboard](documentation/control-board-module.md) describes what you will need, and the set-up of both hardware and software.
 * [Smoothieboard](documentation/installation.md) describes what you will need, and the set-up of both hardware and software.
 * [Pre-requisites and installation](documentation/installation.md) describes what you will need, and the set-up of both hardware and software.
 * [Examples](examples/examples.md) are provided and will explain how the OpenWorkstation was applied for our research.


 <a name="contributing"></a>
 ## Contributing

 We are looking for contributors!
