$ErrorActionPreference = "Continue"
$cleanPath = ($env:PATH -split ';' | Where-Object { $_ -ne '' -and (Test-Path -Path $_ -PathType Container) }) -join ';'
$env:PATH = $cleanPath

Set-Location -Path $PSScriptRoot

Write-Output "=== Pass 1: pdflatex ==="
& "C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode main.tex | Out-Null

Write-Output "=== Pass 2: bibtex ==="
& "C:\Program Files\MiKTeX\miktex\bin\x64\bibtex.exe" main

Write-Output "=== Pass 3: pdflatex ==="
& "C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode main.tex | Out-Null

Write-Output "=== Pass 4: pdflatex (final) ==="
$finalOutput = & "C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode main.tex

Write-Output "=== Compilation Summary ==="
$errors = $finalOutput | Where-Object { $_ -match "^!\s" }
if ($errors) {
    Write-Output "Errors detected:"
    $errors
} else {
    Write-Output "SUCCESS: 0 fatal LaTeX errors."
}

$warnings = $finalOutput | Where-Object { $_ -match "Warning:" }
Write-Output "Warnings: $($warnings.Count)"
$warnings | Select-Object -First 10

if (Test-Path "main.pdf") {
    $pdf = Get-Item "main.pdf"
    Write-Output "Generated PDF: $($pdf.FullName) ($($pdf.Length) bytes, LastWriteTime: $($pdf.LastWriteTime))"
}

