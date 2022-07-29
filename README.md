# assign_room


[BizPro](https://bizpro.mystrikingly.com/) is a National Taiwan University club which aims to research on business studies with people in different fields and talent.
A Career Conference, with 170 attendees, is held by BizPro on Zoom cloud meeting at 7/23. 

Two times of people participated in the conference compared to the previous conference; therefore, if we manually asign the Zoom breakout rooms, it would be time consuming and cause chaos. How to effectively assign the participants into breakout rooms is the problem the scripts would like to solve.

In Zoom, you could provide the csv file to pre-assign the breakout rooms. The format is as follows:

|pre-assign room  |Email            |
|-----------------|-----------------|
|Room1            |example1@zoom.us |
|Room2            |example2@zoom.us |
|...              |...              |

The script `assign.py` + `zoom_create_room.py` could help you pre-assign the breakout rooms. Feel free to use it in different ocassions.
Number of people in different room would be nearly equal.
