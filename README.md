# COMET
GPT-4 COSMIC Measurement Tool

This app requires python 3.

## Introduction

The COMET repository is organized into several directories:

| Directory                       | Description                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [`datasets`]  | Contains the datasets used for the empirical evaluation. |
| [`FLAM`]  | Contains the source code used to fine-tune the hyperparameters of GPT-4 using the GridSearchCV algorithm.              |
| [`COMET`] | Contains the COMET tool sources. |
| [`Comparison Research`] | Contains the results of the systematic search on Scopus to identify all articles proposing COSMIC automation tools and identify potential approaches to compare with COMET. |
| [`deepCOSMIC`] | Contains the experiments with DEEP-COSMIC-UC. |
| [`results`]   | Contains the COMET empirical evaluation results. |
| [`metrics`]   | Contains the source code to compute the COMET metrics. |

## Datasets
The `datasets` directory contains the datasets used for the the empirical evaluation of the COMET approach. The folder contains the following subfolders:
- `ALBERGATE`, contains the ALBERGATE use case model, the manual and automatic measurement
- `AutomaticLineSwitching`, contains the Automatic Line Switching use case model, the manual and automatic measurement
- `K01719`, contains the FID-CPM use case model, the manual and automatic measurement
- `K01726`, contains the FID-MTC use case model, the manual and automatic measurement
- `RiseCooker`, contains the Rise cooker use case model,the manual and automatic measurement
- `U-CURE`, contains the U-CURE use case model, the manual and automatic measurement
- `RQ2-RQ3`, contains the FID-TCT use case model, the manual and automatic measurement
- `test set`, contains the test set used to refine the GPT-4 model for the Sentence Splitter and the COSMIC Analyzer components.

Each sub-folder contains also the directories:
- `FP_prompts`, contains the prompts used for each use case
- `measurement`, contains the manual and COMET result for each use case

## GPT-4 Hyperparameters tuning
The `FLAM` directory contains the source code used to fine-tune the GPT-model hyperparameters. 
The `testSplit.py` script execute the GridSearchCV algorithm using the `test set` (described int the [Project dataset](#datasets) section) to fine-tune the hyperparameters for the Sentence Splitter component. It produces the split.log file in the ./log folder if executed.
The `testAnalysis.py` script execute the GridSearchCV algorithm using the `test set` (described int the [Project dataset](#datasets) section) to fine-tune the hyperparameters for the COSMIC Analyzer component. It produces the analysis.log file in the ./log folder if executed.
Please, follow the SETUP instructions before running the scripts.

## COMET Tool
The `COMET` directory contains the source code of the COMET Web tool. The `app.py` script run the web application. 
Please, follow the SETUP instructions before running the scripts.

## Comparison Research
The `Comparison Research` directory contains the results of the systematic search we performed on Scopus to identify all the articles proposing COSMIC automation tools and identify potential approaches to compare with COMET. The results are reported in the `cosmic_SLR.xlsx` file.

## deepCOSMIC
The `deepCOSMIC` directory contains the source code of `DEEP-COSMIC-UC` (see reference below) and the results of the experiments using it with the COMET datasets.
@article{ochodek2020deep,
  title={Deep learning model for end-to-end approximation of COSMIC functional size based on use-case names},
  author={Ochodek, Miros{\l}aw and Kopczy{\'n}ska, Sylwia and Staron, Miroslaw},
  journal={Information and Software Technology},
  volume={123},
  pages={106310},
  year={2020},
  publisher={Elsevier}
}

## Results
The `results` directory contains the results of the empirical evaluation of the COMET approach. 
It contains the following files:
- `MIS.xlsx`, contains the results for the evaluation of the ALBERGATE application.
- `IoT Microservices.xlsx`, contains the results for the evaluation of the Microservices applications.
- `Realtime.xlsx`, contains the results for the evaluation of the Realtime applications.
- `AI.xlsx`, contains the results for the evaluation of the U-CARE application.
- `Summary.xlsx`, contains the summary of the results.

## Metrics
The `metrics` directory contains the source code used to evaluate the 1-Rouge and BLEU metrics for the analyzed use case models.
It contains the following folders:
- ALBERGATE
- Iot microservices
- Realtime
- U-CURE
- MAE

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
  
# **RUNNING COMET**:
streamlit run app.py

# **METRICS**:
In the 'metrics' folder you can find the python files to calculate COMET metrics: precision, recall and f1-scores for Data groupd, Object of interests, Functional Users, and Data movements. You can also find the MAE folder, where there are the necessary code to compute the MAE metrics for COMET and DEEP-COSMIC-UC on the COMET dataset.
