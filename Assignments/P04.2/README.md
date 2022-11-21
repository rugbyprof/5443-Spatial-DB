## Project 4.1 - Battle Ship
#### Due: 11-22-2022 (Tuesday @ 3:30 p.m.)

## Game Database
<img src="./images/postgres.png" width="150">


### Problem Statement:

- The file [ships.json](ships.json) has a lot of information in different categories including: ship info, ships armaments (guns and location), types of ammo and ammo counts. 
- This data needs storing in a set of tables in postGres. 


### Discussion

The goal for creating the database, as you all know is to allow us to run queries to pull information or update information in an easy manner. So, I will give you some possible queries to think about before creating your tables.

- Fire the guns for one of your ships.
- Change the speed and direction of a specific ship.
- Rotate the guns on one of your ships. 

What do all of these entail? Well to fire the guns for a ship you need to do the following:
  - Creating a fire solution requires getting the guns elevation, guns bearing, ammo type, and current time at a minimum. 
  - The "[ship](./data/ship.sql)" table (at the moment) has no information about a guns bearing, guns elevation, its ammo type, and if it has ammo.
  - So the tables I provided will have to altered or additional tables added to keep track of the state of your fleet.  
  - A table called `ShipState` could be useful. Lets make one.

```sql
CREATE TABLE ship_state (
    ship_id numeric NOT NULL,
    bearing float,
    speed numeric
    location coord
);
```

```sql
CREATE TABLE gun_state (
    ship_id numeric,
    gun_id numeric,
    bearing float,
    angle float
);
```


- I will provide a set of helper files to create very basic tables. There are no primary or foreign keys provided, that is something you will need to add. 
- I took some short cuts when I created my tables by allowing json in some columns. But this allows the query's to be easier, and not force us to create more tables.

| Table Name | File Name                               | description                                                      |
| :--------- | :-------------------------------------- | :--------------------------------------------------------------- |
| cartridge  | [cartridge.sql](./data/cartridge.sql)   | Describes projectiles with gunpowder packed within the case      |
| gun        | [run.sql](./data/run.sql)               | Gives info about each gun like ammo and size                     |
| projectile | [projectile.sql](./data/projectile.sql) | This describes projectiles with no case. Uses bags of propellant |
| ship_guns  | [ship_guns.sql](./data/ship_guns.sql)   | This describes guns on a specific ship with their location       |
| ship       | [ship.sql](./data/ship.sql)             | Has all info about each ship                                     |
| torpedo    | [torpedo.sql](./data/torpedo.sql)       | Describes the different torpedo's                                |

