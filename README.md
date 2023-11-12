# COMET
GPT-4 COSMIC Measurement Tool

This app requires python 3.

## Introduction

The COMET repository provides the proof of concept of the COMET tool. The repository is organized into several directories:

| Directory                       | Description                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [`FLAM`]       | Contains the source code used to fine-tune the hyperparameters of GPT-4 using the GridSearchCV algorithm.              |
| [`project dataset`]                 | Contains the datasets used for the empirical evaluation. |
| [`COMET`]                | Contains the COMET tool sources. |
| [`results`]                | Contains the COMET empirical evaluation results. |
| [`metrics`]                | Contains the source code to compute the COMET metrics. |

## Project dataset
The `project dataset` directory contains the datasets used for the the empirical evaluation of the COMET approach. The folder contains the following subfolders:
- ALBERGATE, contains the ALBERGATE use case model, the manual and automatic measurement
- AutomaticLineSwitching, contains the Automatic Line Switching use case model, the manual and automatic measurement
- K01726, contains the FID-MTC use case model, the manual and automatic measurement
- RiseCooker, contains the Rise cooker use case model,the manual and automatic measurement
- U-CURE, contains the U-CURE use case model, the manual and automatic measurement
- RQ2-RQ3, contains the FID-TCT use case model, the manual and automatic measurement
- test set, contains the test set used to refine the GPT-4 model for the SentenceSplitter and the COMET Analyzer components.

Each sub-folder contains also the directories:
- FP_prompts, contains the prompts used for each use case
- measurement, contains the manual and COMET result for each use case

# **SETUP**
# Step 1: Download the repository
Download the COMET repository and go to the COMET directory. 

# Step 2: Set up virtual environment and install packages
Here is the command to make a virtual environment:

```
python -m venv venv
```
Now you can activate the environment:

```
source venv/bin/activate
```
This app requires two packages: openai and streamlit. First, let’s upgrade pip:

```
pip install --upgrade pip
```
Now we can install the packages:

```
pip install -r requirements.txt
```

# Step 3: Get an OpenAI API key
If you don’t already have an account with OpenAI, you can create an account here. Once you have an account and get logged in, you can click on the name icon in the upper right, and select View API keys.

You can press the button that says Create new secret key. Copy the secret key from the pop-up, and export the environment variable OPENAI_API_KEY:

```
export OPENAI_API_KEY=<paste-your-key-here>
```

If you’ve already blown through your free OpenAI credits and have moved to paid account, it’s a good idea to set a usage limit. Since we are deploying this app publicly, you want to make sure that you don’t accidentally spend more money than intended.
  
# **RUNNIN COMET**:
streamlit run app.py

# **METRICS**:
In the 'metrics' folder you can find the python files to calculate COMET metrics: precision, recall and f1-scores for Data groupd, Object of interests, Functional Users, and Data movements.
