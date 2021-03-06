import os
import json

main_settings = {}

folders_scan = {}

folder_structure = {
    'Foto\'s': None,
    'Plannen': None,
    'Stabiliteit': [
        'Algemene documenten',
        'Berekeningen',
        'Berekeningen Scia',
        'Mails',
        'Meetstaat & borderel',
        'Plannen pdf',
        'Sondeerverslag',
        'Stabiliteitsplannen'
        ],
    'Ventilatieverslaggever': None,
    'vVGP + EPB': [
        'EPB',
        'VGP'],
    'Werfverslagen': None
    }

class Settings():
    # dossier = dict in dict -- dossier[nr][name or path]
    """
    full loading settings function for CADapp __init__
    """
    # load main settings
    def loader(self):
        print("loading settings -- change path?/chose path?")
        with open("settings.txt","r")as f:
            settings = json.load(f)
        print(settings)
        for item in settings:
            main_settings[item] = settings[item]
        with open("folders.txt","r")as f:
            folders = json.load(f)
        print(folders)
        for item in folders:
            folders_scan[item] = folders[item]
        return main_settings, folders_scan    #returns a tuple
    """---------------------------------------------------
    save settings function
    """
    def save_set(self, setting):
        print("saving settings")
        with open("settings.txt","w") as f:
            json.dump(setting, f, indent = 4) # changed order (settings, f) from (f, settings)
        print("save_set")
        print(setting)

    def save_folder(self, dossier):
        print("saving folders from scan")
        with open("folders.txt", "w") as f:
            json.dump(dossier, f, indent = 4)
        print(dossier)
    """---------------------------------------------------
    """
    def load_set(self, name):
        """?    needs to save setting + does not load, but gets specific setting, change name?"""
        print("loads specific setting(?) + checks for existing setting (?)")
        with open("settings.txt", "r") as f:
            self.settings = json.load(f)
        if name in self.settings:
            print("found setting")
            print(self.settings[name])
            return self.settings[name]
        else:
            print("nothing found")
            pass

    #loads dossier settings
    """ADD check for missing folders here?
    """
    def load_dossier(self, dossier):
        print("loads dossier(?)")
        with open("folders.txt", "r") as f:
            self.loading = json.load(f)
            print(self.loading[dossier])
            return self.loading[dossier]

    #read dossiers folders from path
        """?    simpler solution"""
    def read_folders(self, scanpath):
        #main directory path
        print("scanning folders --- change name(?)")
        self.dir = scanpath
        self.dossier = {}
        #create dict (dossier:name)
        #get only folder names
        dirs = [d for d in os.listdir(self.dir) if os.path.isdir(os.path.join(self.dir, d))]
        x = 0
        for folder in dirs:
            a = folder[:4]
            b = folder[7:]
            self.dossier[a] = {}
            self.dossier[a]["name"] = b
            #get full path
            z = [d for d in (os.path.join(self.dir, d1) for d1 in os.listdir(self.dir)) if os.path.isdir(d)]
            self.dossier[a]["path"] = z[x]
            x += 1
        print(self.dossier)
        return self.dossier



        """
        ?       one of the other       ?
        """
    #check if dirs exist for ALL SAVED dossiers
    def check_folders(self, folder_scan):
        """
        ONLY DO THIS FOR INPUT DOSSIER? ? ? ?
        """
        for key in folder_scan:
            print(key)
            print(folder_scan[key])
            print(folder_scan[key]['path'])
            for maps in folder_structure:
                if folder_structure[maps] == None:
                    print("none for {}".format(maps))
                    scanpath = folder_scan[key]['path'] + "//" + maps
                    print(scanpath)
                    self.create_dirs(scanpath)
                else:
                    print("map for {}".format(maps))
                    print(folder_structure[maps])

                    #fix item is list iterate trough list?
                    for item in folder_structure[maps]:
                        print(item)
                        scanpath = folder_scan[key]['path'] + "//" + maps + "//" + item
                        print(scanpath)
                        self.create_dirs(scanpath)

    #check if dirs exist for SPECIFIC dossiers
    def dossier_dir(self, folder_scan):
        path = folder_scan['path']
        for maps in folder_structure:
            if folder_structure[maps] == None:
                    scanpath = folder_scan['path'] + "//" + maps
                    self.create_dirs(scanpath)
            else:
                for item in folder_structure[maps]:
                    scanpath = folder_scan['path'] + "//" + maps + "//" + item
                    self.create_dirs(scanpath)



    # create dirs if they don't exist
    def create_dirs(self, scanpath):
        """
        ADD ??
        if not os.path.exists(directory):
        os.makedirs(directory)
        """

        """
        BETTER ADD??
        import errno

        def make_sure_path_exists(path):
            try:
                os.makedirs(path)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise

                    we try to create the directories, but if they
                    already exist we ignore the error.
                    On the other hand, any other error gets reported.
                    For example, if you create dir 'a' beforehand and
                    remove all permissions from it,you will get an
                    OSError raised with errno.EACCES (Permission denied,
                    error 13).
        """
        print("create nonexisting dirs")
        try:
            print("only scans paths(?)")

            os.makedirs(scanpath)
        except OSError:
            if not os.path.isdir(scanpath):
                print("if not existing (?) ADD STUFF CHECK Settings.py")
                raise

    def structure(self):
        return folder_structure
