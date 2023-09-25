param(
    [string] $UseTypeSpecNext
)

[bool]$UseTypeSpecNext = $useTypeSpecNext -in 'true', '1', 'yes', 'y'

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
    invoke "python eng/scripts/init.py --use-typespec-next=$UseTypeSpecNext"

    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
