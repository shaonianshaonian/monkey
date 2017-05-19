:loop
adb -s 192.168.12.101:5555 shell monkey  -p honc.td --monitor-native-crashes  --pct-touch 93 --pct-motion 7 --pct-nav 0 -s %random% -vv  --throttle 500 320000 >D:\monkey\%random%.log
@ping -n 15 127.1 >nul
adb -s 192.168.12.101:5555 reboot
@ping -n 120 127.1 >nul
@goto loop