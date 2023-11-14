# Hyperparameters tuning
The `FLAM` folder contains the source code to fine-tune the LLM's hyperparameters. 
The `testSplit.py` script execute the GridSearchCV algorithm using the `test set` (described int the [Project dataset](#datasets) section) to fine-tune the hyperparameters for the Sentence Splitter component. It produces the split.log file in the ./log folder if executed.
The `testAnalysis.py` script execute the GridSearchCV algorithm using the `test set` (described int the [Project dataset](#datasets) section) to fine-tune the hyperparameters for the COSMIC Analyzer component. It produces the analysis.log file in the ./log folder if executed.
Please, follow the SETUP instructions before running the scripts.