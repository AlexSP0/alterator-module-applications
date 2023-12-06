#!/bin/sh -e

apps_dir="/usr/share/alterator/applications"

grep -s -l -e "\[Alterator Entry\]" -r $apps_dir | while read -r file; do
	sed "/\[Alterator Entry\]/,\$!d" "$file" |
		sed -n -e "s/^\s*Name\s*=\s*\(.*\)/\1/p" |
		head -n 1
done
