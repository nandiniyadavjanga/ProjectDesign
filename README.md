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
We are working on the data which gives information about the mobile appications. While many public datasets (on Kaggle and the like) provide Apple App Store data, there are not many counterpart datasets available for Google Play Store apps anywhere on the web. 
## DataSource: 
Our data has 13 columns and 10842 rows. The volume of data is 9MB. It is structured data set available in CSV format. The data is clean and not messy. The velocity of dataset is slow as it is updated yearly. From the dataset we can know which category of applications are in demand.
- [Link to DataSource](https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv)







## Big Data Problem(Chaitra Vemula)
For each Category, I will find the Count of records.
## Big Data Solution(Chaitra Vemula)
1. Mapper input: One line of data that mapper read:
   - Photo Editor & Candy Camera & Grid & ScrapBook	ART_AND_DESIGN	4.1	159	19M	10,000+	Free	0	Everyone	Art & Design	43107	1.0.0	   4.0.3 and up	
2. Mapper output/Reducer input: example of an intermediate key,value pair output by mapper
      * ART_AND_DESIGN                Paint Splash!  
      * ART_AND_DESIGN        Popsicle Sticks and Similar DIY Craft Ideas
      * ART_AND_DESIGN        Canva: Poster, banner, card maker & graphic design
      * ART_AND_DESIGN        Install images with music to make video without Net - 2018
      * ART_AND_DESIGN        Little Teddy Bear Colouring Book Game
      * ART_AND_DESIGN        How To Draw Food
      * AUTO_AND_VEHICLES     Monster Truck Stunt 3D 2019
      * AUTO_AND_VEHICLES     Real Tractor Farming
      * AUTO_AND_VEHICLES     Ultimate F1 Racing Championship
      * AUTO_AND_VEHICLES     Used Cars and Trucks for Sale

3. Reducer output:  example of a final key, value pair output by reducer.
   - Category = ART_AND_DESIGN     Count of records = 49
   
4. Chart I will use to display results
   - I will use Bar Chart to display my results.

## Big Data Problem(Abhishek Telugu)
For each Category, I will find minimum of their rating.
## Big Data Solution(Abhishek Telugu)
1. Mapper input: One line of data that mapper read:
   - Photo Editor & Candy Camera & Grid & ScrapBook	ART_AND_DESIGN	4.1	159	19M	10,000+	Free	0	Everyone	Art & Design	43107	1.0.0	   4.0.3 and up	
2. Mapper output/Reducer input: example of an intermediate key,value pair output by mapper
      * ART_AND_DESIGN        4.1
      * ART_AND_DESIGN        3.9
      * ART_AND_DESIGN        4.7
      * ART_AND_DESIGN        4.5
      * ART_AND_DESIGN        4.3
      * ART_AND_DESIGN        4.4
      * AUTO_AND_VEHICLES     3.8
      * AUTO_AND_VEHICLES     4.1
      * AUTO_AND_VEHICLES     4.4
      * AUTO_AND_VEHICLES     4.7

3. Reducer output:  example of a final key, value pair output by reducer.
   - Category = ART_AND_DESIGN     minimum of rating = 3.2
   
4. Chart I will use to display results
   - I will use Bar Chart to display my results.

