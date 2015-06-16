DEMDF
=====

The Discrete Element Methods Data Format (DEMDF) project is an specification for a common data format for DEM simulations.

The DEMDF project aims to stablish an standard of configuration files for particle simulations.
The goal of the DPMDF project is to decouple the data handling/simulation specification from the
numerical methods of integration, which are specific to the many DEM implementations now available.
This would dramatically increase the felixibility of DEM simulations, and allow for easy validation of
numerical codes by making the comparisson between them direct.
Furthermore, the standarization of the configuration files would facilitate the writing of 
data analysis routines that could be used without effort indepeendent of the integration code used.

DEMDF is based on the JSON data format, and simply specifies common names, and a few other things.
This is the complete JSON schema:

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
        "price": {
            "type": "number",
            "minimum": 0,
            "exclusiveMinimum": true
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": true
        }
    },
    "required": ["id", "name", "price"]
}
```
