# 3D-computer-vision-robotics-project

Intro about the project:
This project should handle/work with a huge bunch of datasets acquired from an agricultural robot, which surveyed the farm, where a variety of fruits are harvested.
The data collected by the robot on the fruits harvested are x,y,z axis(cartisean coordinates) of the fruits and r,g,b values (colour code)
The data collected by the robot is huge, around 9000 - 16000 lines of data collected on the fruits, out of this there's a single txt file, which contains data on hundreds of apples and there are around 250 txt files which contain 10000 - 16000 lines of data collected on each out of which there's just 1 apple per file

Aim:
The dateset containing the some apple has 12 columns, there are 6 unessential columns which need to be ignored during the process of finding the apples out of other fruits. Apart from it, these files contain many lines of either missing data(fruits partially occluded by leaves) or Unlabelled data. This needs to taken care of before starting the main objective of the project - data cleaning.

The main objective of this project is to find the apple out of the other fruits, provided the dataset containing the cartisean coordinates and colour codes of around 100000 fruits, as quickly as possible, so that robot can pick up the apples from the farm without any delay.

Implementation:
The dataset cleaning was done by dropping the unnecessary columns and missing rows,
where dropped as whole, as we don't want the robot to be stuck trying to collect the apple, without accurate data.
Calculations are cruicial in picking up the apple properly, without issue. Also this could cause some possible delay.
Finally labelling the dataset(columns) were done using an command to name the columns.

The apples were identified using both the cartesian coodinates and colour codes, 
there was some data provided on the apple harvested:
1. Apples harvested at the farm are of 60-100mm size.
2. The Apples are oval in shape.

Initially, it was planned to find the apples based on these two criteria, 
but later realized that finding the apple's shape with just Cartesian coordinates and colour codes,
would make the task more complicated and could cause overfitting.

Later decided to find the apple using its colour code, 
as there are majorly 4 types of apple based on colour; Red, Yellow, Greem and White.
Used the RGB values and compared it with the RGB values for each kind of apple's colour complexity.

Finally, decided to find the apple's size, 
by finding the fruit's volume, volume is the closest thing to the size of an object.
Assuming that every fruit is almost sphere, as there wasn't much details provided on the other fruits.
found the radius of the fruit using their cartesian coordinates and later used the formula to find the size of sphere on it.






