#!/bin/bash

echo -n "You are about to install a new conky, this will overwrite files at ~/.conky/conky-fsociety/ if similar files exist $1 [Y/n]: "
  read -r answer
if [[ "$answer" == [Yy] ]]; then
	pkill conky
	mkdir ~/.conky > /dev/null 2>&1
	mkdir ~/.conky/conky-fsociety/ > /dev/null 2>&1
	cp {fsocietyrc,mr.robot.png,clocks.lua,reddit.py,posts.txt} ~/.conky/conky-fsociety > /dev/null 2>&1
	touch ~/.conky/conky-fsociety/posts.txt
	echo "Success"
fi
