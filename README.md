Prerequesties:
```
#install python3
apt install python3
```
Start the program using the below command
```
python3 main.py
```
Usage
```
$ create_parking_lot 4
Created a parking lot with 4 slots
$ park TN-52-HH-3214 Green
Allocated slot number: 1
$ park TN-52-AB-4211 Purple
Allocated slot number: 2
$ park TN-52-SL-7563 Brown
Allocated slot number: 3
$ park TN-52-RM-5857 Black
Allocated slot number: 4
$ park CH-52-GG-3274 AppleGreen
Sorry, parking lot is full
$ leave 3
Slot number 3 is free
$ status
Slot No.    Registration No    Colour
1           TN-52-HH-3214      Green
2           TN-52-AB-4211      Purple
4           TN-52-RM-5857      Black
$ park MH-56-RM-3827 Yellow
Allocated slot number: 3
$ park KA-15-FD-4726 White
Sorry, parking lot is full
$ registration_numbers_for_cars_with_colour Yellow
MH-56-RM-3827
$ slot_numbers_for_cars_with_colour Purple
2
$ slot_number_for_registration_number TN-52-RM-5857
4
$ slot_number_for_registration_number OR-57-JK-4932
Not found
$ exit
```
