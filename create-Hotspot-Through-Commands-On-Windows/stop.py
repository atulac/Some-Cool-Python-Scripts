#Code Snippet to stop hotspot

from subprocess import call,check_output
call('netsh wlan stop hostednetwork',shell=True)
raw_input("press enter to exit ;)")
