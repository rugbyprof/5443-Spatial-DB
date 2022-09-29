## Attacking API


### Requirements

Using FastApi, create a set of routes that can be polled every couple of seconds and send back missile location data. First lets define a couple of things.

### Terminology

#### Base

A `base` is a geospatial polygon located somewhere in the continental US. 

#### MegaBase

A `MegaBase` is a set of `bases` aligned or allied with one another.  Each base within a particular `megabase` cannot have any other base aligned with another `militia` within its borders. The border of a `megabase` is a bounding box which contains all allied bases.

#### Regional Militia

A `Regional Militia` is the group in charge of a `MegaBase`. Each militia will have a unique name (ID) and each API call from this group will be accompanied by this ID.

#### Missile

A `missile` is an entity that has the following attributes:
- speed
- altitude
- lon/lat
- bearing
- blast-radius 

#### Speed 

Can be one of the following categories:

|  Cat  |  M/S  | MPH      |
| :---: | :---: | :------- |
|   1   |  111  | 248.307  |
|   2   |  222  | 496.614  |
|   3   |  333  | 744.921  |
|   4   |  444  | 993.228  |
|   5   |  555  | 1241.535 |
|   6   |  666  | 1489.842 |
|   7   |  777  | 1738.149 |
|   8   |  888  | 1986.456 |
|   9   |  999  | 2234.763 |

#### Altitude

Altitudes will have a baseline of `5000`ft and a ceiling of `30,000`ft. 

#### Blast Radius

Blast radii will be anywhere from `200`m up to `1000`m in `100`m increments. I think the `speed` and `blast radius` should be inversely proportionate, but will leave it up for debate.

|  Cat  | Radius |
| :---: | :----: |
|   1   |  200   |
|   2   |  300   |
|   3   |  400   |
|   4   |  500   |
|   5   |  600   |
|   6   |  700   |
|   7   |  800   |
|   8   |  900   |
|   9   |  100   |

### Public Routes 

#### Register

The regional militia will send in their ID and identify in some manner the bases in which they are defending. I'm ok with the backend (this api) assigning an area to each team. Or each team send in their own `bbox` to defend. Of course this would all have to be worked out in advance. A table in postGres should keep track of these relationships. They will also receive an "arsenal" based on region and number of bases (see private routes).

#### StartSimulation

This will register a regional militia with the simulation and start its clock, as well as the generating of missiles that will come their way. 


#### EndSimulation

This stops the missiles and returns a summary of events (score of some kind).

#### RadarSweep

This sends any missile(s) that are within some `buffer`  around the militias region. Basically the `bounding box + buffer` in each direction.

#### FireMissile

This is a route that sends the militias attempt at stopping an incoming missile. It will contain all the values contained in a missile type. Doing this allows both sides to calculate a hit for verification purposes. Also see comments. 

### Private Routes (functions)

#### Generate Missile

Creates a missile and randomly populates the following values:

- speed : pick a category 1-9
- altitude : randomly generate between min and max
- lon/lat  : random starting point outside of the game area
- bearing  : chosen based on the militia it is attacking and more specifically a base in that region. 
- blast-radius : category 1 - 9 possibly based on speed 

#### Generate Arsenal

Randomly assign x number of missiles of various strengths to a group. Should be based on region size, and number of bases to defend.

## Comments

- I think some randomness should be incorporated into each sides missiles. Meaning, just because a missile has a speed and bearing doesn't mean it will travel in a truly straight path. There should be some variance added to a missiles path that gets worse the farther it flies. 

- Maybe we need to come up with predefined categories of missiles so everyone can use a missile identifier. For example: *A `Mark V` missile has a speed of cat 9 and a blast radius of cat 2*. If we have a dozen or so of these predefined missiles, it will be easier to randomly assign arsenals to each team. 