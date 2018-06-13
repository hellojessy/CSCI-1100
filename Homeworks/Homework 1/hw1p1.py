jupiter_rad = 88846/2
jupiter_dis = 483632000
earth_rad   = 7926/2
earth_dis   = 92957100
sun_rad     = 864938/2
lightspeed  = 186000
volume_j    = (4/3)*3.14159*(jupiter_rad**3)
volume_s    = (4/3)*3.14159*(sun_rad**3)
volume_e    = (4/3)*3.14159*(earth_rad**3)

print("Sun-to-Jupiter radius ratio:", round((sun_rad)/(jupiter_rad),2))
print("Sun-to-Earth radius ratio:", round((sun_rad)/(earth_rad),2))
print("Jupiter-to-Earth radius ratio:", round((jupiter_rad)/(earth_rad),2), "\n")
print("Jupiter-to-Earth Sun distance ratio:", round((jupiter_dis/earth_dis),2))
print("Sun-to-Jupiter volume ratio:", round((volume_s/volume_j),2))
print("Sun-to-Earth volume ratio:", round((volume_s/volume_e),2))
print("Jupiter-to-Earth volume ratio:", round((volume_j/volume_e),2),"\n")
print("Sun to Earth light travel time in minutes:", round(((earth_dis)/(lightspeed*60)),2))
print("Sun to Jupiter light travel time in minutes:",round(((jupiter_dis)/(lightspeed*60)),2))