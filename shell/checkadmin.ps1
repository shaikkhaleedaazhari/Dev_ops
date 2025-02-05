# Check if the current user is an administrator
$adminGroup = [System.Security.Principal.WindowsBuiltInRole]::Administrator
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()

if ($currentUser.Groups -match $adminGroup) {
    Write-Host "The current user has administrative privileges."
} else {
    Write-Host "The current user does not have administrative privileges."
}


#:: its noting but calling the method
