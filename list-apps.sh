#!/bin/sh

apps_dir="/usr/share/applications"

grep -s -l -e "\[Alterator Entry\]" $apps_dir/* |
	xargs grep -s -l -e "^\s*Type\s*=\s*Application" |
	xargs sed -n -e "s/^\s*Name\s*=\s*\(.*\)/\1/p"
