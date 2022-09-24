<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui

xbmc.executebuiltin("ActivateWindow(Programs)")
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin"}}')
xbmc.executebuiltin('SendClick(11)')
dialog = xbmcgui.Dialog()
=======
#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui

xbmc.executebuiltin("ActivateWindow(Programs)")
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin"}}')
xbmc.executebuiltin('SendClick(11)')
dialog = xbmcgui.Dialog()
>>>>>>> ae015f14fa26bfbc816a3b195d7f8308e35e6511
dialog.ok("Skin Changer", "SkIN SHOULD HAVE CHANGED")