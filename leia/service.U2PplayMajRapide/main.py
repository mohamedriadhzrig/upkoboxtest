# -*- coding: utf-8 -*-

from resources.lib import service

import xbmcaddon

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon('plugin.video.sendtokodiU2P')

service.run()


