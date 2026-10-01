param(
  [string]$BaseUrl = "http://127.0.0.1:8000"
)

$uri = "$BaseUrl/api/system/version"
Write-Host "Checking security headers on $uri"
$response = Invoke-WebRequest -Uri $uri -Method Head -UseBasicParsing
$required = @{
  "X-Content-Type-Options" = "nosniff"
  "X-Frame-Options" = "DENY"
  "Strict-Transport-Security" = "max-age=31536000; includeSubDomains"
  "Content-Security-Policy" = ""
  "Referrer-Policy" = "strict-origin-when-cross-origin"
  "Permissions-Policy" = "camera=(), microphone=(), geolocation=()"
}
$failed = $false
foreach ($name in $required.Keys) {
  $value = $response.Headers[$name]
  if ([string]::IsNullOrWhiteSpace($value) -or ($required[$name] -and $value -ne $required[$name])) {
    Write-Host "FAIL ${name}: $value" -ForegroundColor Red
    $failed = $true
  } else {
    Write-Host "OK   ${name}: $value" -ForegroundColor Green
  }
}
if ($failed) { exit 1 }
Write-Host "All security headers present." -ForegroundColor Green
