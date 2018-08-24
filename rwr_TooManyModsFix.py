import os, sys
import re
import xml.etree.ElementTree as ET
import winreg




print(sys.version)
path_appdata = os.getenv('APPDATA') + '\\'
path_rwrdata = path_appdata + 'Running with rifles\\'
path_settings = path_rwrdata + 'settings.xml'
 # change it to a general case


tree = ET.parse(path_settings)
root = tree.getroot()


def GetSteamPath():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
    (value, valuetype) = winreg.QueryValueEx(key, 'SteamPath')
    return value


def LaunchRWR():
    os.chdir(GetSteamPath())
    path = 'steam.exe' + ' steam://rungameid/270150'
    os.system(path)



def GetSteamAppPath():
    path_up = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return path_up + '\\'


def GetRWRPath():

    return GetSteamAppPath() + 'common\\RunningWithRifles\\'

def GetWorkshopPath():

    return GetSteamAppPath() + 'workshop\\content\\270150\\'



def ListMap():

    dirs = ['media/packages/vanilla/maps/', 'media/packages/vanilla/maps/']
    maps = []

    for index, dir_ in enumerate(dirs):
        map_ = maps.extend(os.listdir(dir_))
    

    maps = list(set(maps))
    maps.sort()
    [print(i,j) for i, j in enumerate(maps)]
    return maps


def ListMod():
    path_workshop = GetWorkshopPath()
    folders = [GetRWRPath()+"media\\packages\\"]
    for workshop_id in os.listdir(path_workshop):
        path_mod = path_workshop + workshop_id + "\\" + "media\\packages\\"
        folders.append(path_mod)


    mods = []
    for folder in folders:
        for index, mod in enumerate(os.listdir(folder)):
            mods.append(mod)



    
    mods = list(set(mods))
    mods.sort()
    [print(i, j) for i, j in enumerate(mods)]
    return mods
    

def ListOverlay():
    for overlay_path in tree.iterfind('.//enabled_overlays[@taregt]/path'):
        print(overlay_path.text)

def CrateOverlay(map_name, mod_name):
    xml = ET.fromstring('<enabled_overlays target="media/packages/vanilla/maps/' + map_name + '"><path>media/packages/' + mod_name + '</path></enabled_overlays>')
    # root.append(enabled_overlays)
    return xml



print('Here lists maps:')
maps = ListMap()
map_index = int(input('Type the map index you play: '))
map_t = maps[map_index]

print('Here lists mods:')
mods = ListMod()
mod_index = int(input('Type the mod index you play: '))
mod_t = mods[mod_index]



root.append(CrateOverlay(map_t, mod_t))

tree.write(path_settings)
print('Overlay generated for [' + mod_t + '] in [' + map_t + '].')
start = input('Start rwr right now?(y/n) ')
if start == 'y':
    LaunchRWR()


# os.system('rwr_game.exe map=media\\packages\\vanilla\\maps\\'+map_t+' package=media\\packages\\'+mod_t)


'''
A sample of target
<enabled_overlays target="media/packages/vanilla/maps/[map_name]]">
    <path>media/packages/[mod_name]</path>
</enabled_overlays>

'''

