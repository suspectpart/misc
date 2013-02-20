new-alias Out-Clipboard $env:SystemRoot\system32\clip.exe
new-alias clip Out-Clipboard

function Get-ClipboardText()
	{
	    Add-Type -AssemblyName System.Windows.Forms
	    $tb = New-Object System.Windows.Forms.TextBox
	    $tb.Multiline = $true
	    $tb.Paste()
	    $tb.Text
	}

new-alias paste Get-ClipboardText