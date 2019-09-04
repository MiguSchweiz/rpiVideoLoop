import xbmc,time,os,commands
xbmc.executebuiltin("PlayMedia(/home/pi/Videos/pl.m3u)")
xbmc.executebuiltin("PlayerControl(repeatall)")
xbmc.executebuiltin("SetVolume(100)")

os.system('sudo echo "4" > /sys/class/gpio/unexport')
os.system('sudo echo "4" > /sys/class/gpio/export')
os.system('sudo echo "in" > /sys/class/gpio/gpio4/direction')


run=1
while run==1:
	status, output = commands.getstatusoutput("sudo cat /sys/class/gpio/gpio4/value")
	if "0" in output:
		xbmc.executebuiltin("PlayMedia(/home/pi/Videos/pl.m3u)")
		xbmc.executebuiltin("PlayerControl(repeatall)")
		xbmc.executebuiltin("SetVolume(100)")
		xbmc.executebuiltin("ActivateWindow(fullscreenvideo)")
		time.sleep(15)
	else:
		time.sleep(.1)
	
