@echo off
REM Run the build_and_run.sh script inside WSL (recommended)
REM This batch file will try to call WSL and execute the build script. If you prefer, open WSL and run scripts/build_and_run.sh manually.

echo Building and running kernel inside WSL. If you don't have WSL configured, open new-os/scripts/build_and_run.sh in WSL and run it manually.

REM Attempt to run the build script in WSL
wsl -e bash -lc "cd '$(wslpath -a "%~dp0")/new-os' || cd '/mnt/c/\Users/$(whoami)/OneDrive/Ambiente de Trabalho/Repositórios/MIROBOTS/Downloads/Operational System/new-os' ; ./scripts/build_and_run.sh"

pause
