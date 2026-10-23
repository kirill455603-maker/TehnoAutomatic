@echo off
rem apply_patch.bat - применяет патч из patches/ и удаляет его после применения
rem Использование: apply_patch.bat 0001-xxx.patch
setlocal
set PATCH=%~1
if "%PATCH%"=="" ( echo Использование: apply_patch.bat ^<имя файла патча^> & exit /b 1 )
if not exist "%PATCH%" if exist "patches\%PATCH%" set PATCH=patches\%PATCH%
if not exist "%PATCH%" ( echo Файл не найден: %PATCH% & exit /b 1 )
git apply --check "%PATCH%" 2>nul
if %errorlevel%==0 (
    git am --keep-non-patch -q "%PATCH%" && echo Патч применен с коммитом
) else (
    echo git am невозможен, пробую git apply...
    git apply --3way "%PATCH%" && echo Патч наложен без автокоммита
)
del "%PATCH%"
echo Файл %PATCH% удален.
endlocal
