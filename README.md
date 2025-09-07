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
| [`jupyter-labs-spacex-data-collection-api.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/4b569ed735f5acccfa6c5e74be72eba724de007e/jupyter-labs-spacex-data-collection-api.ipynb)   | Collects SpaceX launch data using the SpaceX API.                                                       |
| [`jupyter-labs-webscraping.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/4b569ed735f5acccfa6c5e74be72eba724de007e/jupyter-labs-webscraping.ipynb)                  | Scrapes Falcon 9 launch records from Wikipedia for additional data.                                     |
| [`jupyter-labs-eda-sql-coursera_sqllite.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/4b569ed735f5acccfa6c5e74be72eba724de007e/jupyter-labs-eda-sql-coursera_sqllite.ipynb)     | Explores data using SQL queries on a SQLite database.                                                   |
| [`lab_jupyter_launch_site_location.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/4b569ed735f5acccfa6c5e74be72eba724de007e/lab_jupyter_launch_site_location.ipynb)          | Performs geospatial analysis and visualizes launch site locations.                                      |
| [`spacex-dash-app.py`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/4b569ed735f5acccfa6c5e74be72eba724de007e/spacex-dash-app.py)                              | Dash application that provides an interactive dashboard for SpaceX launch analysis.                     |
| [`SpaceX_Machine Learning Prediction_Part_5.ipynb`](https://github.com/juliasacca/Capstone-IBM-Data-Science-Program/blob/274c81923dccea78b837a883f6c7700719544f15/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb) | Builds and evaluates classification models (Logistic Regression, SVM, etc.) to predict landing success. |

### 🚀 Technologies Used

* **Python:** Pandas, NumPy, Matplotlib, Seaborn, Folium, Plotly
* **APIs & Web Scraping:** Requests, BeautifulSoup
* **Databases:** SQLite, SQL queries
* **Machine Learning:** Scikit-learn (Logistic Regression, SVM, GridSearchCV)
* **Dashboard:** Dash / Plotly
* Jupyter Notebooks

### 📈 Results

–  Developed multiple machine learning models to predict rocket landing success.

–  Achieved best performance with the KNN Model at **90%** *training* accuracy and **94%** *test* accuracy.

–  Created an interactive dashboard which allows dynamic exploration of launch success by site, payload, and orbit.


#### 📜 Acknowledgements
_This project was completed as part of the Applied Data Science Capstone within the IBM Data Science Professional Certificate, and accessed through Coursera ._
