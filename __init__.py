'''
init file for the base map "module"
'''

from .Territories import supply_centers
from .Territories import Empty_land
from .Territories import coastal_land
from .Territories import sea_territories
from .Territories import home_centers

from .Borders import supply_center_connections
from .Borders import supply_empty_connections
from .Borders import empty_empty_connections
from .Borders import coastal_supply_connections
from .Borders import coastal_empty_connections
from .Borders import sea_connections


## Territories
land_territoies = supply_centers + Empty_land 

all_territories = land_territoies + sea_territories

## Connections
coastal_connections = coastal_supply_connections + coastal_empty_connections

land_connections = supply_center_connections + \
                    supply_empty_connections + \
                    empty_empty_connections 

all_connections = land_connections + sea_connections + coastal_connections

if __name__ == "__main__":
    print("Running diagnostics")
    for player, centers in home_centers.items():
        for c in centers:
            assert c in supply_centers, f"{c} is not a supply center"
    for c in Empty_land:
        assert c not in supply_centers, f"{c} is a supply center"
    for connection in supply_center_connections:
        assert all(elem in supply_centers for elem in connection)
    for connection in empty_empty_connections:
        assert all(elem in Empty_land for elem in connection)
    for connection in supply_empty_connections:
        assert sum(elem in supply_centers for elem in connection) == 1
        assert sum(elem in Empty_land for elem in connection) == 1
    for connection in coastal_supply_connections:
        assert sum(elem in coastal_land for elem in connection) == 1
        assert sum(elem in sea_territories for elem in connection) == 1
        assert sum(elem in supply_centers for elem in connection) == 1
    for connection in coastal_empty_connections:
        assert sum(elem in coastal_land for elem in connection) == 1
        assert sum(elem in sea_territories for elem in connection) == 1
        assert sum(elem in Empty_land for elem in connection) == 1
    for connection in sea_connections:
        assert all(elem in sea_territories for elem in connection)

