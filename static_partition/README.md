# WHAT IS PARTITIONING OF HARD DISK?
It is the concept in which a given hard disk is divided into segments of secondary storage, so that each segment is managed separately. This is also done with a view that if damage is caused to one segment, like in cases of complete deletion of data, the damage is not transferred to the entire disk. It rather remains confined to that particular segment.
## MAJOR STEPS INVOLVED IN CREATING A PARTITION
Three major steps are involved are:
- Create
- Format
-	Mount
CREATING
You need to have a harddisk attached.
```fdisk -l```
This command shows you the list of all attached disks.
In the picture below, you can see I have a harddisk of size 3 GiB attached to my OS named /dev/sdb.
```fdisk <drive_name>```  In my case fdisk /dev/sdb.
- This command creates the partition for you. The ‘n’ in the line 'Command (m for help):n' indicates that we are creating a new partition.
The hard disk is of size 10GB in total, But I want to make use of 3GB so I will input +3G.
w: to save the changes made to the partition.
## FORMATTING
```mkfs.ext4 <drive_name>```
In my case **mkfs.ext4 /dev/sdb**
Above command is used to format the partition.
## MOUNTING
Create a new directory , I created /home/dvd.
```mount /dev/sdb1 /home/dvd```
In order to mount the partition to home/dvd .
```df -hT```
To check the successful mounting of the partition.
- cd /home/dvd: change the directory.
Within the directory create a file , I created data.txt.
Now comes our main task which is to increase or decrease the size of the static partition.
For accomplishing this task, we need to first unmount it , using command:
umount /home/dvd
Confirm the same using df -hT.
```e2fsck -f /dev/xvdg1```
This command will check errors and will mark file system as clean.

## RESIZING
```resize2fs /dev/xvdg1 5G```
The above command resizes my partition to 5GB.
After unmounting you can see that no files exist, but don’t worry your files are safe. It’s not yet visible because once unmounted you need to mount it again.

Similarly we can decrease the size .
Suppose we want to decrease from 3GB in the initial to 1GB, we need to follow the same steps as above.
Only a small change, during resizing :
```resize2fs /dev/xvdg1 1G```

