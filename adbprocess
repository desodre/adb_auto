import subprocess

class adb_device:
        
    output = subprocess.check_output('adb devices', shell=True).decode('utf-8')
    lines = output.strip().split('\n')[1:]
    devices = [line.split('\t')[0] for line in lines]
    
    def __init__(self, index):
        self.index = index

    def __str__(self):
        if self.index != None:
            return self.devices[self.index]
        else:
            print(f'all devices: {self.devices}')


def open_activity(activity, dispositivo = None):
    if dispositivo == None:
        subprocess.call(f'adb shell am start -a {activity}')
    else:
        subprocess.call(f'adb {dispositivo} shell am start -a {activity}')


def phantomTouch(x ,y):
    subprocess.call(f"adb shell input tap {x} {y}")

    
