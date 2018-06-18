'''
-- Description: 
    dig command is passed with DNS server IP address. This will return list of IP addresses to be blocked.
    IP addresses are matched using regex module and passed to the iptables class which takes care of the blocking.
    Given IP addresses are DROPPED and not REJECTED because REJECTION sends a message to the user that the packets have been dropped.

-- ARGS:

-- ASSUMPTIONS:
    1. Given that the script will run every minute, it is assumed to be triggred by CRON or similar application
    2. If not cron, main loop can be initiated within a while loop and a time.sleep() of 1 minute

-- USAGE:
    sudo python assignment.py

-- Author:
    Swapnasheel Sonkamble (swar.1318@gmail.com) 

-- TO DO:
    1. Python future library implementation - environment friendly

-- NOTES:

'''


#!/usr/bin/env python

import subprocess
import re

class Parse():

    def __init__(self):
        pass

    def get_process_out(self, command):
        args = command.split()
        try:
            p_out = subprocess.check_output(args)
        except Exception as err:
            print err
        return p_out

    def parse_ip_addresses(self, string):
        # Pattern to get IP addresses
        pattern = "(A\\t((\d{1,3}\.){3}\d{1,3}))"
        # Valid pattern to get IP addresses (considering the range of IP addressing)
        # pattern = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        ip_add = [i[1] for i in re.findall(pattern, string)]
        return ip_add


class ModifyRules():

    def __init__(self):
        pass

    def check_if_rule_exists(self, ip_add):
        command = "sudo iptables -L INPUT -v -n | grep "
        for j in ip_add:
            try:
                ps = subprocess.Popen(command + j, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = ps.communicate()[0]
            except Exception as err:
                print err
            if out == '':
                rule = subprocess.Popen(['sudo', 'iptables', '-A', 'INPUT', '-s', '%s'%j, '-j', 'DROP'], stdout=subprocess.PIPE)

    def flush(self):
        cmd = "sudo iptables -F"
        ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return


def Main():
    dig_command = 'dig @54.175.23.149 acls.threatstop.local'
    p = Parse()
    string = p.get_process_out(dig_command)
    ip_add = p.parse_ip_addresses(string)

    m = ModifyRules()
    m.check_if_rule_exists(ip_add)


if __name__ == "__main__":
    Main()


