# All Datastore info
Get-Datacenter SAV,HUTOR | ForEach-Object {
	$DC = $_
	Get-Datacenter $DC | Get-Datastore | Select @{N="Datacenter";E={@($DC)}}, Name, @{N="TotalSpaceGB";E={[Math]::Round(($_.ExtensionData.Summary.Capacity)/1GB,0)}}, @{N="Type";E={@($_.Type)}}, @{N="UsedSpaceGB";E={[Math]::Round(($_.ExtensionData.Summary.Capacity - $_.ExtensionData.Summary.FreeSpace)/1GB,0)}}, @{N="ProvisionedSpaceGB";E={[Math]::Round(($_.ExtensionData.Summary.Capacity - $_.ExtensionData.Summary.FreeSpace + $_.ExtensionData.Summary.Uncommitted)/1GB,0)}}, @{N="FreeSpaceGB";E={[Math]::Round(($_.ExtensionData.Summary.FreeSpace)/1GB,0)}}, @{N="NumVM";E={@($_ | Get-VM ).Count}},@{N="NumVMHost";E={@($_ | Get-VMHost ).Count}} 
} | Export-Csv -Path C:\vmware\stat\datastores.csv -NoTypeInformation -UseCulture