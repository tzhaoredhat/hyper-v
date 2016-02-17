

# -*- coding : utf-8 -*-
import  xmlrpclib

"""A XML-RPC client

For runing the command in remote host like ssh.
This module will communicated with the XML-RPC-Server, send command to the server and let it run.
There a two class in the module, one for run cmd or shell command, another is for runing powershell cmd.
"""

class RemoteCmd(object):
    """Runing a commnad in remote shell

    Passed a command as the argument, it will return a stdout of remote shell, 
    such as 'ls -l' or 'ipconfig', 
    compatible with the Windows cmd/powershell & Linux shell.

    Attributes:
        hostIP: the IP of the host you want connected
        hostPort: the port used by the XML-RPC-Server runing in remote host. Default is 8888.
        server: a object connected with the xmlrpc server
    """

    def __init__(self, hostIP='10.66.106.48', hostPort=8888):

        self.hostIP = hostIP
        self.hostPort = str(hostPort)

        address = 'http://%s:%s' % (hostIP, hostPort)

        # Connected with the remote XML-RPC server
        self.server = xmlrpclib.ServerProxy(address)

    def RunCmd(self,userCmd):

        feedback = self.server.Command(userCmd)

        if feedback == '':
            print 'Command runing successfully!'
        else:
            print feedback


class RunPowershell(object):
    """Remote running a powershell script

    Passed one arguments: the powershell script's dirctory,it will return a stdout of remote powershell.
    such as 'C:/auto/ps/getHostInfo.ps1'

    Attributes:
        para: the powershell script's path and parameter you want run in remote host.
    """

    def __init__(self,para):
        self.para = para

    def run(self):

        cmd = 'powershell -file %s' % self.para
        print 'Remote host running: %s' % cmd
        
        ps_cmd = RemoteCmd()
        ps_cmd.RunCmd(cmd)


if __name__ == '__main__':

    print 'Input 1 for CMD, 2 for powershell command.'
    num = raw_input("CMD or powershell command?")
    cmd = raw_input("Input the command you want running: ")
    if num  == 1:
        test = RemoteCmd()
        test.RunCmd(cmd)
    elif num == 2:
        test = RunPowershell(para)
        test.run()
    else:
        print "Input error, rerun this script! "

    


    #para = 'C:/auto/ps/getHostInfo.ps1'
    #test = RunPowershell(para)
    #test.run()

