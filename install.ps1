<#
.SYNOPSIS
    Volta AI Engineer — one-command install for Windows.
.DESCRIPTION
    Checks for Node.js ≥ 18, clones/pulls the latest volta-AI-Engineer
    from GitHub, installs dependencies, and links the `volta` command.
    Run from PowerShell:
        iwr -useb https://ntronixvolta.netlify.app/install.ps1 | iex
.LINK
    https://github.com/ntronix44/volta-AI-Engineer
#>

$ErrorActionPreference = "Stop"
$host.ui.RawUI.WindowTitle = "Volta AI Engineer — Installer"

$REPO_URL  = "https://github.com/ntronix44/volta-AI-Engineer.git"
$CLONE_DIR = "$env:USERPROFILE\volta-AI-Engineer"
$VOLTA_DIR = "$env:USERPROFILE\.volta"

# ─── Color helpers ──────────────────────────────────────────────────────────
function Write-Color($color, $text) {
    Write-Host $text -ForegroundColor $color
}

# ─── 1. Check / install Node.js ─────────────────────────────────────────────
Write-Color Cyan "`n  ⚡ Volta AI Engineer — Installer`n"

$nodeExe = (Get-Command "node" -ErrorAction SilentlyContinue)
if (-not $nodeExe) {
    Write-Color Yellow "  Node.js not found. Attempting install via winget..."
    try {
        winget install -e --id OpenJS.NodeJS.LTS --accept-package-agreements 2>$null
        refreshenv 2>$null
        $nodeExe = (Get-Command "node" -ErrorAction SilentlyContinue)
    } catch {
        Write-Color Red "  ✗ winget install failed."
        Write-Host "    Please install Node.js LTS manually from https://nodejs.org and re-run."
        exit 1
    }
}

$nodeVer = (& node -v) 2>$null
Write-Color Gray "  node  $nodeVer"

# Parse major version
if ($nodeVer -match 'v(\d+)') {
    $major = [int]$Matches[1]
    if ($major -lt 18) {
        Write-Color Yellow "  ⚠  Node ≥ 18 required (found v$major). Please upgrade from https://nodejs.org"
        exit 1
    }
} else {
    Write-Color Yellow "  ⚠  Could not parse Node version. Proceeding anyway..."
}

# ─── 2. Clone / pull repo ───────────────────────────────────────────────────
if (Test-Path $CLONE_DIR) {
    Write-Color Gray "  repo exists at $CLONE_DIR — pulling latest..."
    Push-Location $CLONE_DIR
    git pull --ff-only 2>$null
    Pop-Location
} else {
    Write-Color Gray "  cloning from $REPO_URL ..."
    git clone $REPO_URL $CLONE_DIR 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Color Red "  ✗ git clone failed. Check your internet connection and try again."
        exit 1
    }
}

# ─── 3. npm install ─────────────────────────────────────────────────────────
Write-Color Gray "  installing dependencies..."
Push-Location $CLONE_DIR
npm install --no-fund --no-audit 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Color Red "  ✗ npm install failed."
    Pop-Location
    exit 1
}

# ─── 4. Link the `volta` command ────────────────────────────────────────────
$NpmPrefix = (npm config get prefix) 2>$null
if (-not $NpmPrefix -or $NpmPrefix -eq "") {
    $NpmPrefix = "$env:APPDATA\npm"
}

Write-Color Gray "  linking volta command..."
npm link 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Color Yellow "  ⚠  npm link failed. Trying npm install -g instead..."
    npm install -g . 2>$null
}

# ─── 5. Ensure ~/.volta exists ──────────────────────────────────────────────
if (-not (Test-Path $VOLTA_DIR)) {
    New-Item -ItemType Directory -Path $VOLTA_DIR -Force | Out-Null
}
$configPath = "$VOLTA_DIR\config.json"
if (-not (Test-Path $configPath)) {
    @{
        provider = "deepseek"
        maxToolIterations = 120
        streamingEnabled = $true
        autoApproveShell = $false
        autoApproveWrites = $false
        sessionMemory = $true
    } | ConvertTo-Json | Out-File $configPath -Encoding utf8
    Write-Color Gray "  created $configPath"
}

Pop-Location

# ─── 6. Done ────────────────────────────────────────────────────────────────
Write-Color Green "`n  ✓  Volta AI Engineer installed successfully!`n"
Write-Host "    Run 'volta' to start the REPL."
Write-Host "    Set your API key in $VOLTA_DIR\.env or a project .env file."
Write-Host "    Docs: https://github.com/ntronix44/volta-AI-Engineer`n"
