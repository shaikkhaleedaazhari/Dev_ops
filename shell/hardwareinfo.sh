echo "-------------"
echo "Hardware Info"
lshw
echo "-------------"
echo "CPU Info"
lscpu
echo "-------------"
echo "Memory Info"
free -m
echo "-------------"
echo "Disk Info"
df -h
echo "-------------"
echo "Network Info"
ifconfig
echo "-------------"
echo "username"
uname -a
echo "-------------"
echo "disk info"
lsblk
echo "-------------"
echo "memory info"
cat /proc/meminfo


