# COMET
GPT-3 COSMIC Measurement Tool

This app requires python 3.

# **SETUP**
# Step 1: Set up virtual environment and install packages
Here is the command to make a virtual environment:

python -m venv venv
Now you can activate the environment:

source venv/bin/activate
This app requires two packages: openai and streamlit. First, let’s upgrade pip:

pip install --upgrade pip
Now we can install the packages:

pip install openai streamlit


# Step 2: Set up secrets.toml
For local development, we will be storing the API key in a file called secrets.toml, and we will put it in the .streamlit directory. Assuming you are in the root of your repo, you can enter the following commands:

mkdir .streamlit
cd .streamlit
touch secrets.toml
Once we generate the API key in the following step, you can store it in this file.


# Step 3: Get an OpenAI API key
If you don’t already have an account with OpenAI, you can create an account here. Once you have an account and get logged in, you can click on the name icon in the upper right, and select View API keys.

You can press the button that says Create new secret key. Copy the secret key from the pop-up, and paste it into secrets.toml like this (don’t forget to put quotes around the API key):

OPENAI_KEY="<paste-your-key-here-with-quotes>"
If you’ve already blown through your free OpenAI credits and have moved to paid account, it’s a good idea to set a usage limit. Since we are deploying this app publicly, you want to make sure that you don’t accidentally spend more money than intended.
  
# **RUNNIN COMET**:
streamlit run app.py
