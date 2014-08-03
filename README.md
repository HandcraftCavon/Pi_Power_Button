# Raspberry Pi Power button
=========
![](http://i.imgur.com/3piCDkp.jpg)
### What you need:
1. A button
2. female header
3. A resister

### Step:
#### Process on Pi
1. unzip the zip
2. open /etc/rc.local with nano
	1. `sudo nano /etc/rc.local`
3. add codes below in front of the final line: `exit 0`
	`*`
	`sudo nohup python /home/pi/Pi_Power_Button/poweroffbut.py &`
	`sudo nohup python /home/pi/Pi_Power_Button/rebootbut.py &`
	` `
	`exit 0`
4. Ctrl + X to exit, remember to press y to save.
5. Reboot.
6. Circuit:
![](http://i.imgur.com/8QtKXr3.jpg)
