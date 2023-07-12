import subprocess as sb
import os
import xml.etree.ElementTree as ET

#demorei nisso aqui viu, mizera

def Devices():
    command = ['adb', 'devices']
    result = sb.run(command, capture_output=True, text=True)
    output = result.stdout.strip().split('\n')[1:]
    devices = [line.split('\t')[0] for line in output if line.endswith('\tdevice')]
    return devices


def Screenshot(devices: list, nome: str):
    for device in devices:
        local = sb.check_output(f"adb -s {device} ls sdcard/DCIM")

        #Aqui ele verifica se a pagina ja existe, se nao ele cria e tira o print do msm jeito

        if "adbScrenshots" in str(local):
            sb.run(f"adb -s {device} shell screencap sdcard/DCIM/adbScrenshots/{nome}.png")
            print("Print tirado com sucesso")
        else:
            print("Pasta adbScrenshots nao encontrada, sera criada atumaticamente")
            sb.run(f"adb -s {device} shell mkdir sdcard/DCIM/adbScrenshots")
            sb.run(f"adb -s {device} shell screencap sdcard/DCIM/adbScrenshots/{nome}.png")
            print("Print tirado com sucesso")

def Click(devices: list, x: int, y: int):
    for device in devices:
        sb.run(f"adb -s {device} shell input tap {x} {y}")


def getDeviceInfos(devices: list):
    for device in devices:
        model = (sb.run(f"adb -s {device} shell getprop ro.product.model", capture_output=True, text=True).stdout).strip()
        activated_id = (sb.run(f"adb -s {device} shell getprop ro.boot.activatedid", capture_output=True, text=True).stdout).strip()

        if os.path.exists(f"Projetos\{model}"):
            pass
        else:
            os.mkdir(f"{model}")
        
        if os.path.exists(f"Projetos\{model}\{activated_id}"):
            pass
        else:
            os.mkdir(f"Projetos\{model}\{activated_id}")

        os.system(f"adb -s {device} shell getprop >Projetos\{model}\{activated_id}\PropriedadesDispositivo.txt ")

def getIMEI(devices: list):
    for device in devices:
        sb.run(f"adb -s {device} shell input keyevent KEYCODE_CALL")
        sb.run(f"adb -s {device} shell input text '*#06#'")
        sb.run(f"adb -s {device} shell  uiautomator dump --compressed")
        sb.run(f"adb -s {device} pull /sdcard/window_dump.xml")

        with open("window_dump.xml", "r") as arquivo:
            primeira_linha = arquivo.readlines()

        root = ET.fromstring(primeira_linha)
        imei1_node = root.find(".//node[@text='IMEI1']")
        imei1 = imei1_node.tail.strip()
        print("IMEI1:", imei1)
        

getIMEI(Devices())

