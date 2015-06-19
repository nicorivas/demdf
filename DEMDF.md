# Lalala - lala

Specification of a Discrete Elemet Method (DEM) simulation

## Properties
 * domain: Two D-vectors specifying the opposite vertices of a square that defines the system's domain
 * dimensionality: Number of spatial degrees of freedom of particles
 * name: Name of the simulation
 * timeStepNumber: How many time-steps have been realized
 * timeStep: For soft-simulations, the time-step of integration of the forces
 * bodyForce: External body force
 * timeEnd: Time (in arbitrary units) at which the simulation should stop
 * particles: Array with particles
 * walls: Array with walls
 * timeStepNumberEnd: Number of time-steps at which the simulation should stop
 * time: Current time (in arbitrary units) of the simulation
