# ProjectDesign
## Project Name: ProjectDesign
### Project Number: 04
### Participants:
1. Nandini Yadav Janga
1. Chaitra Vemula
1. Abhishek Telugu
## Links:
1. [GitHub Project Link](https://github.com/nandiniyadavjanga/ProjectDesign)
1. [GitHub Issue Tracker](https://github.com/nandiniyadavjanga/ProjectDesign/issues)
## Introduction: 
We are working on the data which gives information about the list of accidents handled by Barcelona police, incorporates the number of injuries by severity, the number of vehicles and the point of impact.
## DataSource: 
Our data has 11 columns and 10339 rows. The volume of data is 1.69MB. It is structured data set available in CSV format. The data is clean and not messy. The velocity of dataset is fast as it is updated monthly. From the datset we can know the impact of accidents on people in different districts by which proper measures can be taken to eradicate accidents in the future.
- [Link to DataSource](https://www.kaggle.com/xvivancos/barcelona-data-sets#accidents_2017.csv)

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
   4. Chart I will use to display results
     - I will use Bar Chart to display my results.
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

