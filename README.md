# Serpent Group 🐍

<p align=center>
    <img src="img/serpent.jpg" width="70%">
</p>


A brief and technical study about a malicious campaign targeting french entities in the construction, real estate and government industries.

---

## Intro

In march 2022, **Proofpoint** identified a new email campaign aimed at french entities, one month before the presidential elections.

The security firm attributed this campaign to a likely advanced threat actor, named **Serpent Group**, based on the TTPs observed especially leveraging the python language as a vector. The ultimate objective still remains unknown. 

This study focuses on detailing and reproducing the initial access techniques and procedures used during this campaign.

---

## Initial Access

Attackers used spear-phishing with attachment (MITRE T1566.001) and a resume-themed subject line. 

<p align=center>
    <img src="img/email.png" width="80%">
</p>


The attached Microsoft Word document, masquerading as an information related to GPDR, contained a malicious VBA macro which downloads an image (```https://www.fhccu[.]com/images/ship3[.]jpg```)  that contains a powershell script embedded and executes it.

The use of this steganography technique is well documented ([**MITRE T1027.003**](hhttps://attack.mitre.org/software/S0231/)). Groups like **Sandworm Team** have already exploited it during their campaigns, particularly with the [**Invoke-PSImage**](https://github.com/peewpw/Invoke-PSImage) tool.

We developed our own version of the malicious VBA Macro which decrypts and executes a powershell command under the Outlook process to download an retrieve the malicious image.

<p align=center>
    <img src="img/macro.png" width="80%">
</p>

The powershell script, embedded in the image, downloads and installs **Chocolatey**, a package manager for Windows, similar to apt-get or yum on Linux systems. 

<p align=center>
    <img src="img/chocolatey.png" width="40%">
</p>

Then, the powershell script used **Chocolatey** to install **Python** and **pip** to install various dependencies including **PySocks**, on the Windows target machine. Keep in mind that this action requires administrative privileges.

Next, the powershell script downloaded another image (```https://www.fhccu[.]com/images/7[.]jpg```) containing a python script also hidden using steganography and saved the python script as **MicrosoftSecurityUpdate.py**. Finally, it created and executed a .bat script that in turn executed the malicious MicrosoftSecurityUpdate.py a.k.a [**Serpent Backdoor**](tools/MicrosoftSecurityUpdate.py).

During this study, we came up with a similar powershell script, named [**chocoloader.ps1**](tools/chocoloader.ps1), that installs [**Anaconda**](https://community.chocolatey.org/packages/anaconda3) instead which doesn't require elevated privileges. We also implemented a registry run key persistence which will run python and the serpent backdoor. 

---
## Custom C2

TODO

---
## Defense

### Registry keys

Every time a user clicks "**Enable Editing**" or "**Enable Content**" when opening a Microsoft Office file, its path is added as a value to the TrustedRecords key in the registry (*HKCU\SOFTWARE\Microsoft\Office\16.0\Word\Security\Trusted Documents\TrustRecords*).

If the last four bytes of the value are set to **FF FF FF 7F**, it means that the user enabled macros when opening this document.

A cool idea would be to write a simple script that regularly monitors all trusted documents with macros enabled, extracts the macros and looks for IOCs or any malicious activity.

### YARA Rules

Here is an example of a yara rule to detect a powershell or python script embedded in an image. This rule has been generated using chatGPT.

<pre>
<code>
rule Image_Containing_Scripting_Language
{
    meta:
        author = "chatGPT"
        description = "Rule to detect image containing PowerShell or Python script"
        reference = "https://proofpoint.com/us/threat-insight/post/serpent-group-targets-french-entities-via-malicious-image-attachments"
        date = "2022-03-01"
        hash = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p"
    strings:
        $powershell = "powershell" ascii nocase
        $python = "python" ascii nocase
        $powershell_encoded = {40 70 6F 77 65 72 73 68 65 6C 6C}
        $python_encoded = {40 70 79 74 68 6F 6E}
        $script = {63 72 65 61 74 65 20 53 63 72 69 70 74}
        $obfuscated_1 = "eval("
        $obfuscated_2 = "str_rot13("
        $obfuscated_3 = "base64_decode("

    condition:
        any of ($powershell, $python, $powershell_encoded, $python_encoded) and $script and (any of ($obfuscated_1, $obfuscated_2, $obfuscated_3))
}
</code>
</pre>

This rule looks for the strings "powershell", "python" in the file being scanned, the encoded version of the these string, the string "create script" which is a common string found in scripts, and also look for common obfuscation techniques such as eval(), str_rot13(), base64_decode().

It's also possible to add more obfuscation techniques, but keep in mind that the rule may become too specific and may not match other variations of the same script. It's always a balance between specificity and coverage.

## References

- Proofpoint : https://www.proofpoint.com/us/blog/threat-insight/serpent-no-swiping-new-backdoor-targets-french-entities-unique-attack-chain
- VMWare Threat Analysis Unit (TAU) : https://blogs.vmware.com/security/2022/04/serpent-the-backdoor-that-hides-in-plain-sight.html
