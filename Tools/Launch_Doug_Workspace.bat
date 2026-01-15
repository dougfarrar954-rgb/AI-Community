@echo off
:: ==================================================
:: Doug's Workspace Launcher
:: ==================================================
echo.
echo Launching Doug's Workspace...
echo.

:: 1. Antigravity (VS Code) - Opening the GitHub folder
echo [1/5] Opening Antigravity (c:\Users\dougf\Documents\GitHUB)...
start "" "C:\Users\dougf\AppData\Local\Programs\Antigravity\Antigravity.exe" "c:\Users\dougf\Documents\GitHUB"

:: 2. Google Chrome - Opening specified tabs
echo [2/5] Opening Google Chrome Tabs...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://studio.pickaxe.co/STUDIO1R5KFM1HGQWS6S2/JKCAZZ93O0" "https://pickaxe.co/user/dashboard" "https://gemini.google.com/app" "https://github.com/dougfarrar954-rgb"

:: 3. TickTick (Chrome App)
echo [3/5] Opening TickTick...
start "" "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" --profile-directory=Default --app-id=cfammbeebmjdpoppachopcohfchgjapd

:: 4. Notion
echo [4/5] Opening Notion...
if exist "%LOCALAPPDATA%\Programs\Notion\Notion.exe" (
    start "" "%LOCALAPPDATA%\Programs\Notion\Notion.exe"
) else (
    echo    - Notion executable not found in default location.
)

:: 5. Wispr Flow
echo [5/5] Opening Wispr Flow...
if exist "%LOCALAPPDATA%\WisprFlow\Wispr Flow.exe" (
    start "" "%LOCALAPPDATA%\WisprFlow\Wispr Flow.exe"
) else (
    echo    - Wispr Flow executable not found in default location.
)

echo.
echo All set! Have a productive session.
echo (Closing in 5 seconds...)
timeout /t 5 > nul
exit
