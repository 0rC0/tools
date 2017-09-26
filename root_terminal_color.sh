#!/bin/bash

#Source https://lifehacker.com/5195951/use-a-different-color-for-the-root-shell-prompt

#---------------
function change_root_terminal_color(){
	local color="PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '"
	echo $color >> /root/.bashrc
}

#Check if I'm root
if ! [ $(id -u) = 0 ]; then
   echo "The script has to be run as root"
   exit 1
else
   change_root_terminal_color
fi
