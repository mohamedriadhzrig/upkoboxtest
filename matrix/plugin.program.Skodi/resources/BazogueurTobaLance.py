#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui

xbmc.executebuiltin('RunPlugin(plugin://plugin.program.Skodi/?action=BazogueurTobaLance)')
xbmc.sleep(1000)
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.estuary"}}')
xbmc.sleep(100)
xbmc.executebuiltin('SendClick(11)')
xbmc.sleep(100)
xbmc.executebuiltin('System.Logoff()')
xbmc.sleep(100)
xbmc.executebuiltin('SendClick(11)')
xbmc.executebuiltin("ActivateWindow(Programs)")
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.arctic.zephyr.mod"}}')
xbmc.executebuiltin('SendClick(11)')
dialog = xbmcgui.Dialog()
dialog.ok("Skin Changer", "SkIN DOIT AVOIR CHANGÉ")