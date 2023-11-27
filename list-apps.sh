#!/bin/sh

apps_dir="/usr/share/applications"

grep -s -l -e "\[Alterator Entry\]" $apps_dir/* |
	xargs grep -s -l -e "^\s*Type\s*=\s*Application" |
	xargs sed "/\[Alterator Entry\]/,\$!d" |
	sed -n -e "s/^\s*Name\s*=\s*\(.*\)/\1/p" |
	head -n 1
