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
 * A complete documentation of the DEMDF.
 * A JSON Schema containing all the DEMDF specification.
 * A minimal and simple validation Python script that checks the validity of the configuration files using the JSON Schema.
 * Sample configuration files for several simulations.

### Features

### Limitations

It only supports 2 and 3 dimensions.

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "DEM Simulation",
    "description": "Specification of a Discrete Elemet Method (DEM) simulation",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the simulation",
            "type": "string"
        },
        "endTime": {
            "type": "number",
            "minimum": 0,
            "exclusiveMinimum": true
        },
        "particles": {
            "type": "array",
            "items": {
                "type": "array",
                "items": [{"type":number},{"type":number},{"type":number}]
            }
        }
    },
    "required": ["id", "name", "price"]
}
```
