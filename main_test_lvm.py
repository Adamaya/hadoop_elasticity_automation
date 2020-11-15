import lvm

print("""
    ################################
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
    ################################
""")
command_number=int(input("Enter the command number: "))
if command_number==1:
    status_report=lvm.attached_drive_report()
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==2:
    drive = input("enter the drive name: ")
    status_report=lvm.create_physical_volume(drive)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==3:
    vgname = input("enter the volume group name:")
    drive = input("enter the drive name: ")
    status_report=lvm.create_volume_group(vgname,drive)
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
    vgname = input("enter the volume group name:")
    lvname = input("enter the logical volume name: ")
    size = input("enter the extended volume size: ")
    status_report=lvm.create_logical_volume(vgname,lvname,size)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")


elif command_number==6:
    lvPath = input("enter the logical volume path: ")
    status_report=lvm.format_logical_volume(lvPath)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print("failed to execute the command")

elif command_number==7:
    mount_directory = input("enter the mount directory path: ")
    lvPath = input("enter the logical volume path: ")
    status_report = lvm.mount_logical_volume("/datanodedir","/dev/vg1/lv1")
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])

elif command_number==8:
    vgname = input("enter the volume group name:")
    lvPath = input("enter the logical volume path: ")
    status_report=lvm.extend_volume_group(vgname, lvPath)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])

elif command_number==9:
    vgname = input("enter the volume group name: ")
    lvname = input("enter the logical volume name: ")
    size = input("enter the extended volume size: ")
    status_report=lvm.extend_logical_volume(vgname, lvname, size)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])

elif command_number==10:
    lvpath = input("enter the logical volume path: ")
    status_report=lvm.format_extended_partition(lvpath)
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])

        
elif command_number==11:
    status_report=lvm.check_report()
    if status_report[0] == 0:
        print(status_report[1])
    else:
        print(status_report[1])
