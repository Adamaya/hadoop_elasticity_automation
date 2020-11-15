import lvm

print("""
    1. Display available hard drives
    2. Create Physical Volume
    3. Create Volume Group
    4. Display Volume Group
    5. Create Logical Volume
    6. Format logical Volume
    7. Mount Logical Volume
    8. Extend Volume Group
    9. Extend Logical Volume
    10. Format extended partition
    11. Hadoop Cluster Report
""")
command_number=int(input("Enter the command number: "))
if command_number==1:
    status_report=lvm.attached_drive_report()
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==2:
    status_report=lvm.create_physical_volume("/dev/sdb")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==3:
    status_report=lvm.create_volume_group("vg1","/dev/sdb")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==4:
    status_report=lvm.display_volume_group()
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==5:
    status_report=lvm.create_logical_volume("vg1","lv1","2")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")


elif command_number==6:
    status_report=lvm.format_logical_volume("/dev/vg1/lv1")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==7:
    status_report=lvm.mount_logical_volume("/datanodedir","/dev/vg1/lv1")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])
