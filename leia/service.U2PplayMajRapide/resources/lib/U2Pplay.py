import xbmc
import time

xbmc.executebuiltin("Notification(Chargement HK2...)")
xbmc.sleep(3000)
xbmc.executebuiltin('PlayMedia("plugin://plugin.video.sendtokodiU2P/?action=majhkneww")')
xbmc.executebuiltin( "Notification(HK2 OK...,,5000)" )
time.sleep(30)
xbmc.executebuiltin( 'ReloadSkin()' )
xbmc.executebuiltin( "Notification(Rafraichissement Skin,,3000)" )