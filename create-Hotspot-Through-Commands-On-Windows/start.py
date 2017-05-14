#Snippet to start hotspot from command prompt

from subprocess import call,check_output
call('netsh wlan set hostednetwork mode=allow ssid=YourHotspotName key=YourPassword',shell=True)

#ssid and key to be put as per one's own interest

call('netsh wlan start hostednetwork',shell=True)
raw_input("press enter to exit ;)")
