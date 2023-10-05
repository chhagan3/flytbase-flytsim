mport time
from flyt_python import api


drone = api.navigation (timeout=120000) 

time.sleep(3)

print 'taking off'
drone.take_off(10.0)

print ' going along the setpoints'
drone.position_set(8.0, 6.0, 5, relative=True)
drone.position_set(-8.0, 6.0, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)
drone.land(async=False)

print 'Landing'
drone.disconnect()

