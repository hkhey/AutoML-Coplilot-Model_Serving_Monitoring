# AutoML-Coplilot-Model_Serving_Monitoring
---

#### Overview
This project demonstrates the deployment of a machine learning model as a service using Azure Automated Machine Learning (AutoML), focusing on predicting future weather conditions from the "weather_data.csv" dataset.

#### Steps with Screenshots

1. **Dataset Preparation**
   - **Screenshot 1**: Upload of "weather_dataset_processed.csv" to Azure Machine Learning Studio.
     ![Dataset Upload](https://cdn.discordapp.com/attachments/1191490101247758479/1193685027024818237/cap1.png)
   - **Screenshot 2**: Exclusion of specific columns like "Timestamp" and "Location".
     ![Schema Definition](https://cdn.discordapp.com/attachments/1191490101247758479/1193685027419062302/cap2.png)

2. **Model Training with Automated ML**
   - **Screenshot 3**: Azure AutoML interface with the dataset.
     ![AutoML Interface](https://cdn.discordapp.com/attachments/1191490101247758479/1193685027691704480/cap3.png)
   - **Screenshot 4**: Model training process.
     ![Model Training](https://cdn.discordapp.com/attachments/1191490101247758479/1193685028023062598/cap4.png)
   - **Screenshot 5**: Selection of the best-performing model.
     ![Model Selection](https://cdn.discordapp.com/attachments/1191490101247758479/1193685028308254730/cap5.png)

3. **Model Deployment**
   - **Screenshot 6**: Deployment process using Azure Container Instance.
     ![Model Deployment](https://cdn.discordapp.com/attachments/1191490101247758479/1193685028606062632/cap6.png)
   - **Screenshot 7**: Deployment status "Healthy".
     ![Deployment Status](https://cdn.discordapp.com/attachments/1191490101247758479/1193685028908060792/cap7.png)

4. **Inference and Testing**
   - **Screenshot 8**: `inference.py` script with service URL placeholder.
     ![Inference Script](https://cdn.discordapp.com/attachments/1191490101247758479/1193683276884361336/Screenshot_20240108_000557.png)
   - **Screenshot 9**: Script execution and predictions.
     ![Script Execution](https://cdn.discordapp.com/attachments/1191490101247758479/1193683277136015421/Screenshot_20240108_000712.png)


#### Files in the Repository

- `app.py`: Flask application script.
- `inference.py`: Script for testing the deployed model.
- `requirements.txt`: List of Python dependencies.

#### Installation and Running

- Install Python and dependencies from `requirements.txt`.
- Run `app.py` to start the Flask application.
- Access the web application at the local host address provided.

#### Note

- Replace placeholder values in scripts with actual data from your Azure setup.
- For detailed steps or troubleshooting, refer to Azure AutoML documentation or the provided PDF.

---
