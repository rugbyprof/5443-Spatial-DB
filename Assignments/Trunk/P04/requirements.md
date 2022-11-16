## P04 - Requirements

## Server
- Digital ocean (or some other) server in which your project code and database will be places.
- Your fastApi script and PostGres database will reside on the server.

## Database

- You will use as much of the power of PostGis as you can when implementing your project.
- Overuse of Python in lieu of using PostGis can result in loss of points.
- Static data should be stored in tables, then selected to be used in other calculations that require dynamic (real time) data.

## API

- An api that communications with `missilecommand` allow you (the defender) to stop incoming missiles.
- This api should perform the calculations necessary to stop incoming missiles. Again, using postgres for as much as you can.

## Game Overview

### 1) REGISTRATION 

- Register with game by sending a simple get request.
    - **GET** : `http://missilecommand.live/REGISTER`
- Response:
    - **id**      : int - unique integer assigned to a team.
    - **region**  : geojson - A featureCollection  that contains a multipolygon for a region to be defended.
    - **arsenal** : json - A key value dictionary with missile name and amount of missiles.
    - **cities**  : geojson - A featureCollection of points that reside in the region which will be targeted. 

- Example Response
```json 
{
  "id": 2,
  "region": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [
                [
                  -90.843911,
                  29.05005
                ],
                [
                  -90.820342,
                  29.057325
                ],
                ...
,
                [
                  -80.17395,
                  25.525375
                ]
              ]
            ]
          ]
        },
        "properties": {
          "gid": 6,
          "cid": 2,
          "prev_size": 18020,
          "reduced_size": 1164
        }
      }
    ]
  },
  "arsenal": {
    "Atlas": 17,
    "Harpoon": 13,
    "Hellfire": 15,
    "Javelin": 13,
    "Minuteman": 11,
    "Patriot": 6,
    "Peacekeeper": 9,
    "SeaSparrow": 7,
    "Titan": 5,
    "Tomahawk": 2,
    "Trident": 2,
    "total": 100
  },
  "cities": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            -80.947266,
            26.115986
          ]
        },
        "properties": {
          "id": 14,
          "latitude": 26.115986,
          "longitude": -80.947266
        }
      },
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            -90.878906,
            30.297018
          ]
        },
        ...
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            -85.429688,
            34.415973
          ]
        },
        "properties": {
          "id": 77,
          "latitude": 34.415973,
          "longitude": -85.429688
        }
      }
    ]
  },
  "active": false
}
```

### 2) START

- Start a game by sending a request with the teamID you received from `REGISTER`: 
    - **GET** :`http://http://missilecommand.live:8080/START/2`

- Response:
  - list : [string]
```json
[
  "Let get started !!! Use RADAR_SWEEP to see incoming missiles..."
]
```

### 3) RADARSWEEP

- Every few seconds, you should perform a `radar sweep` to get incoming missiles: 
    - **GET** :`http://missilecommand.live:8080/RADAR_SWEEP`

- Response: a list of missiles which should contain the following:
    - **id**            : int (e.g. 0-n)
    - **lon**           : float (e.g. -98.1234)
    - **lat**           : float (e.g. 34.3456)
    - **bearing**       : float (e.g. 0 - 359)
    - **altitude**      : float (e.g. 5000 - 10000)
    - **current_time**  : int (unix timestamp)
    - **missile_type**  : string (value from missile table)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "id": 177,
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -61.688978575,
          41.338014636
        ]
      },
      "properties": {
        "bearing": 4.6608386,
        "altitude": 10111.861,
        "current_time": 1667323116,
        "missile_type": "SeaSparrow"
      }
    },
    {
      "id": 166,
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -61.669318861,
          26.736942608
        ]
      },
      "properties": {
        "bearing": 5.0966997,
        "altitude": 13271.164,
        "current_time": 1667323116,
        "missile_type": "Trident"
      }
    },
    ...
```

### 4) FIRE_SOLUTION

- As you complete radar sweeps obtaining missile location information you attempt to identify missiles targeting your region. As these missiles are identified you should POST a fire solution in an attempt to bring them down: 
    - **POST** :`http://missilecommand.live:8080/FIRE_SOLUTION`

- Post Body should contain the following: 

  - team_id                 : int 
  - target_missile_id       : int
  - missile_type            : string - type of missile
  - fired_time              : int - unix timestamp
  - firedfrom_lat           : float - beginning lat
  - firedfrom_lon           : float - beginning lon
  - aim_lat                 : float - target lat
  - aim_lon                 : float - target lon
  - expected_hit_time       : int - unixtimestamp
  - target_alt              : float - targets altitude

