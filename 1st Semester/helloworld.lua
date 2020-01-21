local wx = require 'wx'

local PATH_TO_APPLICATION = [[notepad.exe]]     -- Windows assumed for sake of exemplification

local ans = wx.wxMessageBox( "Should the application be started?", "Hi there!",
    wx.wxOK + wx.wxCANCEL + wx.wxICON_QUESTION )
if ans == wx.wxOK then
    wx.wxExecute( PATH_TO_APPLICATION )
end

print("The application has exited") -- this is what gets printed out