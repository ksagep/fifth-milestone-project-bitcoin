# Bitcoin – currency of matrix

Crypto currencies are very popular nowadays, many people "mine" them, but even more people trade them. This inspired me to develop the project and use predictive analytics. It is a constantly changing and dynamically developing field that is full of challenges. Crypto currencies are affected by events in the world in the same way as real currencies. 
In predictive analytics, there is the possibility of extracting different information from the available data and databases, thereby creating the opportunity to reach a wide range of customers. In my opinion, this field will develop dynamically in the future, on the one hand thanks to increasingly diverse and more easily accessible databases, and on the other hand thanks to the performance of more advanced computers.

![My Image](assets/images/am_i_responsive.jpg) 

## What does this website do?

The purpose of the project is to help a friend of mine find answers who wants to trade Bitcoin in the future.

For link to this website click [Here](https://fifth-milestoneproject-bitcoin.herokuapp.com/).

# **MACHINE LEARNING PIPELINE**

During the project development I followed the CRISP-DM (**CR**oss **I**ndustry **S**tandard **P**rocess for **D**ata **M**ining) method. This method contains six steps which are as follows: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment. It is an industry-proven way to guide your data mining efforts. As a methodology, it includes descriptions of the typical phases of a project, the tasks involved with each phase, and an explanation of the relationships between these tasks.

![My Image](assets/images/crisp_dm_steps.png)

This picture helped me lot in the work. During the development I followed step by step this method and I worked out the details of each area. When I worked out a part of this method I start the next because the individual parts build on each other.

# Planning Phase - project and dataset understanding

## Business requirements

A friend of mine has a successful business and has been making a lot of money recently. She would invest part of her savings in cryptocurrency, particularly in Bitcoin. She decided on Bitcoin because it is the cryptocurrency that has been "mined" for the longest time and is mined in the main cryptomines (e.g. USA, Kazakhstan, Russia, etc.). In her opinion, the price of Bitcoin will rise significantly in the next period. She asked me to look for answers to her questions from the database available to her. Her database is open-sourced and shared only with me for this project.

### The project goals are:
- Verify the client's assumption that the daily opening price is always lower than the closing price, so it is worth selling the crypto currency at the end of the day. There is a greater chance that the client will be able to buy cryptocurrency at a time close to the opening.

- The client would like to know that as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.

## Data collection

### Dataset Content

The dataset is sourced from *Kaggle*. Kaggle is an online platform preferable for data scientist community and machine learning fans.
I created a fictitious user story where predictive analytics can be applied in a real project in the future workplace.
The fileformat of dataset is csv. The dataset has 2786 rows and represents bitcoin market data between 14/Mar/2014 – 29/Oct/2021. Each row represents a date between 14/Mar/2014 – 29/Oct/2021, each column contains different information about exchange rate. You can find in the dataset 7 **columns** which are as follows: Serial number, Currency, Date, Closing price, Opening price, 24h High and 24h Low. The last four columns contain different information about exchange rate.

![My Image](assets/images/columns.jpg)

The data set includes information about:
-   Currency which is Bitcoin for every row
-   Date of a given day 
-	Open and closing prices in USD which are show how the exchange rate developed during the given day;
-	The highest and lowest exchange rate in USD value during the given day.

|      Variable        	|                      Meaning           	         |       Units 	     |   Range	|
|:---------------------:|:--------------------------------------------------:|:----------:|:--------------:
| Date                	| Given date of day 	                             | YY-MM-DD | 2014-03-14 - 2021-10-29 |
| Closing Price (USD) 	| exchange rate value when the market closed  	     | USD |   	109,58 - 63347,80|
| 24h Open (USD)     	| exchange rate value when the market opened 	     | USD |109,58 - 63563,67|
| 24h High (USD) 	    | the highest value of exchange rate on the given day| USD |119,67 - 64802,79|
| 24h Low (USD)     	| the lowest value of exchange rate on the given day |  USD |84,33 - 62095,63|

The types of data are as follows: **currency and date** are *object*, the **different prices** are *float64*. I transformed the type of date in the *Data collection phase* from object to float64 (numeric) because easier to manage this type of data during the studies.
In the assessment I got some instructions that should develop the description of dataset. I provided more information about dataset, data type and content of rows and columns.

### Data cleaning

The dataset is well structured and there are no missing, duplicated or infinite data.

![My Image](assets/images/pandas_overview.jpg)

![My Image](assets/images/variables_overview.jpg)

### Data augmentation and annotation

I did not use data augmentation and annotation during the development of project.

### Feature engineering

The assessment group drew my attention to the fact that the feature engineering notebook was not developed. I developed it and it contains now data exploration part, checking missing data with other method part, checking data duplication, checking outliers, variable transformation part, split the dataset.

### Feature scaling and selection

The aims of these parts are increase accuracy, reduce training time and take less overfitting.
I used during the project the StandardScaler() and SelectFromModel() possibilities to build ML pipeline.

### Project Terms and Jargon

-	*Exchange rate*: the value of rate between Bitcoin and USD on the given day
-	*Open prices*: the value of Bitcoin in USD at market open on given day
-   *Closing prices*: the value of Bitcoin in USD at market close on given day

### Hypothesis and how to validate?

1.	The opening price is lower than the closing price.
	Validation: This will be validated with a correlation study and use diagrams for visualisation. Use mathematical calculation solution for better understanding of dataset. 

2.	As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.
    Validation: This will be validated with a correlation study. Use diagrams for visualisation. Use mathematical calculation solution for better understanding of dataset.


## The rationale to map the business requirements to the Data Visualizations and ML tasks

During the evaluation, it was determined by the assessment team that the pages did not appear on the dashboard due to an error. I correct it and I display these pages now. I developed the content of the business requirements also.

### Business Requirements 1 – Data visualisation and correlation study
The client interested to understand the patterns from **differences between opening and closing prices** so the client can realize or decide the most relevant variables which are correlated as best option to sell or buy Bitcoins on a given day.

-	I inspect the opening and closing value of exchange rate
-	I create the difference between the two values for each day
-	I conduct a correlation study to understand better the correlation to the expectation of client
-	I plot the trends of differences in diagrams

### Business Requirements 2 - Data visualisation and correlation study
As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate. How will correlate the opening and closing price to each other? Which period of the year could be the best for trading?

-   I inspect the difference between the opening and closing value on 1st January, 30th June and 31th December in every year
-   I make an annual comparison of these data with a correlation study
-   I plot the annual values in a diagram

## Features
        
   ### Navigation 
        - The dashboard developed is a multipage streamlit application with sidebar navigation and checkbox links.
        - The navigation links provides quick access to the four pages as follows:

          - Page 1: Short project summary
            This page contain briefs about Client's requirements, description of project dataset and terms and jargons.
![My Image](assets/images/short_project_sum.jpg)

          - Page 2: Differences between opening and closing value
            It shows answer business requirement 1. Lists the findings related to the inspection of the opening and closing value of exchange rate.
![My Image](assets/images/study_of_diff_page.jpg)

          - Page 3: Annual comparison
            It will answer business requirement 2. Lists the findings related to the inspection of the difference between the opening and closing value on 1st January, 30th June and 31th December in every year.
![My Image](assets/images/study_of_annual_comparison_page.jpg)

          - Page 4: Project hypothesis and validation
            This page shows the project hypothesis and how these were validated across the project.
![My Image](assets/images/hypothesis_and_valid.jpg)

          - Page 5: Exchange rate predictor - Bitcoin
            This page display the parts of ML pipeline with a short description.
![My Image](assets/images/rate_predictor.jpg)

## Deployment

### Dashboard design

The structure of dashboard follow the list as you find below:

   #### Page 1: Short project summary
        - This page is showing the **dataset summary and the business requirements** as well as **the terms and jargons** for better understanding.

        - Client's requirements:
            - Verify the client's assumption that the daily opening price is always lower than the closing price, so it is worth selling the cryptocurrency at the end of the day.
            - To prove that as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.

        - Description of project dataset:
            - The dataset is sourced from Kaggle. I created a fictitious user story where predictive analytics can be applied in a real project in the future workplace.
            - The dataset has 2786 rows and represents bitcoin market data between 14/Mar/2014 – 29/Oct/2021. Each row represents a date between 14/Mar/2014 – 29/Oct/2021, each column contains different information about rate of exchange. The data set includes information about:
                -	Open and closing prices which are show how the exchange rate developed during the given day;
                -	The highest and lowest exchange rate value during the given day.

        - Terms and jargons of the project:
            -	Exchange rate: the value of rate between Bitcoin and USD on the given day
            -	Open prices: the value of Bitcoin in USD at market open on given day
            -   Closing prices: the value of Bitcoin in USD at market close on given day

   #### Page 2: Differences between opening and closing value
        It will answer business requirement 1
        - Lists the findings related to the inspection of the opening and closing value of exchange rate
        - Checkbox 1: Plot the trend of differences in a diagram

   #### Page 3: Annual comparison
        It will answer business requirement 2
        - Lists the findings related to the inspection of the difference between the opening and closing value on 1st January, 30th June and 31th December in every year
        - Checkbox 1: Differences between annual comparison of the aformentioned data
        
   #### Page 4: Project hypothesis and validation
        - Display every hypothesis and their validations

   #### Page 5: Exchange rate predictor - Bitcoin
        - Display the ML pipeline parts with images and short descriptions.


### Workspace Setup
The repository for this project was created off the [template](https://github.com/Code-Institute-Solutions/milestone-project-bring-your-own-data) provided by Code Institute and GitPod workspace was used to develop this project.

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- Click `Gitpod` to create a Gitpod workspace.
- **To return to the current workspace, login to your gitpod account and open the workspace created earlier, since clicking on GitPod button on the GitHub page creates a new workpspace each time.**

### Deploying to Heroku
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App and set the location (Europe).
2. In the **"Settings"** manage the config vars part.
3. In the buildpacks I chose heroku/python
4. At the Deploy tab, select GitHub as the deployment method.
5. Select my repository name and click Search. Once it is found, click Connect.
6. **If you use Python version 3.8.12 or 15 should change the stack of Heroku to 20 before deployment for proper working.**
7. Select the branch you want to deploy, then click Deploy Branch.
8. The deployment process should happen smoothly if all deployment files are fully functional.
9. Click the button **Open App** on the top of the page to access my App. The App live link is: https://fifth-milestoneproject-bitcoin.herokuapp.com/ 

## Main Data Analysis Libraries

- jupyter notebook - used for writing and running the ML pipelines
- numpy - used for array manipulation
- pandas - used to structure the data
- matplotlib - for creating the charts and plots for data visaulization
- seaborn - used in conjuction with matplotplib for data visualization
- plotly - used for ploting charts for data visualization
- streamlit - for the dashboard development

## Other Frameworks, Libraries & Programs Used

- Git - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub
- GitHub: - used to store the projects code after being pushed from Git
- GitPod - Workspace used for the project
- AmIResponsive - Used to generate responsive image used in README file
- Heroku - Deployment platform for the project

## Credits
### Content:
    - Code Institute course materials
    - Code Institute Slack Community for some helps
    - Code Institute Mentor meetings and support
    - Code Institute tutor support
    - W3schools.com for ideas
    - Geeksforgeeks.com for thoughts
    - Listendata.com for thoughts
    - Datacamp.com for ideas
    - Net-information.com for ideas
    - Bobbyhadz.com for thoughts
    - Linuxhint.com for ideas
    - Datascience-pm.com for better understanding of CRISP-DM approach

### Media:
    - Am I Responsive for a responsive image in README 
    - I took the placeholder pictures from my app for README

## Unfixed bugs

Plot the images on the dashboard. I tried to use short or full path of images; use urls of images and other methods. When I start the project from terminal, the code, what you can find in my project now, works properly. But when I deploy it on Heroku it did not worked properly and sent an error message (the given image does not exists) even though the project deploy was successful.
    
## Acknowledgements

    I would like to thank my family and especially for my wife who support me during the learning time.
    I would like to thank also my mentor, Marcel Mulders for his support, guidance and feedbacks throughout the course of the project.