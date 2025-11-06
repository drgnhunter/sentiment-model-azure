# sentiment-model-azure
A-to-Z guide for deploying a sentiment analysis API on Azure Machine Learning. 

# Deploy a Scikit-Learn Sentiment Analysis Model on Azure ML

This repository contains all the code and configuration files for the A-to-Z blog post on deploying a `scikit-learn` sentiment analysis model as a production-ready API on Azure Machine Learning.

**Blog Post Link:** **[Link to your blog post here]**

This project demonstrates a complete, battle-tested workflow, including all the configuration files needed to overcome common errors related to quotas, Python environments, and permissions.

---

## 🚀 Project Files

This repo provides the exact files needed to deploy the model:

* `sentiment_model.pkl`: A pre-trained `scikit-learn` sentiment analysis model.
* `score.py`: The Python script required by Azure ML to load the model and make predictions.
* `environment.yml`: A Conda environment file that defines the exact Python version and packages (like `numpy`, `scikit-learn`, and `azureml-inference-server-http`) needed to run the `score.py` script. This file is crucial for preventing dependency errors.
* `deployment.yaml`: The deployment configuration file. This defines our VM size (`Standard_DS2_v2`), sets up readiness probes to handle slow start-up times, and points to all the other files.
* `.amlignore`: Tells Azure ML to ignore files (like `venv/`) when uploading the code.

---

## 🛠️ How to Use

To deploy this project, you will need an Azure subscription and the [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

For a complete, step-by-step walkthrough of every command, please read the full blog post: **[Link to your blog post here]**

The short version of the deployment process is:

1.  **Configure Your CLI:**
    * Log in using `az login --tenant <YOUR-TENANT-ID>`
    * Register required resource providers (`Microsoft.MachineLearningServices`, etc.)
    * Set your defaults: `az configure --defaults group="<YOUR-GROUP>" workspace="<YOUR-WORKSPACE>"`

2.  **Create Azure Resources:**
    * `az ml model create ...` (to register `sentiment_model.pkl`)
    * `az ml online-endpoint create ...` (to create the blank endpoint)

3.  **Deploy the Model:**
    * Run `az ml online-deployment create --file deployment.yaml`.
    * This will likely fail with a permission error.

4.  **Fix Permissions & Update:**
    * Assign the `AcrPull` role to your endpoint's identity (see blog for details).
    * Run `az ml online-deployment update --file deployment.yaml`. This will take ~15 minutes to build the custom environment.

5.  **Route Traffic:**
    * `az ml online-endpoint update --name "sentiment-analysis-endpoint" --traffic "blue=100"`

6.  **Test Your API!**
    * Use Postman or `curl` to send test data to your new endpoint.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. You are free to use, modify, and distribute this code.
