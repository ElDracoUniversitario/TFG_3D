#!/bin/bash

for f in *.png; do
  if $f != "negro.png"
  then
    pngtopnm $f | ./ppmtorgb565 > /dev/fb0
    sleep 5s
    pngtopnm negro.png | ./ppmtorgb565 > /dev/fb0
    sleep 5s
  fi
done
