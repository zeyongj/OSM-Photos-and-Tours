# README


**Simon Fraser University**

**CMPT 353 D100: Computational Data Science**

**Instructor: Dr. Greg Baker**

**Project Topic: OSM, Photos, and Tours**

**Group Doge**


## Background

1. This group, named "Doge", consists of Tian Xiao (txa11@sfu.ca), Yuqing Wu (ywa292@sfu.ca) and Zeyong Jin (zeyongj@sfu.ca).

2. The logo of this group is <img src="https://www.heredg.com/wp-content/uploads/2020/06/%C5%92%C2%A2%E2%80%93%E2%89%88%C3%95%C2%BA%E2%88%86%C2%A8_20200530192407.jpg" height="30" width="30">.

3. The topic of this group project is [OSM, Photos, and Tours](https://coursys.sfu.ca/2021su-cmpt-353-d1/pages/ProjectTour), check more information by clicking on the hyperlink.


## Data

1. The data is provided by the instructor, or collected online from WikiPedia and Statistics Canada.

## Libraries

This project uses the following libraries, ensure you have installed all the libraries to execute.

1. webbrowser

2. numpy

3. pandas

4. math

5. exifread

6. folium

7. sys

8. matplotlib

9. seaborn
 
10. warnings

11. os

12. urllib

13. bs4


## Instruction

1. We finished Questions 2: 
> I feel like there are some parts of the city with more chain restaurants (e.g. McDonald's or White Spot franchises, not independently-owned places): is that true? Is there some way to find the chain places automatically and visualize their density relative to non-chains?

Question 2 is done via the program of plot_density.py. You can also view the output directly via the Jupyer Notebook file of plot_density.ipynb. Further analysis is on the report.

2. We also completed Question 3: 
> If I was going to choose a hotel (or AirBnb), where should it be? What places have good amenities nearby? 

Question 3 is done via the program of airbnb_hotel.py. Further analysis is on the report.

3. Last, as of Question 4: 
> Any of these could be turned into big data problems by working with the global version of the data set. You can recreate that data as described above. 

We put forward the question about which cuisines are most welcomed in Vancouver, and based on the outcome we want to figure out whether nationality is a key factor that determines the most favourite cuisines in Vancouver. The analysis is on the report, supported by the program of plot_density.py. You can also view the output directly via the Jupyer Notebook file of plot_density.ipynb. 

## Structure

.idea

    inspectionProfiles

        profiles_settings.xml

    .gitignore

    misc.xml

    modules.xml

    osm-project.iml

    vcs.xml

    workspace.xml

code

    disassemble-osm.py

    just-vancouver.py

    osm-amenities.py

data

    .gitkeep
    
    Data_of_minority_1.csv

    amenities-vancouver.json

    amenities-vancouver.json.gz

    list_of_chain_restaurants.csv

    listings.csv


photo

    IMG_0029.JPG

    IMG_0030.JPG

    IMG_0031.JPG

    IMG_0033.JPG

    IMG_0037.JPG

    IMG_0039.JPG

    IMG_0044.JPG

    IMG_2628.JPG

    IMG_2641.JPG

    IMG_5861.JPG


results

    f1_density.jpg
    
    f2_chain.jpg

    f3_non-chain.jpg

    f4_amenities.jpg

    f5_top20.jpg

    f6_cuisine.jpg

    f7_piecuisine.jpg

    f8_citizenship.jpg

    f9_piecitizenship.jpg

    hotel.csv

    hotel_map.html

CHANGELOG.md

CONTRIBUTING.md

LICENSE

Project_Report_Group_Doge.pdf

README.md

airbnb_hotel.py

hotel_map.html

plot_density.ipynb

plot_density.py


## Execution

1. To run plot_density.py, type the following in the terminal: `python plot_density.py`.

    1.1 The program will generate a csv file of list_of_chain_restaurant.csv. You can directly view output from the folder of data, or via the Jupyter Notebook file of plot_density.ipynb. 

    1.2 The program will generate 9 JPG pictures, named from f1 to f9. You can directly view output from the folder of results, or via the Jupyter Notebook file of plot_density.ipynb. 
   
    1.3 The pictures would be saved on the folder of results.

2. To run airbnb_hotel.py, type the following in the terminal: `python airbnb_hotel.py photo/IMG_0029.JPG all`. 

   2.1 You can change  `IMG_0029.JPG` to any of JPG files in the photo folder.

   2.2 `all` can be changed to any integer, since `price` is integer in the "listings.csv" file.  
   
   2.3 The program will generate a html file of hotel_map.html as well as a csv file of hotel.csv. You can directly view the hotel_map.html via a web browser from the folder of results. After execution, the system would also open the hotel_map.html automatically for you.

## Contribution

1. Yuqing Wu (ywa292@sfu.ca) and Zeyong Jin (zeyongj@sfu.ca) were responsible for Questions 2 and 4.

2. Tian Xiao (txa11@sfu.ca) finished the part of Question 3.

3. Tian Xiao (txa11@sfu.ca), Yuqing Wu (ywa292@sfu.ca) and Zeyong Jin (zeyongj@sfu.ca) wrote the report by cooperation.

## Versions

1. This project was created on July 24th, 2021.

2. This project was last modified and submitted to the CSIL GitLab platform on August 13th, 2021.


## License

1. This work is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) (or any later version).

    `SPDX-License-Identifier: Apache-2.0-or-later`

## Disclaimer

This repository is ONLY for backup. Students should NEVER use this repository to finish their works, IN ANY WAY.

It is expected that within this course, the highest standards of academic integrity will be maintained, in
keeping with SFU’s Policy S10.01, `Code of Academic Integrity and Good Conduct`.

In this class, collaboration is encouraged for in-class exercises and the team components of the assignments, as well
as task preparation for group discussions. However, individual work should be completed by the person
who submits it. Any work that is independent work of the submitter should be clearly cited to make its
source clear. All referenced work in reports and presentations must be appropriately cited, to include
websites, as well as figures and graphs in presentations. If there are any questions whatsoever, feel free
to contact the course instructor about any possible grey areas.

Some examples of unacceptable behaviour:
- Handing in assignments/exercises that are not 100% your own work (in design, implementation,
wording, etc.), without a clear/visible citation of the source.
- Using another student's work as a template or reference for completing your own work.
- Using any unpermitted resources during an exam.
- Looking at, or attempting to look at, another student's answer during an exam.
- Submitting work that has been submitted before, for any course at any institution.

All instances of academic dishonesty will be dealt with severely and according to SFU policy. This means
that Student Services will be notified, and they will record the dishonesty in the student's file. Students
are strongly encouraged to review SFU’s Code of Academic Integrity and Good Conduct (S10.01) available
online at: http://www.sfu.ca/policies/gazette/student/s10-01.html.


## Epilogue

1. Group Doge presents its compliments to the instructor Dr. Baker and teaching assistants in the course of computational data science.

2. If you have any questions or suggestions, please contact us via the aforementioned emails.



Best Regards, 

Group Doge  <img src="https://www.heredg.com/wp-content/uploads/2020/06/%C5%92%C2%A2%E2%80%93%E2%89%88%C3%95%C2%BA%E2%88%86%C2%A8_20200530192407.jpg" height="30" width="30">

August 25th, 2021
