$modules = $profile.Replace("Microsoft.PowerShell_profile.ps1", "modules\")
gci $modules | foreach {. $modules\$_ }