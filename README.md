# hyper-v
# Quick start guide
# Install vm
# Make sure you have install the python module pexpect

    $ sudo easy_install pexpect

or

    $ sudo pip install pexpect
# Download file /hypervbolic/install_vm.py and run it.

# Attention: You may need refresh the host in you Hyper-V Manager.Hotplug SCSI disk and test if it work normal

# 1.Download file /hypervbolic/Hotplug_SCSI_Test.py and run it.
# We build a XML-RPC Server and Client for Interactive between with Linux and Windows, undoubtedly we use ssh to run our command in remote Linux host(More accurately it is a RHEL OS running in Hyper-V Server).

# Attention:

### The operate in Windows Hyper-V host usually can not finished in a single line command, so it better to run powershell command in a powershell script. XML-RPC Server just support running single line command.
Basic component

# XML-RPC Client (packaging the cmd and powershell command class and sent it to server, running in our Linux working machine)
# XML-RPC Server (a very short server and and run cmd and powershell command, runing in Hyper-V server)
# SSH login, logout, and expecting the shell prompt. (This module do various tricky things)

# Finished automation script

# Install vm in remote Hyper-V host
#  Hotplug a SCSI disk and check if it works normal
# Auto reboot a remote host(for boot error case)
