ThreatSTOP
============

Script to query dig command, parse IP addresses, and block/ update IPTABLES rules
------------------

File List
-----
.:
README.md  
src/  
src/assignment.py  
src/test.py  

How to run file
----

* sudo python assignment.py
* sudo python test.py


Assumptions
----
1. Given that the script will run every minute, it is assumed that the script will be triggred by CRON or similar application
2. If not cron, then a while loop can be written that will run after time.sleep() of 1 minute
3. Script only runs on Python2.7 and not on Python3. To install python2.7 on a linux device, you can use "sudo apt install python"
4. Unittest module required for testing
5. Blocked IP addresses work only for A records. Blocked IP addresses are DROPPED and not REJECTED


