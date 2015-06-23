DEMDF
=====

The Discrete Element Methods Data Format (DEMDF) project aims to create a specification for a common and universal data format for DEM simulations.

The goal of the DEMDF project is to decouple the data handling/simulation specification from the
numerical methods of integration, which are specific to the many DEM implementations now available.
This would dramatically increase the felixibility of DEM simulations, and allow for easy validation of
numerical codes by making the comparisson between them direct.
Furthermore, the standarization of the configuration files would facilitate the writing of 
data analysis routines that could be used without effort independent of the integration code used.

DEMDF is based on the JSON data format, and uses a JSON Schema to specify all the variable names, descriptions, types and constrains.

We provide:
 * [A complete documentation of the DEMDF](DEMDF.md).
 * A JSON Schema containing all the DEMDF specification (demdfSchema.json).
 * A minimal and simple validation Python script that checks the validity of the a particular DEMDF file using the JSON Schema (validator.py).
 * Sample configuration files for several simulations.

### Features

### Limitations

It only supports 2 and 3 dimensions.

### Contributing

The DEMDF project is now on its early stages and would highly benefit from support from the DEM community. If you have, manage or contribute to a particle simulation code, and would like to add support for the DEMDF format, please feel free to contact us. If you would like to comment or participate regularly in the development of the DEMDF file format specification, you will be more than welcome!
