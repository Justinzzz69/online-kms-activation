import os
import platform
import subprocess

schwanz = """
▓█████▄  █    ██     ██░ ██   ██████ 
▒██▀ ██▌ ██  ▓██▒   ▓██░ ██▒▒██    ▒ 
░██   █▌▓██  ▒██░   ▒██▀▀██░░ ▓██▄   
░▓█▄   ▌▓▓█  ░██░   ░▓█ ░██   ▒   ██▒
░▒████▓ ▒▒█████▓    ░▓█▒░██▓▒██████▒▒
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒     ▒ ░░▒░▒▒ ▒▓▒ ▒ ░
 ░ ▒  ▒ ░░▒░ ░ ░     ▒ ░▒░ ░made by hskys on discord
 ░ ░  ░  ░░░ ░ ░     ░  ░░ ░░  ░  ░  
   ░       ░         ░  ░  ░      ░  
 ░                                   
 [1]activate windows 10/11 [2]remove activation
 """


def main():
    print(schwanz)
    print("")
    check_all_dependencies()
    select = input(">>> ")

    if select == '1':
        activate_windows()
    elif select == '2':
        remove_windows()
    elif select == '3':
        whoamdeit()


def check_all_dependencies():
    version = platform.system() + ' ' + platform.release()
    print("Your Windows version: " + version)
    try:
        output = subprocess.check_output(['slmgr.vbs', '/xpr'], stderr=subprocess.STDOUT, shell=True)
        output_str = output.decode('utf-8').strip()
        return "The computer is permanently activated" in output_str
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False


def get_windows_edition():
    system = platform.system()
    release = platform.release()
    edition = platform.win32_edition()
    return f"{system} {release} {edition}"


def activate_windows():
    windows_edition = get_windows_edition()
    print(windows_edition + " is being activated now!")

    # Windows 11 activation
    if windows_edition == "Windows 11 Home":
        os.system('slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 11 Professional":
        os.system('slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 11 Education":
        os.system('slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 11 Enterprise":
        os.system('slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43B8YKP-D69TJ')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    # Windows 10 activation
    elif windows_edition == "Windows 10 Home":
        os.system('slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 10 Professional":
        os.system('slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 10 Education":
        os.system('slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 10 Enterprise":
        os.system('slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    # Windows 8.1 activation
    elif windows_edition == "Windows 8.1 Home":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8.1 Professional":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8.1 Education":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8.1 Enterprise":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    # Windows 8 activation
    elif windows_edition == "Windows 8 Home":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8 Professional":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8 Education":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 8 Enterprise":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    # Windows 7 activation
    elif windows_edition == "Windows 7 Home":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 7 Professional":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 7 Education":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()
    elif windows_edition == "Windows 7 Enterprise":
        os.system('slmgr /ipk')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        activation_ended()


def remove_windows():
    print("remove windows activation")
    os.system('slmgr /upk')


def activation_ended():
    print("Your Windows has been activated!")
    input("")
    main()


def whoamdeit():
    print("deine mudda")


if __name__ == "__main__":
    main()
