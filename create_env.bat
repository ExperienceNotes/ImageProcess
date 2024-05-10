@echo on
cd %USERPROFILE%
REM define your conda env name
set ENV_NAME=my_env

REM Check if your conda is installed.
call conda --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Conda doesn't install in this path. Please make sure it has been added to the system path.
    exit /b
)
REM Check if an environment with the same name already exists.
call conda env list | findstr /c:"%ENV_NAME%" > nul 2>&1
if %errorlevel% equ 0 (
    echo env "%ENV_NAME%" is already exits.
    exit /b
)
REM Create new conda env
call activate base
echo Creating conda env named "%ENV_NAME%" ...
call conda create --name %ENV_NAME% python=3.9 -y
if %errorlevel% equ 0 (
    echo env "%ENV_NAME%" Create Successful.
) else (
    echo env "%ENV_NAME%" Create fail.
)
call activate %ENV_NAME%
cd %~dp0
call pip install -r .\requirements.txt
cmd /k
