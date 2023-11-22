#!/bin/sh

[ $# -ne 1 ] && echo "Usage: $0 <app-name>" && exit 1

apps_dir="/usr/share/applications"
app=$1

file=$(find $apps_dir -type f -exec grep -l -e "^\s*Name\s*=\s*$app" {} \+)

[ -z $file ] && exit 1

cat $file
