#Code Snippet to show the status and present configuration of running hotspot

from subprocess import call,check_output
call('netsh wlan show hostednetwork',shell=True)
raw_input("press enter to exit ;)")
