@ echo off

rem Activate the virtual environment
call venv\Scripts\activate.bat

rem Set environment variables from .env file
for /f "delims=" %%a in (.env) do set %%a

rem Run your Python script
python src\my_first_llm_app.py