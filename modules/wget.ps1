Function wget() 
{
	param($address);
	$wc = New-Object System.Net.WebClient;
	return $wc.DownloadString($address);
}