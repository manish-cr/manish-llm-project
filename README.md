# manish-llm-project
This is a command-line based app that gives pertinent answers about me, 'Manish'. First, clone the repository and use either of the 2 approaches to run the app. If you will be using docker, ensure to download and start the docker machine first. [docker download](https://www.docker.com/products/docker-desktop/)
## Instructions
Here is how to run this on:
### Windows:
Click on `run_chatbot.bat` on manish-llm-project directory
### Docker:
```bash
docker build -t chatbot-image .
docker run --rm -it chatbot-image
```