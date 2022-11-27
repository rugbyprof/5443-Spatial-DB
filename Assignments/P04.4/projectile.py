# This code calculates
# 1. Time taken by a projectile,
# 2. location where it impacts with ground/ship
# 3. angle of impact
# 4. joules of energy it carries at impact

import math

ENERGY_TO_MASS_RATIO = 5
LLPRECISION = 8
PRECISION = 3


class Projectile:
    def __init__(
        self,
        mps,
        bearing,
        start_lon,
        start_lat,
        altitude,
        elevation,
        payload_mass,
    ):
        """
        Calculates where a projectile will land and how much energy created with proper inputs.
        Params:
            mps (float) : meters per second
            bearing (float): degree in which the gun points
            start_lon (float): starting longitude of gun
            start_lat (float): starting latitude of gun
            altitude (float): altitude of gun (usually 10m on ship deck)
            elevation (float): the barrels vertical angle from -1 degrees to 45 degrees
            payload_mass (float): weight of projectile in kg
        """
        self.mps = mps
        self.bearing = bearing
        self.startLat = start_lat
        self.startLon = start_lon
        self.altitude = altitude
        self.elevation = elevation
        self.mass = payload_mass
        self.destLat = None
        self.destLon = None

        self.vf_y = 0
        self.vf_x = 0

        # calc x-component and y-component of the velocity
        self.v_x = self.mps * math.cos(self.elevation * math.pi / 180)
        self.v_y = self.mps * math.cos(self.elevation * math.pi / 180)

        self.totFlightTime = self.calcFlightTime()
        self.distanceTravelled = self.getDistanceTravelled()

        self.destLat, self.destLon = self.getDestCoords()
        self.impactAngle = self.getImpactAngle()
        self.impactEnergy = self.getEnergy()

    def __str__(self):
        a = f"totFlightTime      ::  {str(round(self.totFlightTime,PRECISION))}"
        a += f"\ndistance travelled ::  {str(round(self.distanceTravelled,PRECISION))}"
        a += f"\ndestLat            :: {str(round(self.destLat,LLPRECISION))}"
        a += f"\ndestLon            ::  {str(round(self.destLon,LLPRECISION))}"
        a += f"\nimpactAngle        :: {str(round(self.impactAngle,PRECISION))}"
        a += f"\njoulesAtImpact     ::  {str(round(self.impactEnergy,PRECISION))}"
        a += f"\nmegaJoulesAtImpact ::  {str(round(self.impactEnergy/1000000,PRECISION))}"
        return a

    def calcFlightTime(self):
        tot_disp = -1 * self.altitude
        # using v^2 - u^2 = 2as
        v = (((self.v_y**2) + 2 * (-9.8) * tot_disp) ** 0.5) * -1

        # using v = u + at
        t = (v - self.v_y) / (-9.8)

        self.vf_y = v
        return t

    def getDistanceTraveled(self):
        self.vf_x = self.v_x
        return self.totFlightTime * self.v_x

    def getDestCoords(self):
        R = 6378.1 * (10**3)  # Radius of the Earth in meters
        brng = self.bearing
        d = self.distanceTraveled  # Distance in meters

        lat1 = math.radians(self.startLat)  # Current lat point converted to radians
        lon1 = math.radians(self.startLon)  # Current long point converted to radians

        lat2 = math.asin(
            math.sin(lat1) * math.cos(d / R)
            + math.cos(lat1) * math.sin(d / R) * math.cos(brng)
        )

        lon2 = lon1 + math.atan2(
            math.sin(brng) * math.sin(d / R) * math.cos(lat1),
            math.cos(d / R) - math.sin(lat1) * math.sin(lat2),
        )

        lat2 = math.degrees(lat2)
        lon2 = math.degrees(lon2)

        return (lat2, lon2)

    def getImpactAngle(self):
        tot_disp = -1 * self.altitude
        v = (((self.v_y**2) + 2 * (-9.8) * tot_disp) ** 0.5) * -1
        # tan of angle = v_y/v_x
        tan_v = v / self.v_x

        return math.atan(tan_v) * 180 / math.pi

    def getEnergy(self):
        return (
            0.5
            * self.mass
            * ((self.vf_y**2) + (self.vf_x**2))
            * ENERGY_TO_MASS_RATIO
        )

    def results(self):
        return {
            "totFlightTime": round(self.totFlightTime, PRECISION),
            "distance traveled": round(self.distanceTraveled, PRECISION),
            "destLat": round(self.destLat, LLPRECISION),
            "destLon": round(self.destLon, LLPRECISION),
            "impactAngle": round(self.impactAngle, PRECISION),
            "joulesAtImpact": round(self.impactEnergy, PRECISION),
            "megaJoulesAtImpact": round(self.impactEnergy / 1000000, PRECISION),
        }


def usage():
    print(
        """Projectile(
        meters_per_second, 
        gun bearing,
        startLon, 
        startLat,
        altitude (in meters), 
        elevation (in degrees)
        projectile_mass (in kg)
        )
        """
    )


if __name__ == "__main__":

    proj = Projectile(700, 270, -4.660736864, 44.54346084, 10, 45, 1900)
    print(proj)
    print(proj.results())
    pass
