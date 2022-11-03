## Battle Ship!

- N number of teams 
- One predefined area of combat. 
- Each team will receive the same number of battle ships.
- Each team will randomly spawn, eith ships equidistant apart in some standard formation.
- Some teams may be in visual range of other teams, or not. 
- The closer teams are, the more accurate "radar" data they will have.
- Choices that teams have are:

```python
def turnFleet(bearing: float):
    """ Moves the entire fleet toward the input bearing. A fleet can only turn
        10 degrees per turn so it may take multiple turns to acheive your goal.
    Params:
        bearing (float) : direction your fleet wants to go. 
    Returns: 
        bearing (float) : the new (and current) direction of the fleet
    """
    pass
```

```python
def moveFleet(distance: float):
    """ Moves the entire fleet along each ships current bearing up to its max       
        speed distance for a turn. Multiple turns may be required to acheive the goal. The distance a fleet can move is slower than individual ships. 
    Params:
        distance (float) : distance your fleet wants to go. 
    Returns: 
        location (list[points]) : the new (and current) locations of each ship.
    """
    pass
```

```python
def turnShip(ship_id: list, bearing:list):
    """ Turns a list of ships toward the bearing indicated. Only half the fleet can be turned in one turn as each ship has a unique turning radius which is better than the fleets as a whole. 

    Params:
        ship_id (list[int]) : ship ids to be turned 
        bearing (list[float]) : direction for each ship 
    Returns: 
        bearing (list[float]) : the new (and current) direction of the corresponding ships
    """
    pass
```

```python
def moveShip(ship_id: list, distance:list):
    """ Moves each ship a specified distance. Up to half the fleet can be moved in this manner. Each ship has a unique speed, and multiple turns may be required to acheive each goal.
    Params:
        ship_id (list[int])
        distance (list[int]) : distance your fleet wants to go. 
    Returns: 
        location (list[points]) : the new (and current) locations of each ship in the list.
    """
    pass
```

```python
def fireVolley(ship_id: int, angle:float, bearing:float):
    """ Fires the ships guns at the angle and bearing indicated. Velocity is      
        defined by the ship type. The bearing is also limited by:
        - 45 degrees perpendicular to
          - the bearing of the ship
          - and direction of the guns (port starboard)
        In real life guns can be rotated up to 300°, but that's a lot of stuff to keep track of already.
    Params:
        ship_id (int)
        angle (float) : between -5° (below ships deck) to 45°
    Returns: 
        location (list[points]) : the new (and current) locations of each ship in the list.
    """
    pass
```


## Ships

2,700 pounds (1,225 kg) armor-piercing projectiles at a muzzle velocity of 
2,500 ft/s (762 m/s), or 
1,900 pounds (862 kg) high-capacity projectiles at 2,690 ft/s (820 m/s), 
up to 24 miles (21 nmi; 39 km).


```json
[
   {
      "class":"Beto class",
      "displacement":"35,000 tons",
      "Armament":[
         "9 × 16 in (406 mm) (3x3) 2,500 ft/s (762 m/s)",
         "20 × 5 in (127 mm) (10x2)",
         "16 x 1.1 inch AA (4x4)"
      ],
      "Armor":"12in Belt / 7in Deck",
      "Speed":"28 knots"
   },
   {
      "class":"d'Ivoire class",
      "displacement":"38,000 tons",
      "Armament":[
         "9 × 16 in (406 mm) (3x3)",
         "20 × 5 in (127 mm) (8x2)",
         "40 x 40mm AA (17x4)",
         "76 x 20 mm AA"
      ],
      "Armor":"12in Belt / 7.5in Deck",
      "Speed":"27 knots"
   },
   {
      "class":"Kılıç class",
      "displacement":"48,500 tons",
      "Armament":[
         "9 × 16 in (406 mm) (3x3)",
         "20 × 5 in (127 mm) (10x2)",
         "80 x 40mm AA (20x4)",
         "49 x 20 mm AA"
      ],
      "Armor":"12in Belt / 8in Deck",
      "Speed":"33 knots"
   },
   {
      "class":"Vikrant class",
      "displacement":"65,000 tons",
      "Armament":[
         "12 × 16 in (406 mm) (4x3)",
         "20 × 5 in (127 mm) (10x2)",
         "80 x 40mm AA (20x4)",
         "49 x 20 mm AA"
      ],
      "Armor":"16in Belt / 8.2in Deck",
      "Speed":"28 knots"
   }
]
```
