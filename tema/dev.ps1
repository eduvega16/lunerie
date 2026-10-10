# Vista previa local del tema en http://127.0.0.1:9292 (shopify theme dev; no toca la tienda real).
# Lee la contraseña de la tienda de .claude\store-password (fuera de git, solo en cada PC); si no existe, la pide.
# Claude la lanza en segundo plano desde VS Code (sin abrir ventanas):
#   shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda --store-password "$(cat .claude/store-password)"
# Este script es para lanzarla a mano:  powershell -ExecutionPolicy Bypass -File tema\dev.ps1
$repo = Split-Path $PSScriptRoot
Set-Location $repo
New-Item -ItemType Directory -Force '.claude' | Out-Null
$fichero = Join-Path $repo '.claude\store-password'
if (Test-Path $fichero) {
    $p = (Get-Content $fichero -Raw).Trim()
} else {
    $sec = Read-Host -AsSecureString 'Contrasena de la tienda'
    $p = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec))
}
shopify theme dev --store qjxvnn-xq.myshopify.com --path tema/tienda --store-password $p 2>&1 |
    Tee-Object -FilePath (Join-Path $repo '.claude\theme-dev.log')
