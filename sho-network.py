#!/usr/bin/python

import shodan
# insert key 
SHODAN_API_KEY = "your key here"
api = shodan.Shodan(SHODAN_API_KEY)
# open output file
outfile = open("shodan-ruan.txt", "w") 

# set network to shodan
network = '12.22.148.'
# set address range
for num in range(1,254):
	ip = (network) + str(num)
#	print ip
	try:
		# Lookup the host
		host = api.host(ip)
		print """
	    	    IP: %s
	        	Organization: %s
	        	Operating System: %s
		""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
		outfile.write ("""
	    	    IP: %s
	        	Organization: %s
	        	Operating System: %s
		""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
		# Print all banners
		for item in host['data']:
   			    print """
       			        Port: %s
           			    Banner: %s
   	    		""" % (item['port'], item['data'])
   	   	outfile.write("""
       	    	    Port: %s
       	    	    Banner: %s
   	    		""" % (item['port'], item['data']))	
	except Exception, e:
			print 'Error: %s' % e
    	pass
	num += 1
outfile.close()
