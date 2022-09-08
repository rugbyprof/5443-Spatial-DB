## Project 1 - Project setup  
#### Due: 09-13-2022 (Tuesday @ 3:30 p.m.)


# MORE TO BE ADDED

## Overview

No Groups for this one.

### Database

- Have local install of Postgres dB with PostGis installed and enabled.
- Visualization tools (e.g. Pgadmin4) recommended to allow myself or others to help debug problems. 
- Create a DB called `Project1` and use the public schema for this project.
- Find a data file from https://cs.msutexas.edu/~griffin/data and load it into your DB. Obviously create an appropriate table with a geometry data type added to allow for some spatial query's to be run. 

### Api

- Have a local api that has the following routes:
  - findAll
  - findOne
  - findClosest

#### findAll

- Returns all the tuples from your table

#### findOne

- Returns a single tuple based on a column name (attribute) and value (e.g `id=1299` , or `name=texas`).

#### findClosest

- Returns a single tuple which contains the closest geometry to the one passed in (e.g. `lon=-123.63454&lat=34.74645`)


## Deliverables

- Be ready to show the class on Sep 8th that your api works by running your routes in front of class. I will randomly select X number of students to present.
- Create a folder called `Project01` in your `Assignments` folder. 
- All of your code and any files used should be in this folder.
- Create an appropriate [README](../../Resources/03_Readmees/README.md) file. 
- Push your code to Github on the 8th of September **after** class. 
