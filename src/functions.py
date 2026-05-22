##############################################################################################
# Functions for Project: Near Real-Time Wildfire Population Proximity Assessment for Australia
##############################################################################################

from rasterio.mask import mask as raster_mask

def raster_sum(raster, geometry, nodata=None):
    """
    Compute the sum of raster pixel values within a certain geometry.

    This function masks a raster using a geometry and calculates the
    total sum of all pixel values inside it.

    All NoData values and negative values are treated as 0 before calculation.
    
    Parameters
    ----------
    raster : rasterio.io.DatasetReader
        Open raster dataset.
    geometry : shapely.geometry.polygon.Polygon
        A single geometry used to mask the raster. Must be in the same CRS as the raster.
    nodata : float, optional
        NoData value to exclude. If None, the raster's internal nodata value is used.

    Returns
    -------
    float
        Sum of estimated population that lies inside the buffer around the fire. 
        Returns 0.0 if no valid data is found.

    Examples
    --------
    >>> raster_sum(population_raster, buffer_geometry, nodata=-99999)
    1450.0
    """

    # Mask raster using a single geometry (in a list as required by rasterio)
    data, _ = raster_mask(
        raster,
        [geometry],
        crop=True
    )

    # Extract first band and convert to float for calculations
    arr = data[0].astype(float)

    # Determine NoData value 
    nodata_value = raster.nodata if nodata is None else nodata

    # Replace NoData values with 0
    if nodata_value is not None:
        arr[arr == nodata_value] = 0

    # Replace negative values with 0 
    arr[arr < 0] = 0

    # Return total sum of valid pixels
    return float(arr.sum())


def classify(val):
    """ 
    Classifies summed population within buffer into discrete levels
    based on user-defined thresholds.

    Paramteres:
    ----------
    val: int or float
         Total population value (here within buffer around a fire event)

    Returns
    -------
    int
        Classification classes:
        0 = no people
        1 = between 1 and 9 people
        2 = between 10 and 99 people
        3 = over 100 people
    
    Example: 
    >>> classify(50)
    2
    """
    if val == 0:
        return 0
    elif val < 10:
        return 1
    elif val < 100:
        return 2
    else:
        return 3
