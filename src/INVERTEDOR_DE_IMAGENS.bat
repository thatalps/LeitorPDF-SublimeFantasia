@echo off
REM Este script sobrescreve as imagens JPG arrastadas aplicando espelhamento horizontal

REM Verifica se o ImageMagick está disponível
where magick >nul 2>&1
if errorlevel 1 (
    echo ImageMagick nao encontrado. Instale em: https://imagemagick.org
    pause
    exit /b
)

REM Loop por todos os arquivos arrastados
for %%F in (%*) do (
    echo Espelhando: "%%~fF"
    magick "%%~fF" -flop "%%~fF"
)

echo.
echo Concluído. Imagens sobrescritas com sucesso.
pause
