from gpiozero import RGBLED
import psutil, time

led = RGBLED(14, 15, 18)

def get_disk_percent(interval=0.5):
    t1 = psutil.disk_io_counters().busy_time
    time.sleep(interval)
    t2 = psutil.disk_io_counters().busy_time
    return (t2 - t1) / (interval * 1000) * 100

while True:
    cpu = psutil.cpu_percent(interval=0.1)
    print("cpu: ", cpu)
    r = cpu / 100.0
    g = 1 - r

    disk_percent = get_disk_percent(interval=0.2)
    print("disk_percent: ", disk_percent)

    if disk_percent < 25:
        b = 0.0
    elif disk_percent < 75:
        b = 0.5
    else:
        b = 1.0

    led.color = (r, g, b)
    time.sleep(0.1)


