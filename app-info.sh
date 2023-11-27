#!/bin/sh

[ $# -ne 1 ] && echo "Usage: $0 <app-name>" && exit 1

apps_dir="/usr/share/applications"
app=$(echo "$1" | xargs)

tmpfile=$(mktemp /tmp/alterator-global-app-info.XXXXXX)
grep -s -l -e "\[Alterator Entry\]" -r $apps_dir >$tmpfile

while read -r file; do
	name=$(sed "/\[Alterator Entry\]/,\$!d" "$file" |
		sed -n -e "s/^\s*Name\s*=\s*\(.*\)/\1/p" |
		head -n 1 |
		xargs)

	[ "$name" = "$app" ] && cat $file && exit 0
done <$tmpfile

exit 1
