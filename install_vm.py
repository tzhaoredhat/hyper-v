
# -*- coding : utf-8 -*-

"""Automatically install the guest os use ISO on Hyper-V server.

Execute this module will create a virtual machine in remote Hyper-V Server Host.

New VM config:
    VMName:             RHEL_AUTOMATION
    Memory:             1GB
    CPU core:           4
    Disk:               30GB (Dynamic expending)
    Generation:         1

Attention:
    When this script executed over,
    You may need refrash the host in your Hyper-V Manager to see the new installed guest.
"""

from xml_rpc_client import RunPowershell
import random

def install(path, vmname, kspath, isopath):
    """Install a vm in remote host.

    args:
        path: powershell scripts' path in remote Windows host.
        vmname: the name of vm you want create.
        kspath: kickstart load install iso file.
        isopath: the iso use to install vm. 
    """

    # Prevent namespace confilct
    postfix = str(random.randint(0,99))
    vmname = vmname + postfix

    para = path + vmname + kspath + isopath

    vmInstall = RunPowershell(para)
    vmInstall.run()


if __name__ == '__main__':

    path = 'C:/auto/ps/hyperv_install.ps1'
    vmname = ' RHEL_AUTOMATION'
    kspath = ' C:/iso/rhel_auto.iso'
    isopath = ' C:/iso/RHEL-6.7-20150603.0-Server-x86_64-dvd1.iso'

    install(path, vmname, kspath, isopath)

