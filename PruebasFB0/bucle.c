for f in *.png; do
  pngtopnm $f | ./ppmtorgb565 > /dev/fb0
  sleep 5s
  pngtopnm negro.png | ./ppmtorgb565 > /dev/fb0
  sleep 5s
done
