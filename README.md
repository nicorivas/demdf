demdf
=====

The Discrete Element Method Data Format (DEMDF) project is an specification of a common data format for DEM simulations.

The DEMDF project aims to stablish an standard of configuration files for particle simulations.
The goal of the DEMDF project is to decouple the data handling/simulation specification from the
numerical methods of integration, which are specific to the many DEM implementations now available.
This would dramatically increase the felixibility of DEM simulations, and allow for easy validation of
numerical codes by making the comparisson between them direct.
Furthermore, the standarization of the configuration files would facilitate the writing of 
data analysis routines that could be used without effort indepeendent of the integration code used.
