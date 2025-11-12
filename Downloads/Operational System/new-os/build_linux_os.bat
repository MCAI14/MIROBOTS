@echo off
REM Build Linux+Calculator ISO and test in VirtualBox
setlocal enabledelayedexpansion

set PROJECT_PATH=c:\Users\misha\OneDrive\Ambiente de Trabalho\Repositórios\MIROBOTS\Downloads\Operational System\new-os

echo Building MirobotOS (Linux + Calculator)...
echo.

REM Convert Windows path to WSL path and run the build script
for /f "tokens=*" %%i in ('wsl wslpath -u "%PROJECT_PATH%"') do set WSL_PATH=%%i
wsl bash -c "cd '%WSL_PATH%' && chmod +x scripts/build_linux_iso.sh && ./scripts/build_linux_iso.sh"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build complete!
    echo ISO location: %PROJECT_PATH%\mirobotOS.iso
    echo.
    echo To test in VirtualBox:
    echo 1. Open VirtualBox
    echo 2. Create a new VM (Linux, 64-bit)
    echo 3. Under Storage, attach the ISO as a CD/DVD
    echo 4. Start the VM
    echo 5. Type 'calculator' at the shell prompt to run
) else (
    echo Build failed. Check the output above.
)

pause
