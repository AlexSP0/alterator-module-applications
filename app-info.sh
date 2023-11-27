#!/bin/sh

[ $# -ne 1 ] && echo "Usage: $0 <app-name>" && exit 1

apps_dir="/usr/share/applications"
app=$1

grep -s -l -e "\[Alterator Entry\]" -r $apps_dir | while read -r file; do
	name=$(sed "/\[Alterator Entry\]/,\$!d" "$file" |
		sed -n -e "s/^\s*Name\s*=\s*\(.*\)/\1/p" |
		head -n 1)

	[ "$name" = "$app" ] && cat $file && exit 0
done

exit 1
