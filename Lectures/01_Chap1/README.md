

- https://blog.devart.com/difference-between-schema-database.html
  - https://www.postgresql.org/docs/current/sql-createschema.html
  - https://www.postgresql.org/docs/current/sql-createdatabase.html

- https://gisgeography.com/spatial-data-types-vector-raster/

- https://trac.osgeo.org/gdal/wiki/FAQGeneral#WhatdoesOGRstandfor


A database is the main container, it contains the data and log files, and all the schemas within it. You always back up a database, it is a discrete unit on its own. Schemas are like folders within a database, and are mainly used to group logical objects together, which leads to ease of setting permissions by schema.

https://geoalchemy-2.readthedocs.io/en/latest/orm_tutorial.html