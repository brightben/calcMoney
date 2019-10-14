#!/bin/bash

find . -name "*.zip" |
while read filename
do
  if [[ "$filename" != *"test.zip"* ]]
  then
    unzip -o -d "`dirname "$filename"`" "$filename"
  fi
done
