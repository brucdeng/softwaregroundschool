# Connecting PX4 SITL (WSL) with QGroundControl on Windows

This guide documents how I configured **PX4 SITL** running in **Windows Subsystem for Linux (WSL)** to successfully connect with **QGroundControl (QGC)** running on my local Windows machine.

---

## 1. Port Forwarding Setup

First, I enabled port forwarding between WSL and Windows to allow UDP communication on **port 14550** — the default MAVLink port used by QGroundControl.
Can be done in any Windows terminal.

## 2. Enabling MAVLink Broadcasting

Next, I modified the px4-rc.mavlink file to enable UDP broadcasting.
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
After this, the connection between QGC and PX4 was created and I could begin sending commands to takeoff and land the drone. One key thing I noticed was that after running the command above, I ran
```
mavlink status
```
And saw that broadcasting was enabled for the instance of mavlink I connected to
```
instance #3:
        GCS heartbeat valid
        mavlink chan: #3
        type:           GENERIC LINK OR RADIO
        flow control: OFF
        rates:
          tx: 2577.7 B/s
          txerr: 0.0 B/s
          tx rate mult: 1.000
          tx rate max: 4000 B/s
          rx: 41.8 B/s
          rx loss: 91.3%
        Received Messages:
          sysid:255, compid:190, Total: 648 (lost: 59133)
        FTP enabled: NO, TX enabled: YES
        mode: Normal
        Forwarding: Off
        MAVLink version: 2
        transport protocol: UDP (14560, remote port: 14550)
        Broadcast enabled: YES
        partner IP: 172.23.16.1
        ping statistics:
          last: 0.00 ms
          mean: 0.00 ms
          max: 0.00 ms
          min: 0.00 ms
          dropped packets: 0
```



