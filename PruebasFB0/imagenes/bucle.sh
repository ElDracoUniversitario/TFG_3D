#!/bin/bash

for f in *.png; do
  if [ "$f" != "negro.png" ]; then
    pngtopnm $f | ./ppmtorgb565 > /dev/fb0
    sleep 1s
    ./negro
    sleep 1s
  fi
done
