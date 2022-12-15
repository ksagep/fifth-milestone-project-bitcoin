# Bitcoin – currency of matrix

Crypto currencies are very popular, many people mine them, but even more people trade them. This inspired me to develop the project and use predictive analytics. In predictive analytics, there is the possibility of extracting different information from the available data and databases, thereby creating the opportunity to reach a wide range of customers. In my opinion, this field will develop dynamically in the future, on the one hand thanks to increasingly diverse and more easily accessible databases, and on the other hand thanks to the performance of more advanced computers.

![My Image](assets/images/i_am_responsive.jpg)

## What does this website do?

The purpose of the project is to help a friend of mine find answers who wants to trade Bitcoin among the crypto currencies in the future.

For link to this website click [Here](https://.herokuapp.com/).

# Planning Phase

## Business requirements

A friend of mine has a successful business and has been making a lot of money recently. She would invest part of her savings in cryptocurrency, particularly in Bitcoin. She decided on Bitcoin because it is the cryptocurrency that has been "mined" for the longest time and is mined in the main cryptomines (e.g. USA, Kazakhstan, Russia, etc.). In her opinion, the price of Bitcoin will rise significantly in the next period. She asked me to look for answers to his questions from the database available to her. Her database is open-sourced and shared only with me for this project.

### The project goals are:
- Verify the client's assumption that the daily opening price is always lower than the closing price, so it is worth selling the cryptocurrency at the end of the day.

- To prove that as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.

## Dataset Content

The dataset is sourced from Kaggle. I created a fictitious user story where predictive analytics can be applied in a real project in the future workplace.
The dataset has 2786 rows and represents bitcoin market data between 14/Mar/2014 – 29/Oct/2021. Each row represents a date between 14/Mar/2014 – 29/Oct/2021, each column contains different information about exchange. The data set includes information about:
-	Open and closing prices which are show how the exchange rate developed during the given day;
-	The highest and lowest exchange rate value during the given day.

|      Variable        	|                      Meaning           	         |       Units 	     |   	
|---------------------	|--------------------------------------------------  |----------------   |
| Date                	| Given date of day 	                             | Date  	         |
| Closing Price (USD) 	| exchange rate value when the market closed  	     | 109,58 - 63347,80 |   	
| 24h Open (USD)     	| exchange rate value when the market opened 	     | 109,58 - 63563,67 |
| 24h High (USD) 	    | the highest value of exchange rate on the given day| 119,67 - 64802,79 |
| 24h Low (USD)     	| the lowest value of exchange rate on the given day | 84,33 - 62095,63  |

## Project Terms and Jargon
-	Exchange rate: the value of rate between Bitcoin and USD on the given day
-	Open and closing prices: the value of Bitcoin in USD at market open and close on that day

## Hypothesis and how to validate?

1.	The opening price is lower than the closing price.
	Validation: This will be validated with a correlation study and use diagrams for visualisation.

2.	As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.
    Validation: This will be validated with a correlation study. Use diagrams for visualisation.


## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirements 1 – Data visualisation and correlation study

-	I will inspect the opening and closing value of exchange rate
-	I create the difference between the two values for each day
-	I will conduct a correlation study to understand better the correlation to the expectation of client
-	I will plot the trends of differences in diagrams

### Business Requirements 2 - Data visualisation and correlation study

-   I will inspect the difference between the opening and closing value on 1st January and 31th December in every year
-   I will make an annual comparison of these data with a correlation study
-   I will plot the annual values in a diagram


## Dashboard design
The structure of dashboard follow the list as you find below:

   ### Page 1: Short project summary
        - This page is showing the dataset summary and the business requirements as well as the terms of jargons for better understanding.

        - Client's requirements:
            - Verify the client's assumption that the daily opening price is always lower than the closing price, so it is worth selling the cryptocurrency at the end of the day.
            - To prove that as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.

        - Description of project dataset:
            - The dataset is sourced from Kaggle. I created a fictitious user story where predictive analytics can be applied in a real project in the future workplace.
            - The dataset has 2786 rows and represents bitcoin market data between 14/Mar/2014 – 29/Oct/2021. Each row represents a date between 14/Mar/2014 – 29/Oct/2021, each column contains different information about exchange. The data set includes information about:
                -	Open and closing prices which are show how the exchange rate developed during the given day;
                -	The highest and lowest exchange rate value during the given day.

        - Terms and jargons of the project:
            -	Exchange rate: the value of rate between Bitcoin and USD on the given day
            -	Open and closing prices: the value of Bitcoin in USD at market open and close on that day

   ### Page 2: Differences between opening and closing value
        It will answer business requirement 1
        - Lists the findings related to the inspection of the opening and closing value of exchange rate
        - Checkbox 1: Differences between opening and closing value of exchange rate
        - Checkbox 2: Plot the trend of differences in a diagram

   ### Page 3: Annual comparison
        It will answer business requirement 2
        - Lists the findings related to the inspection of the difference between the opening and closing value on 1st January and 31th December in every year
        - Checkbox 1: Differences between annual comparison of the aformentioned data
        - Checkbox 2: Plot the annual values in a diagram

   ### Page 4: Project hypothesis and validation
            - Display every hypothesis and their validations

   ### Page 5: ML performance metrics
            - A technical page which is displaying the model performance

## Features
The application is designed using streamlit library. It is has a sidebar menu with five navigation links.

   ### Navigation 
        - The dashboard developed is a multipage streamlit application with sidebar navigation checkbox links.
        - The navigation links provides quick access to the five pages as follows:

          - Page 1: Short project summary
          - Page 2: Differences between opening and closing value
          - Page 3: Annual comparison
          - Page 4: Project hypothesis and validation
          - Page 5: ML performance metrics

## Unfixed bugs

## Deployment

### Workspace Setup
The repository for this project was created off the [template](https://github.com/Code-Institute-Solutions/) provided by Code Institute and GitPod workspace was used to develop this project.

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- Click `Gitpod` to create a Gitpod workspace.
- **To return to the current workspace, login to your gitpod acoount and open the workspace created earlier, since clicking on GitPod button on the GitHub page creates a new workpspace each time.**

### Creating Heroku App
The Python version in the project is set to 3.8.13, which is not supported by Heroku's current default stack, heroku-22.
As a result of the above, the app was created from Heroku CLI and set to use buildstack heroku-20.

Steps take to create the app is as follows:
1. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if not already installed
2. Copy API key from heroku
	- sign in and click on the avatar icon and select **Account Settings**
	- Scroll down to the API Key section and click **Reveal** button, and copy key displayed.
3. Login to Heroku via the console and enter your details when prompted
	`heroku login -i`
	- enter key copied from step 2 when prompted for password
4. Create the app
	`heroku apps:create pp5-mildew-detection --stack heroku-20`

### Deploying to Heroku
1. Sign in to Heroku
2. Select app
3. At the Deploy tab, select GitHub as the deployment method.
4. Select your repository name and click Search. Once it is found, click Connect.
5. Select the branch you want to deploy, then click Deploy Branch.
6. The deployment process should happen smoothly in case all deployment files are fully functional. 
7. Click the button **Open App** on the top of the page to access your App.



The steps of the publishing on the Heroku were as follow:
    
    1. I created an app name and set the location (Europe)

    2. In the **"Settings"** I managed the config vars part

    3. In the buildpacks I chose heroku/python

    4. In the Deploy section I create a connection between GitHub and Heroku

    5. With the Deploy Branch button I created a deployed app

    6. The website was published on Heroku Page and the link was provided in the same section.

## Main Data Analysis and Machine Learning Libraries
- jupyter notebook - used for writing and running the ML pipelines
- numpy - used for array manipulation
- pandas - used to structure the data
- matplotlib - for creating the charts and plots for data visaulization
- seaborn - used in conjuction with matplotplib for data visualization
- plotly - used for ploting charts for data visualization
- streamlit - for the dashboard development
- scikit-learn - used for data processing

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
### Media:
    - Am I Responsive for a responsive image in README 
    - I took pictures 
    - I took the placeholder picture

## Acknowledgements
    I would like to thank my family and especially for my wife who support me and sometimes pressured me to learn.
    I would like to thank also my mentor, Marcel Mulders for his support, guidance and feedbacks throughout the course of the project.





## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.



## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
