What is this
------------

This package provides a modprobe configuration file for hid_apple which
reverses the behavior of media and function keys and fixes tilde mapping.

I'm building and using it on a Red Hat Enterprise Linux 7 / CentOS 7 platform
but should work with Fedora as well.


Manual configuration
--------------------

Alternatively you can add the following to a startup script

	echo 2 > /sys/module/hid_apple/parameters/fnmode
	echo 0 > /sys/module/hid_apple/parameters/iso_layout
