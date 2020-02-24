# ProjectDesign
## Project Name: ProjectDesign
### Project Number: 04
### Participants:
1. Nandini Yadav Janga
1. Chaitra Vemula
1. Abhishek Telugu

### Course Description: Through this course we can analyse very big data using Map-Reduce approach.Through Map-Reduce we can take out the columns we want to analyse from the whole data using mapper and can perform some aggregate functions on those columns using reducer.

## Links:
1. [GitHub Project Link](https://github.com/nandiniyadavjanga/ProjectDesign)
1. [GitHub Issue Tracker](https://github.com/nandiniyadavjanga/ProjectDesign/issues)

## Introduction: 
We are working on the data which gives information about the list of accidents handled by Barcelona police, incorporates the number of injuries by severity, the number of vehicles and the point of impact.

## DataSource: 
Our data has 11 columns and 10339 rows. The volume of data is 1.69MB. It is structured data set available in CSV format. The data is clean and not messy. The velocity of dataset is fast as it is updated monthly. From the datset we can know the impact of accidents on people in different districts by which proper measures can be taken to eradicate accidents in the future.
- [Link to DataSource](https://www.kaggle.com/xvivancos/barcelona-data-sets#accidents_2017.csv)

## Requirements:
     - Install python3 version
     - Install visual studio code
     - Install power shell
     - Install MS Excel
  
 ## Sequence of steps for execution:
   - Select a structured data set from https://www.kaggle.com which is in csv format.
     - Make sure python is installed using command prompt as an administrator using command: choco install python -y
     - Create mapper and reducer python files for each problem and write appropriate code corresponding to mapper and reducer.
     - In the project folder right click and then click open powershell here as administrator.
     - In powershell write command : python 1mapper.py
     - After running 1mapper.py, run 3reducer.py file using command: python reducer.py
     - Solution for the problem will be saved in 03.txt file as we used the project provied by Dr.Case as reference.
     - Copy the text from the 03.txt file and paste it in excel sheet.
     - Select the data in excel sheet and go to insert to generate graph or chart.
     - Select a best suitable graph type and generate the graph for the corresponding data.

## Big Data Problems
### Nandini Yadav Janga
1. For each district, I will find the sum of victims. 
2. Big Data Solution
   1. Mapper input: One line of data that mapper read:
     - 2017S001190  Nou Barris  Monday  February  13  11  Morning  1	  0	1	3

   2. Mapper output/Reducer input: example of an intermediate key,value pair output by mapper
    * Ciutat Vella	1
    * Ciutat Vella	1
    * Eixample	1
    * Ciutat Vella	0
    * Ciutat Vella	1

  3. Reducer output:  example of a final key, value pair output by reducer.
     - Ciutat Vella	634
  4. Chart I will use to display results
     - I will use clustered column chart to display my results.
     ![Clustered Column Chart](https://github.com/nandiniyadavjanga/ProjectDesign/blob/master/sum-of-victims/screenshots/Sumofvictimschart.PNG)
### Chaitra Vemula
1. For each Month, I will find the average of victims. 
2. Big Data Solution
   1. Mapper input: One line of data that mapper read:
     - 2017S001190  Nou Barris  Monday  February  13  11  Morning  1	  0	1	3

   2. Mapper output/Reducer input: example of an intermediate key,value pair output by mapper
    * October         2
    * September       2
    * December        5
    * July            1
    * May             1
    * September       1

  3. Reducer output:  example of a final key, value pair output by reducer.
     - April	0.027218934911242602
   4. Chart: I will use to display results
     - I will use Line Chart to display my results.
     
   ![Clustered Column Chart](https://github.com/nandiniyadavjanga/ProjectDesign/blob/master/average-of-victims/screenshots/Chart.PNG)

### Abhishek Telugu
1. For each Month, I will find the maximum of victims. 
2. Big Data Solution
   1. Mapper input: One line of data that mapper read:
     - 2017S001190  Nou Barris  Monday  February  13  11  Morning  1	  0	1	3

   2. Mapper output/Reducer input: example of an intermediate key,value pair output by mapper
   
    * October	2
    * September	2
    * December	5
    * July	1
    * May	1
    * September	1
    * May	1

  3. Reducer output:  example of a final key, value pair output by reducer.
     - May	6.0
   4. Chart I will use to display results
     - I will use Bar Chart to display my results.

