import subprocess
import time


class Adb_Simplify:
    @staticmethod
    def devices():
        command = ['adb', 'devices']
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip().split('\n')[1:]
        devices = [line.split('\t')[0] for line in output if line.endswith('\tdevice')]
        return devices

    @staticmethod
    def screenshot(device_id, save_path):
        command = f"adb -s {device_id} shell screencap -p"
        result = subprocess.run(command, capture_output=True)
        with open(save_path, 'wb') as file:
            file.write(result.stdout)

    @staticmethod
    def start_activity(device_id, package, activity):
        command = f"adb -s {device_id} shell am  start -n {package}/{activity}"
        subprocess.run(command)

    @staticmethod
    def click(device_id, x, y):
        command = f"adb -s {device_id} shell input tap {str(x)} {str(y)}"
        subprocess.run(command)

    @staticmethod
    def call(device_id, number, duracao=3):
        subprocess.run(f"adb -s {device_id} shell am start -a android.intent.action.DIAL")
        time.sleep(1)
        subprocess.run(f"adb -s {device_id} shell input text {number}")
        subprocess.run(f"adb -s {device_id} shell input keyevent 5")
        time.sleep(duracao)
        subprocess.run(f"adb -s {device_id} shell input keyevent 6")

