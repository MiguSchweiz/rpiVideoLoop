#!/bin/bash
sudo apt-get update
sudo apt-get install kodi

echo "copy Videos to /home/pi/Videos"
echo "Press Any key to continue"
read

cd /home/pi/Videos
rm pl.m3u
ls >pl.m3u
cd /home/pi/rpiVideoLoop

mkdir -p /home/pi/.kodi/userdata/
cp autoexec.py /home/pi/.kodi/userdata/

cp videoloop.sh /home/pi/

sudo cp videoloop.service /etc/systemd/system/videoloop.service
sudo systemctl enable videoloop.service
sudo systemctl start videoloop.service


