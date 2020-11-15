import lvm

input("read drives")
status_report=lvm.attached_drive_report()
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")

input("create_pv")
status_report=lvm.create_physical_volume("/dev/sdb")
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")

input("create_vg")
status_report=lvm.create_volume_group("vg1","/dev/sdb")
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")

input("display_vg")
status_report=lvm.display_volume_group()
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")

input("create logical volume")    
status_report=lvm.create_logical_volume("vg1","lv1","2")
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")


input("format logical volume")    
status_report=lvm.format_logical_volume("/dev/vg1/lv1")
if status_report[0] == 0:
    print(status_report[1])
else:
    print("failed to execute the command")

input("mount lv")
status_report=lvm.mount_logical_volume("/root/lv1dir","/dev/vg1/lv1")
if status_report[0] == 0:
    print(status_report[1])
else:
    print(status_report[1])
