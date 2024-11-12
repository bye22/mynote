FileEncoding ("UTF-8-RAW")
;@Ahk2Exe-UpdateManifest 1

ConfigPath := "世界RPG配置文件.ini"
ConfigLoadSection := "世界RPG"
ConfigLoadKey := "存档文件"
ConfigStartScriptKey := "开启脚本按键"

MyGui := Gui()
SelectLoadFile := MyGui.Add("Button", "x420 y9 w100", "选择存档文件")
OpenLodeDirBtn := MyGui.Add("Button", "x420 y39 w100", "打开文件目录")
CopyFileBtn := MyGui.Add("Button", "x420 y65 w100", "备份所有存档")
LoadText := MyGui.Add("Edit", "x10 y10 w400")
MyGui.AddText("x10 y45", "读取职业:")
MyProfession := MyGui.AddText("x70 y45 w100")
MyGui.AddText("x170 y45", "脚本启用按键1: ")
try
	MyHotKey := MyGui.AddHotkey("x250 y40 w120", GetLoadConfig(ConfigStartScriptKey))
catch
	MyHotKey := MyGui.AddHotkey("x250 y40 w120","vChosenHotkey")
MyGui.AddText("x170 y68", "脚本启用按键2: ")
MyHotKey2 := MyGui.AddHotkey("x250 y65 w120", "vSecondHotkey")

MyGui.AddText("x10 y90", "鼠标连点:")
MyGui.AddText("x10 y110", "间隔(毫秒):")
ClickInterval := MyGui.Add("Edit","x250 y102 w120","")
MyGui.AddText("x10 y130", "快捷键(hotkey):")
ClickHotKey := MyGui.AddHotkey("x250 y125 w120","vClickHotkey")
ClickBtnType :=MyGui.Add("DDL", "vcbx x380 y125 w120 Choose1", ["左键(Left)","右键(Right)"])
HotChaeckBox := MyGui.AddCheckBox("x10 y150", "改键(hotkey):Alt+QWERTF=>Num784512:")
xf_HotkBox := MyGui.AddCheckBox("x10 y170", "智能施法开关(```):血法-QWEF")


RunWar3Btn := MyGui.Add("Button", "x250 y200 w100", "运行魔兽争霸3")
MyGui.Show

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;~ 托盘菜单
Persistent
Tray := A_TrayMenu ; 为了方便.
;~ Tray.Delete() ; 删除标准项目.

Tray.Add("打开窗口", OpenWinActive)
;~ Tray.Add("退出", DestroyWin)

OpenWinActive(*)
{
    MyGui.Show
}

OnExit CopyFile

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



global OldHotKey := MyHotKey.Value

LoadText.OnEvent("Change", LoadTextChange)
SelectLoadFile.OnEvent("Click", OpenFile)
OpenLodeDirBtn.OnEvent("Click", OpenLodeDir)
CopyFileBtn.OnEvent("Click", CopyFile)
MyHotKey.OnEvent("Change", MyHotKeyChange)
MyHotKey2.OnEvent("Change", MyHotKey2Change)
ClickHotKey.OnEvent("Change", ClickHotKeyChange)
ClickInterval.onEvent("Change", ClickIntervalChange)
ClickBtnType.onEvent("Change",ClickBtnTypeChange)
HotChaeckBox.onEvent("Click",HotChaeckBoxChange)
xf_HotkBox.onEvent("Click",xf_HotkBoxChange)
RunWar3Btn.onEvent("Click",RunWar3BtnChange)
init()

;初始化
init()
{
    global OldHotKey, OldHotKey2, OldClickHotKey, MyHotKey, MyHotKey2, ClickHotKey, LoadText
	global IsClicking := false  ; 初始状态为不连点
	global ClickInterval ; 设置点击间隔为100毫秒
	global IswaitHotsFlag :=false ;智能施法
	OutputDebug "debug"
    if (FileExist(ConfigPath))
    {
        try {
			CopyFile
            if (GetLoadConfig(ConfigLoadKey) != "")
                LoadText.Value := GetLoadConfig(ConfigLoadKey)
				LoadTextChange(LoadText)
            if (GetLoadConfig(ConfigStartScriptKey) != "")
                Hotkey(MyHotKey.Value, AutoLoad, "On")
            if (GetLoadConfig("开启脚本按键2") != "")
                MyHotKey2.Value := GetLoadConfig("开启脚本按键2")
                Hotkey(MyHotKey2.Value, AutoLoadSecond, "On")
			if (GetLoadConfig("开启鼠标点击按键") != "")
				 ClickHotKey.Value := GetLoadConfig("开启鼠标点击按键")
				 Hotkey(ClickHotKey.Value, AutoLoadClick, "On")
			if (GetLoadConfig("设置点击间隔") != "")
				ClickInterval.Value := GetLoadConfig("设置点击间隔")
				ClickIntervalChange(ClickInterval)
			if (GetLoadConfig("设置鼠标按键类型") != "")
				ClickBtnType.Value := GetLoadConfig("设置鼠标按键类型")
				ClickBtnTypeChange(ClickBtnType)
        }
    }
    OldHotKey := MyHotKey.Value
    OldHotKey2 := MyHotKey2.Value
	OldClickHotKey := ClickHotKey.Value
}


;~ 改键小键盘
HotkeyAction(action) {
    keys := ["!q", "!w", "!e", "!r", "!t", "!f"]
    for key in keys {
        Hotkey(key, MyFunc, action)
    }
}

HotChaeckBoxChange(*) {
    if (HotChaeckBox.value == 1) {
        HotkeyAction("On")
    } else if (HotChaeckBox.value == 0) {
        HotkeyAction("Off")
    } else {
        MsgBox "错误: 无效的选项，请选择 0 或 1。"
    }
}


MyFunc(ThisHotkey)
{
	if("!q"==ThisHotkey){
		Send "{Numpad7}"
	}else if("!w"==ThisHotkey){
		Send "{Numpad8}"
	}else if("!e"==ThisHotkey){
		Send "{Numpad4}"
	}else if("!r"==ThisHotkey){
		Send "{Numpad5}"
	}else if("!t"==ThisHotkey){
		Send "{Numpad1}"
	}else if("!f"==ThisHotkey){
		Send "{Numpad2}"
	}
}

/*
	读取第一行存档代码
*/

AutoLoad(ThisHotkey)
{
	if (!CheckFilePath(ControlGetText(LoadText))) {
        MsgBox "错误: 无效的存档文件路径。"
        return
    }

    ; 读取并复制存档代码
    FirstStr := CusLoopFile(ControlGetText(LoadText), "call Preload( `"存档代码 1: ", "存档代码 1: ", "`" ")
    if (FirstStr == "False") {
        MsgBox "存档代码读取失败，请检查存档文件。"
        return
    }

    ; 复制到剪切板并执行按键操作
	FirstStr:= "-load " StrReplace(FirstStr,"-load ")
    A_Clipboard := FirstStr
    Send "{Enter}"
    Send "{Ctrl Down}v{Ctrl Up}"
    Send "{Enter}"
}

/*
	读取第二行存档代码
*/
AutoLoadSecond(ThisHotkey)
{
    if (!CheckFilePath(ControlGetText(LoadText))) {
        MsgBox "错误: 无效的存档文件路径。"
        return
    }

    ; 读取并复制存档代码
    sencondStr := CusLoopFile(ControlGetText(LoadText), "call Preload( `"存档代码 2: ", "存档代码 2: ", "`" ")
    if (sencondStr == "False") {
        MsgBox "存档代码读取失败，请检查存档文件。"
        return
    }

    ; 复制到剪切板并执行按键操作
	sencondStr:= "-load " StrReplace(sencondStr,"-load ")
    A_Clipboard := sencondStr
    Send "{Enter}"
    Send "{Ctrl Down}v{Ctrl Up}"
    Send "{Enter}"
}



/*
	处理鼠标点击事件
*/
AutoLoadClick(ThisHotkey)
{
    global IsClicking
    if IsClicking {  ; 如果已经在连点，则停止
        IsClicking := false
        SetTimer(ClickBtnTypeChange, -1)  ; 关闭定时器
    } else {  ; 否则，开始连点
        IsClicking := true
        SetTimer(ClickBtnTypeChange, ClickInterval.Value)  ; 开启定时器，设定点击间隔
    }
}


MyHotKeyChange(*)
{
	try
	{
		Hotkey(OldHotKey, AutoLoad, "off")
		Hotkey(MyHotKey.Value, AutoLoad, "on")
		global OldHotKey := MyHotKey.Value
		SaveConfig(MyHotKey.Value, ConfigStartScriptKey)
	}
}
MyHotKey2Change(*)
{
    global OldHotKey2, MyHotKey2
    try
    {
        Hotkey(OldHotKey2, AutoLoadSecond, "Off")
        Hotkey(MyHotKey2.Value, AutoLoadSecond, "On")
        OldHotKey2 := MyHotKey2.Value
        SaveConfig(MyHotKey2.Value, "开启脚本按键2")
    }
}

ClickHotKeyChange(*)
{
    global OldClickHotKey, ClickHotKey
    try
    {
        if (ClickHotKey.Value != "")
        {
            Hotkey(OldClickHotKey, AutoLoadClick, "Off")  ; 先关闭上一个热键
            Hotkey(ClickHotKey.Value, AutoLoadClick, "On")  ; 激活新的热键
            OldClickHotKey := ClickHotKey.Value
            SaveConfig(ClickHotKey.Value, "开启鼠标点击按键")
        }
    }
}

LoadTextChange(*)
{
	if(CheckFilePath(ControlGetText(LoadText)))
	{
		SaveConfig(ControlGetText(LoadText), ConfigLoadKey)
		middleString := CusLoopFile(ControlGetText(LoadText), "职业", ": ", "`" ")
		ControlSetText(middleString, MyProfession)
	}else
	{
		ControlSetText("", MyProfession)
	}
}

/*
	延迟时间设置（毫秒）
*/
ClickIntervalChange(*)
{
	if(IsNumber(ControlGetText(ClickInterval)) == "0")
	{
		MsgBox "请输入一个自然数"
		ControlSetText("" ,ClickInterval)
	}else
	{
		SaveConfig(ControlGetText(ClickInterval), "设置点击间隔")
	}
}
;~ 按钮类型判断左击或右击
ClickBtnTypeChange(*)
{
	SaveConfig(ClickBtnType.Value, "设置鼠标按键类型")
	if(IsClicking)
	{
		if(ControlGetIndex(ClickBtnType) == 1)
		{
			;~ OutputDebug 1
			Click
		}
		if(ControlGetIndex(ClickBtnType) == 2)
		{
			Click "Right"
		}
	}
}

;打开存档目录
OpenLodeDir(*)
{
	if(FileExist(GetLoadConfig(ConfigLoadKey)))
	{
		Run Format("explorer.exe {1}", GetLodeDir())
	}else
	{
		MsgBox "存档文件不存在"
	}
}
;~ 备份存档
CopyFile(*)
{
	global erroCount :=0
		try
			FileCopy "D:\Warcraft.3.v1.20e-v1.27a.CHS.Green.Edition\TWRPG\*.txt", "D:\Warcraft.3.v1.20e-v1.27a.CHS.Green.Edition\TWRPG\备份\*.*" , 1
		catch as Err
			erroCount++
		if(erroCount==0){
			ToolTip "备份成功"
			SetTimer () => ToolTip(), -2000  ;2秒后自动消失
		} else if(erroCount>0){
			ToolTip "备份失败"
			SetTimer () => ToolTip(), -2000
		}
}
;~ 运行魔兽争霸
RunWar3BtnChange(*)
{
;~ 《魔兽争霸Ⅲ》还有一些隐藏的游戏运行参数：
;~ 　　-window 游戏以窗口模式运行
;~ 　　-fullscreen 游戏以全屏模式运行(默认)
;~ 　　-loadfile "filename" 进入游戏直接读取文件,如果是w3m/w3x文件则直接进行单人游戏,如果是w3g则直接播放replay
;~ 　　-datadir "dir"数据目录,用于替换当前《魔兽争霸Ⅲ》的一些内部文件制作特殊版本或MOD(将要修改的war3.mpq/war3xloacl.mpq/war3patch.mpq中的文件连同目录解压到这个目录里修改即可)
;~ 　　-classic 进入ROC游戏(仅用于TFT)
;~ 　　-swtnl 关闭部分透明和光影以兼容旧显卡
;~ 　　-opengl 用OpenGL模式
;~ 　　-d3d 用D3D模式(默认)
	Run "D:\Warcraft.3.v1.20e-v1.27a.CHS.Green.Edition\Frozen Throne.exe"
}

;获取存档目录
GetLodeDir()
{
	endIndex := InStr(ControlGetText(LoadText), "\", , , -1)
	middleString := SubStr(ControlGetText(LoadText), 1, endIndex)
	return middleString
}

;选择存档文件并保存到配置文件中
OpenFile(*)
{
	SelectedFile := FileSelect(3, GetLodeDir() , "Open a file", "Text Documents (*.txt;)")
	if(SelectedFile != "")
	{
		ControlSetText(SelectedFile, LoadText)
		SaveConfig(SelectedFile, ConfigLoadKey)
	}
}

;保存配置文件
SaveConfig(newConfigText, LoadKey)
{
	if(!FileExist(ConfigPath))
	{
		FileAppend "[世界RPG]`n", ConfigPath, "CP0"
	}
	IniWrite newConfigText, ConfigPath, ConfigLoadSection, LoadKey

}

;读取存档配置
GetLoadConfig(Key)
{
	return IniRead(ConfigPath, ConfigLoadSection, Key)
}

;截取2个字符串之间的字符串
CustomSubStr(str ,startTag, endTag)
{
	startIndex := InStr(str, startTag) + StrLen(startTag)
	endIndex := InStr(str, endTag)
	middleString := SubStr(str, startIndex, endIndex - startIndex)
	if (startIndex > 0 && endIndex > 0) {
		return SubStr(str, startIndex, endIndex - startIndex)
	}else
	{
		return "False"
	}
}

;逐行读取文件
CusLoopFile(FilePath, Needle, startTag, endTag)
{
	middleString := ""
	if(CheckFilePath(FilePath))
	{
		Loop read, FilePath
		{
			if InStr(A_LoopReadLine, Needle)
			{
				str := A_LoopReadLine
				middleString := middleString CustomSubStr(str ,startTag, endTag)
				if(middleString == "False" )
				{
					MsgBox "读取存档失败"
					break
				}
			}
		}
	}
	return middleString
}

CheckFilePath(FilePath)
{
	return FileExist(FilePath) && InStr(FilePath, ".txt") > 0
}



;;;;;;智能施法;;;;;;;;;;;
`::{
	    global IswaitHotsFlag
		if IswaitHotsFlag {  ; 如果已经在连点，则停止
			IswaitHotsFlag := false
			xf_HotkBox.value:=0
		} else {  ; 否则，开始启用
			IswaitHotsFlag := true
			xf_HotkBox.value:=1
		}
		xf_HotkBoxChange
	}
waitHots(ThisHotkey){
			 KeyWait StrReplace(ThisHotkey,"~")  ; 等待用户物理释放按键.
			 Click
}

xf_HotkBoxChange(*){
	if(xf_HotkBox.value==1){
			Hotkey "~q" ,waitHots,"On"
			Hotkey "~w" ,waitHots,"On"
			Hotkey "~e" ,waitHots,"On"
			Hotkey "~f" ,waitHots,"On"
		}else{
			Hotkey "~q" ,waitHots,"Off"
			Hotkey "~w" ,waitHots,"Off"
			Hotkey "~e" ,waitHots,"Off"
			Hotkey "~f" ,waitHots,"Off"
		}
}
