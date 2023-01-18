rule Image_Containing_Scripting_Language
{
    meta:
        author = "Your Name"
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