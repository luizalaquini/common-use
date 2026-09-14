<#
.SYNOPSIS
    Autentica no AWS CodeArtifact e configura as variáveis de ambiente que o uv
    usa para acessar o índice privado "python-packages".

.DESCRIPTION
    O token do CodeArtifact expira (padrão de 12h). Rode este script sempre que
    o token expirar, ANTES de executar comandos como `uv add`, `uv sync` ou
    `uv lock` que precisem buscar pacotes do índice privado.

    IMPORTANTE: execute com "dot sourcing" para que as variáveis fiquem
    disponíveis na sua sessão atual do PowerShell:

        . .\scripts\codeartifact-login.ps1

    (repare no ponto e no espaço antes do caminho)

.PARAMETER Profile
    Profile da AWS CLI usado para obter o token. Padrão: ContaDados.
#>

[CmdletBinding()]
param(
    [string]$Profile     = "ContaDados",
    [string]$Domain      = "data-science-ai",
    [string]$DomainOwner = "839629613889",
    [string]$Region      = "us-east-2"
)

$ErrorActionPreference = "Stop"

Write-Host "Obtendo token do CodeArtifact (profile: $Profile)..." -ForegroundColor Cyan

$token = aws codeartifact get-authorization-token `
    --domain $Domain `
    --domain-owner $DomainOwner `
    --region $Region `
    --query authorizationToken `
    --output text `
    --profile $Profile

if (-not $token) {
    Write-Error "Falha ao obter o token do CodeArtifact. Verifique suas credenciais AWS e o profile '$Profile'."
    return
}

$env:CODEARTIFACT_TOKEN                  = $token
$env:UV_INDEX_PYTHON_PACKAGES_USERNAME   = "aws"
$env:UV_INDEX_PYTHON_PACKAGES_PASSWORD   = $token

Write-Host "Login concluido. Variaveis definidas para esta sessao (token com $($token.Length) caracteres)." -ForegroundColor Green
Write-Host "Agora voce pode rodar: uv add <pacote>  /  uv sync  /  uv lock" -ForegroundColor Green
