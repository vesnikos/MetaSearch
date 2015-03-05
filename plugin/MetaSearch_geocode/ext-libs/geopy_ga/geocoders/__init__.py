"""
Each geolocation service you might use, such as Google Maps, Bing Maps, or
Yahoo BOSS, has its own class in ``geopy.geocoders`` abstracting the service's
API. Geocoders each define at least a ``geocode`` method, for resolving a
location from a string, and may define a ``reverse`` method, which resolves a
pair of coordinates to an address. Each Geocoder accepts any credentials
or settings needed to interact with its service, e.g., an API key or
locale, during its initialization.

To geolocate a query to an address and coordinates:

    >>> from geopy.geocoders import Nominatim
    >>> geolocator = Nominatim()
    >>> location = geolocator.geocode("175 5th Avenue NYC")
    >>> print(location.address)
    Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
    >>> print(location.latitude, location.longitude)
    (40.7410861, -73.9896297241625)
    >>> print(location.raw)
    {u'place_id': u'9167009604', u'type': u'attraction', ...}


To find the address corresponding to a set of coordinates:

    >>> from geopy.geocoders import Nominatim
    >>> geolocator = Nominatim()
    >>> location = geolocator.reverse("52.509669, 13.376294")
    >>> print(location.address)
    Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
    >>> print(location.latitude, location.longitude)
    (52.5094982, 13.3765983)
    >>> print(location.raw)
    {u'place_id': u'654513', u'osm_type': u'node', ...}

Locators' ``geolocate`` and ``reverse`` methods require the argument ``query``,
and also accept at least the argument ``exactly_one``, which is ``True``.
Geocoders may have additional attributes, e.g., Bing accepts ``user_location``,
the effect of which is to bias results near that location. ``geolocate``
and ``reverse`` methods  may return three types of values:

- When there are no results found, returns ``None``.

- When the method's ``exactly_one`` argument is ``True`` and at least one
  result is found, returns a :class:`geopy.location.Location` object, which
  can be iterated over as:

    (address<String>, (latitude<Float>, longitude<Float>))

  Or can be accessed as `Location.address`, `Location.latitude`,
  `Location.longitude`, `Location.altitude`, and `Location.raw`. The
  last contains the geocoder's unparsed response for this result.

- When ``exactly_one`` is False, and there is at least one result, returns a
  list of :class:`geopy.location.Location` objects, as above:

    [Location, [...]]

If a service is unavailable or otherwise returns a non-OK response, or doesn't
receive a response in the allotted timeout, you will receive one of the
`Exceptions`_ detailed below.

Every geocoder accepts an argument ``format_string`` that defaults to '%s'
where the input string to geocode is interpolated. For example, if you only
need to geocode locations in Cleveland, Ohio, you could do::

    >>> from geopy.geocoders import GeocoderDotUS
    >>> geolocator = GeocoderDotUS(format_string="%s, Cleveland OH")
    >>> address, (latitude, longitude) = geolocator.geocode("11111 Euclid Ave")
    >>> print(address, latitude, longitude)
    11111 Euclid Ave, Cleveland, OH 44106 41.506784 -81.608148

"""

__all__ = (
    "get_geocoder_for_service",
    "ArcGIS",
    "Baidu",
    "Bing",
    "GeocoderDotUS",
    "GeocodeFarm",
    "GeoNames",
    "GoogleV3",
    "MapQuest",
    "OpenCage",
    "OpenMapQuest",
    "Nominatim",
    "YahooPlaceFinder",
    "LiveAddress",
)


from geopy_ga.geocoders.arcgis import ArcGIS
from geopy_ga.geocoders.baidu import Baidu
from geopy_ga.geocoders.bing import Bing
from geopy_ga.geocoders.dot_us import GeocoderDotUS
from geopy_ga.geocoders.geocodefarm import GeocodeFarm
from geopy_ga.geocoders.geonames import GeoNames
from geopy_ga.geocoders.googlev3 import GoogleV3
from geopy_ga.geocoders.mapquest import MapQuest
from geopy_ga.geocoders.opencage import OpenCage
from geopy_ga.geocoders.openmapquest import OpenMapQuest
from geopy_ga.geocoders.osm import Nominatim
from geopy_ga.geocoders.placefinder import YahooPlaceFinder
from geopy_ga.geocoders.smartystreets import LiveAddress

from geopy_ga.exc import GeocoderNotFound


SERVICE_TO_GEOCODER = {
    "arcgis": ArcGIS,
    "baidu": Baidu,
    "google": GoogleV3,
    "googlev3": GoogleV3,
    "geocoderdotus": GeocoderDotUS,
    "geonames": GeoNames,
    "yahoo": YahooPlaceFinder,
    "placefinder": YahooPlaceFinder,
    "opencage": OpenCage,
    "openmapquest": OpenMapQuest,
    "mapquest": MapQuest,
    "liveaddress": LiveAddress,
    "nominatim": Nominatim,
    "geocodefarm": GeocodeFarm,
}


def get_geocoder_for_service(service):
    """
    For the service provided, try to return a geocoder class.

    >>> from geopy_ga.geocoders import get_geocoder_for_service
    >>> get_geocoder_for_service("nominatim")
    geopy_ga.geocoders.osm.Nominatim

    If the string given is not recognized, a
    :class:`geopy_ga.exc.GeocoderNotFound` exception is raised.

    """
    try:
        return SERVICE_TO_GEOCODER[service.lower()]
    except KeyError:
        raise GeocoderNotFound(
            "Unknown geocoder '%s'; options are: %s" %
            (service, SERVICE_TO_GEOCODER.keys())
        )

