import xbmc
import time

xbmc.executebuiltin("Notification(Chargement HK2...)")
xbmc.sleep(1000)
xbmc.executebuiltin('PlayMedia("plugin://plugin.video.sendtokodiU2P/?action=majhkneww")')
xbmc.executebuiltin( "Notification(HK2 OK...,,2000)" )
time.sleep(5)
xbmc.executebuiltin( 'ReloadSkin()' )
xbmc.executebuiltin( "Notification(Rafraichissement Skin,,2000)" )