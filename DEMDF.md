# Discrete Element Method File Format (DEMDF) specification.

The following document describes the Discrete Element Method File Format (DEMDF), a common file format for particle simulations. DEMDF is built upon the JavaScript Object Notation (JSON) data-interchange format; we refer the readers to [http://json.org/](http://json.org/) for the JSON data format specification. The JSON data format is used mainly due to its minimal formating and thus excellent human readibility, and due to the widespread availability of parsers in many programming lenguages.

DEMDF specifies the name, data types, uses and limits of common variables to all Discrete Element Method simulations. Its goals are flexibility, that is, the ability to be used by most types of particle simulations; low size, by reducing as much as possible repeated data; and readability.

## Properties
 * ###domain

 *An array of two arrays of size D, specifying the opposite vertices of a square that defines the system's domain.*

 The domain defines the region in space where objects are allowed to be. Any object outside the domain should result in an error. It's main use is avoiding unexpected behaviour by limiting the available space for particles. Notice that the wall objects and the grid are not neccessarily specified by the domain.

 Type: array

 Format: `[[x1,y1,z1],[x2,y2,z2]] for 3 dimensions.`

 * ###dimensionality

 *Number of spatial degrees of freedom of particles.*

 Type: integer

 range: (2,3)

 * ###name

 *Name of the simulation.*

 The name of the simulation should serve as a human readable reference to the specific simulation. It should not be used for the generation of directories, as simulations could consist of several directories, and a general name is more flexible than directory names

 Type: string

 * ###eventCount

 *How many events have been processed since the beginning of an event-driven simulation.*

 Type: integer

 range: (0,infty)

 * ###objectTypes

 *An array of objects specifying the properties of each type of object..*

 Object types exist to reduce the amount of data saved on the particle list, as all particle properties (with the exception of position and velocity, stored in the 'particles' list) can be stored in an objectType and thus only referenced by the objectType id.

 Every particle should have an objectType identifier, and the corresponding properties stored by the objectType. For example, the radius of particle [0.1, 0.5, 0.3, 8.1, 2.3, 5.1, 10] is stored in the objectType 10.

 Type: array

 * ###timeStep

 *For soft-simulations, the time-step of integration of the forces.*

 Type: number

 range: (0,infty)

 * ###timeStepCount

 *How many time-steps have been realized since the beginning of the simlation.*

 Type: integer

 range: (0,infty)

 * ###fileFormatVersion

 *Version of the DEMDF specification being used.*

 Format names and structure will change, so knowing the version being read becomes neccessary

 Type: number

 range: ,infty)

 * ###timeEnd

 *Time (in arbitrary units) at which the simulation should stop.*

 Type: number

 range: (0,infty)

 * ###interactions

 *Array of objects, each object containing the description of the interaction between the different objectTypes.*

 Type: array

 * ###bodyForce

 *An external body force.*

 It should be specified as a D-vector which results a in a force in simulational units being applied to all objects

 Type: array

 * ###eventCountEnd

 *Number of events at which the simulation should stop.*

 Type: integer

 range: (0,infty)

 * ###objects

 *Object of objects, containing the lists of walls and particles..*

 Type: object

 * ###timeStepCountEnd

 *Number of time-steps at which the simulation should stop.*

 Type: integer

 range: (0,infty)

 * ###time

 *Current time (in arbitrary units) of the simulation.*

 Type: number

 range: (0,infty)

 * ###output

 *Object containing the list of output routines, such as measurements and including demdf files.*

 Type: object

 * ###fileFormat

 *Name of data format; always demdf.*

 Intended for verification of the validity of the file

 Type: string

