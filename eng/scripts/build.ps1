param(
    [string] $BuildNumber,
    [string] $Output,
    [string] $BuildAlphaVersion
)

[bool]$BuildAlphaVersion = $BuildAlphaVersion -in 'true', '1', 'yes', 'y'

$ErrorActionPreference = 'Stop'

$root = (Resolve-Path "$PSScriptRoot/../..").Path.Replace('\', '/')

function invoke($command) {
    Write-Host "> $command"
    Invoke-Expression $command
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Command failed: $command"
        exit $LASTEXITCODE
    }
}

Push-Location $root
try {
    if ($BuildAlphaVersion) {
        invoke "python -u eng/scripts/build.py --output-dir=`"$Output`" --version-suffix=`"-alpha.$BuildNumber`""
    } else {
        invoke "python -u eng/scripts/build.py --output-dir=`"$Output`""
    }

    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
