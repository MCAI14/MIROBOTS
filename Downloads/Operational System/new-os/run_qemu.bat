@echo off
REM Run the build_and_run.sh script inside WSL (recommended)
REM This batch file will try to call WSL and execute the build script. If you prefer, open WSL and run scripts/build_and_run.sh manually.

echo Building and running kernel inside WSL. If you don't have WSL configured, open new-os/scripts/build_and_run.sh in WSL and run it manually.

REM Attempt to run the build script in WSL
setlocal
REM This script will try to run QEMU natively on Windows if the bootimage exists.
REM If the image is not present, it will instruct you to build inside WSL using the provided script.

set KERNEL_BIN=%~dp0new-os\target\x86_64-blog_os\debug\bootimage-kernel.bin

echo Looking for kernel image at:
echo   "%KERNEL_BIN%"

if exist "%KERNEL_BIN%" (
	echo Found kernel image.
	echo Starting QEMU (Windows native qemu-system-x86_64.exe must be in PATH)...
	qemu-system-x86_64 -drive format=raw,file="%KERNEL_BIN%" -serial stdio -display none
) else (
	echo Kernel image not found.
	echo To build the bootable image, run the build script inside WSL (recommended):
	echo   1) Open WSL/Ubuntu
	echo   2) cd to the Windows path of this project, e.g.:
	echo      cd /mnt/c/Users/<teu-usuario>/OneDrive/"Ambiente de Trabalho"/Repositórios/MIROBOTS/Downloads/"Operational System"/new-os
	echo   3) chmod +x scripts/build_and_run.sh
	echo   4) ./scripts/build_and_run.sh
	echo
	echo Alternatively, after building in WSL you can come back here and re-run this batch to use QEMU nativo.
)

endlocal
pause

pause
