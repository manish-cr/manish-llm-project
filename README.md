# manish-llm-project
This is a command-line based app that gives pertinent answers about me, 'Manish'. First, clone the repository and use either the windows or docker approach to run this app.
## Prerequisites
1. You will need to create a virtual environment (venv). (*if you intend to run the chatbot on windows*), here are the steps:
    1. clone the repository to your local machine
    2. create a virtual environment in the root directory
    ```bash
    python -m venv venv
    ```
    3. Activate the virtual environment (Windows)
    ```bash
    venv\Scripts\activate.bat
    ```
    4. Install dependencies using pip
    ```bash
    pip install -r requirements.txt
    ```
2. You will need to get an OpenAI API KEY first, here are the steps:
    1. End-user will be invited to create an account on OpenAI API key
    2. Create a **`.env`** file in the root folder of manish-llm-project and follow the example of **`.env.example`** to recreate the environment
    3. Follow the below instructions
## Instructions
Here is how to run this on:
### Windows:
Click on **`run_chatbot.bat`** on manish-llm-project directory
### Docker:
If you intend to use docker, ensure to download and start the docker machine first. [docker download](https://www.docker.com/products/docker-desktop/)
```bash
docker build -t chatbot-image .
docker run --rm -it chatbot-image
```