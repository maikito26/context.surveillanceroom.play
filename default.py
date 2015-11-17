import xbmc, xbmcaddon

if __name__ == "__main__":
    
    PREVIEW = 0
    SINGLECAMERA = 1
    ALLCAMERAS = 2

    __addon__ = xbmcaddon.Addon()
    
    _type = int(__addon__.getSetting('type'))
    
    if _type == PREVIEW:
        for camera_number in "123456":
            if __addon__.getSetting('camera%s' %camera_number) == 'true':
                xbmc.executebuiltin('RunPlugin(plugin://plugin.video.surveillanceroom?action=show_preview&camera_number=%s)' %camera_number)
 
    elif _type == SINGLECAMERA:
        camera_number = int(__addon__.getSetting('camera')) + 1
        if __addon__.getSetting('controls') == 'true':
            xbmc.executebuiltin('RunPlugin(plugin://plugin.video.surveillanceroom?action=single_camera&camera_number=%s)' %camera_number)
        else:
            xbmc.executebuiltin('RunPlugin(plugin://plugin.video.surveillanceroom?action=single_camera_no_controls&camera_number=%s)' %camera_number)
        
    else:
        xbmc.executebuiltin('RunPlugin(plugin://plugin.video.surveillanceroom?action=all_cameras)')

