# Datasets
The `datasets` directory contains the datasets used for the the empirical evaluation of the COMET approach. The folder contains the following subfolders:
- `ALBERGATE`, contains the ALBERGATE use case model, the manual and automatic measurement
- `AutomaticLineSwitching`, contains the Automatic Line Switching use case model, the manual and automatic measurement
- `K01726`, contains the FID-MTC use case model, the manual and automatic measurement
- `RiseCooker`, contains the Rise cooker use case model,the manual and automatic measurement
- `U-CURE`, contains the U-CURE use case model, the manual and automatic measurement
- `RQ2-RQ3`, contains the FID-TCT use case model, the manual and automatic measurement
- `test set`, contains the test set used to refine the GPT-4 model for the Sentence Splitter and the COSMIC Analyzer components.

Each sub-folder contains also the directories:
- `FP_prompts`, contains the prompts used for each use case
- `measurement`, contains the manual and COMET result for each use case