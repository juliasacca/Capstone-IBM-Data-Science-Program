# 🚀 Applied Data Science Capstone – SpaceX Launch Analysis

This repository contains my final project for the IBM Data Science Professional Certificate. It showcases a full data science workflow using SpaceX launch data — from data collection to building a machine learning model and an interactive dashboard.

### 📌 Project Overview

The objective of this capstone is to predict the success of Falcon 9 first stage landings, a key factor in SpaceX’s ability to reuse rockets and reduce costs.

Throughout the project, I applied:

* Data collection from APIs and web scraping
* Data wrangling and exploratory data analysis (EDA)
* SQL queries for structured analysis
* Geospatial visualization of launch sites
* Interactive dashboard creation with Dash
* Machine learning model development and evaluation

### 📂 Repository Contents
| File                                              | Description                                                                                             |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [`SpaceX-Data-Collection-API.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Data-Collection-API.ipynb)   | Collects SpaceX launch data using the SpaceX API.                                                       |
| [`SpaceX-Webscraping.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Webscraping.ipynb)                  | Scrapes Falcon 9 launch records from Wikipedia for additional data.                                     |
| [`SpaceX-Data-Wrangling.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Data-Wrangling.ipynb) | Performs exploratory data analysis through data wrangling. |
| [`SpaceX-EDA-SQL.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-EDA-SQL.ipynb)     | Explores data using SQL queries on a SQLite database.                                                   |
| [`SpaceX-EDA-Viz.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-EDA-Viz.ipynb)          | Explores and prepares data through feature engineering.                                      |
| [`SpaceX-Launch-Site-Location.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Launch-Site-Location.ipynb)          | Performs geospatial analysis and visualizes launch site locations.                                      |
| [`SpaceX-Dash-App.py`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Dash-App.py)                              | Provides an interactive dashboard for SpaceX launch analysis via Dash application.                     |
| [`SpaceX-Machine-Learning-Prediction.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/main_with_app/SpaceX-Machine-Learning-Prediction.ipynb)  | Builds and evaluates classification models (Logistic Regression, SVM, etc.) to predict landing success. |

### 🚀 Technologies Used

* **Python:** Pandas, NumPy, Matplotlib, Seaborn, Folium, Plotly
* **APIs & Web Scraping:** Requests, BeautifulSoup
* **Databases:** SQLite, SQL queries
* **Machine Learning:** Scikit-learn (Logistic Regression, SVM, GridSearchCV)
* **Dashboard:** Dash, Plotly, Heroku
* Jupyter Notebooks

### 📈 Results

–  Developed multiple machine learning models to predict rocket landing success.

–  Achieved best performance with the KNN Model at **90%** *training* accuracy and **94%** *test* accuracy.

–  Created an interactive dashboard which allows dynamic exploration of launch success by site, payload, and orbit.

### 👔 Presentation
[`Interactive Dashboard`](https://spacex-dash-app-e395ca8c9927.herokuapp.com/)

[`Link to Presentation`](https://docs.google.com/presentation/d/e/2PACX-1vS0SefwrPcUAjoHdEHUtogVKzGJiqM8CW-lqRCCFC_PgEFRMytoHZgDP6VIb2Q6P3P8qCSqfwVdzIq2/pub?start=false&loop=false&delayms=3000)


#### 📜 Acknowledgements
_This project was completed as part of the Applied Data Science Capstone within the IBM Data Science Professional Certificate, and accessed through Coursera._
