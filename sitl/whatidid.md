# Connecting PX4 SITL (WSL) with QGroundControl on Windows

This guide documents how I configured **PX4 SITL** running in **Windows Subsystem for Linux (WSL)** to successfully connect with **QGroundControl (QGC)** running on my local Windows machine.

---

## 1. Port Forwarding Setup

First, I enabled port forwarding between WSL and Windows to allow UDP communication on **port 14550** — the default MAVLink port used by QGroundControl.
Can be done in any Windows terminal.

## 2. Enabling MAVLink Broadcasting

Next, I modified the px4-rc.mavlink configuration file to enable UDP broadcasting.
This was intended to make PX4 broadcast MAVLink messages rather than send them only to localhost.
Don't know if this made a difference or not. Included this step regardless.

## 3. Running PX4 SITL

Ran the following command in WSL terminal
```terminal
make px4_sitl gz_x500
```
At this point, i began getting no GCS connection errors. I ran the following command in mavlink terminal
```
mavlink start -u 14560 -r 4000 -t <WSL_IP> -p 14550
```
After this, the connection between QGC and PX4 was created and I could begin sending commands to takeoff and land the drone.

