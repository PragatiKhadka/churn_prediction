## churn_prediction
### Description
The objective of the project is to develop a clustering machine learning model that help the bank to predict if a (new) customer will stay in the bank or will churn. The application has been deployed in [heroku](https://ml-churn-prediction.herokuapp.com/).

### Installation
In order to run the program, install the libraries in the `requirements.txt`. 

### Usage
1. `Clustering.ipynb` contains all the codes related to the data preprocessing, training and prediction from the mode.
2. In the `model` folder, `clustering_model.sav` is the model saved from the step 1.
3. The `data` folder contains two json files which are the results of the churn rate and female percentage calculations on each cluster. It is saved automatically from step 1.
4. The 'templates` folder contains all the html pages used in the application.
5. `app.py` is the main python program that runs the application. 

### Example 
1. Go to the [heroku](https://ml-churn-prediction.herokuapp.com/)

![home](./images/home.PNG)

2. Click the button to continue  
3. Enter the customer information and click submit

![cust_info](./images/cust_info.PNG)  
4. The result will be displayed. The first row of the table is the `cluster id`. Second row is the `churn rate` in that cluster. And the third row is the `% of female population` in that cluster.  
![result](./images/output.PNG)

### Program Flow
1. Read the provided dataset
2. Understand and analyse the data based on the features
3. Select the algorithm (k-means)
4. Select the features to use in the model
5. Select the optimal value of k for the k-means
6. Train the model and save it
7. Calculate the `Silhoutte score` to check the performance of the model
8. Calculate the churn rate and the female percentage on each cluster and save it into json
9. 3D plot the clusters
