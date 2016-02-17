
# -*- coding: utf-8 -*-

"""This class extends pexpect.spawn to specialize setting up SSH connections.
This adds methods for login, logout, and expecting the shell prompt.
It does various tricky things to handle many situations in the SSH login process.
if the session is your first login, then pxssh automatically accepts the remote certificate;
or if you have public key authentication setup then pxssh won’t wait for the password prompt.

Attention:
    If the ssh connection be forced closed by remote host(for example remote host reboot),
    it will raise a pexpect.EOF error and end running the scripts, so if needed please catch the 
    pexpect.EOF error.
"""

import pxssh
import sys
import pexpect

class autoSSH(object):
    """Simulation ssh login, logout, run command."""
    
    def __init__(self, hostname, username, passwd ,commands=[]):
        self.hostname = hostname
        self.username = username
        self.passwd = passwd
        self.commands = commands

    
    def login_and_out(func):
        """This is a decorator in class. For SSH login and logout."""

        def run(self, cmd=False):

            try:
                # Create a object of class pxssh use its constructor
                child = pxssh.pxssh()
                child.login(self.hostname, self.username, self.passwd, original_prompt='[#$>]')

                func(self,cmd,child)

                child.logout()

            except pxssh.ExceptionPxssh as err:
                print str(err)
            except pexpect.EOF as e:
                print str(e)
    
        return run

        

    
    @login_and_out
    def run(self, cmd=False, child=None):
        """This is a middle func between the decorator and command func."""

        if cmd: 
            self.ssh_cmd(child,self.commands)
        else:
            print 'Just Login and logout!'


    def ssh_cmd(self,child,commands):
        """Runs the command in remote host automatically.

        Overwrite this func to use it.
        Following is just a demo.
        """

        for cmd in commands:
            child.sendline(cmd)
            if child.prompt():
                print 'Command [%s] run successful!' % cmd
                print 'Following is stdout:'
                print '----------------------------------'
            else:
                print 'Command %s run timeout' % cmd
            
            print child.before



if __name__ == '__main__':
    a = ['ls','ls -al','ifconfig','ps','mv mylog.txt a.txt']
    test = autoSSH('10.66.108.196', 'root', 'redhat',a)
    test.run(True)

