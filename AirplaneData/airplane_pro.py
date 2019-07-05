
class AI():
    def __init__(self):
        self.yindaoche = 0
        self.feiji = 0
        self.ketiche = 0
        self.jiayouche = 0
        self.qianyinche = 0
        self.kecangmen = 0
        self.huocangmen = 0
        self.canche = 0

    def get_date(self, content):
        try:
            self.yindaoche += float(content.split()[1])
            self.feiji += float(content.split()[3])
            self.ketiche += float(content.split()[5])
            self.jiayouche += float(content.split()[7])
            self.qianyinche += float(content.split()[9])
            self.kecangmen += float(content.split()[11])
            self.huocangmen += float(content.split()[13])
            self.canche += float(content.split()[15])
        except:
            print("输入txt不符合要求")
        return (self.yindaoche, self.feiji, self.ketiche, self.jiayouche, self.qianyinche, self.kecangmen, self.huocangmen, self.canche)


class RG():
    def __init__(self):
        self.yindaoche = 0
        self.feiji = 0
        self.ketiche = 0
        self.jiayouche = 0
        self.qianyinche = 0
        self.kecangmen = 0
        self.huocangmen = 0
        self.canche = 0

    def get_date(self, content):
        try:
            self.yindaoche += float(content.split()[17])
            self.feiji += float(content.split()[19])
            self.ketiche += float(content.split()[21])
            self.jiayouche += float(content.split()[23])
            self.qianyinche += float(content.split()[25])
            self.kecangmen += float(content.split()[27])
            self.huocangmen += float(content.split()[29])
            self.canche += float(content.split()[31])
        except:
            print("输入txt不符合要求")
        return (self.yindaoche, self.feiji, self.ketiche, self.jiayouche, self.qianyinche, self.kecangmen, self.huocangmen, self.canche)


class LOU():
    def __init__(self):
        self.yindaoche = 0
        self.feiji = 0
        self.ketiche = 0
        self.jiayouche = 0
        self.qianyinche = 0
        self.kecangmen = 0
        self.huocangmen = 0
        self.canche = 0

    def get_date(self, content):
        try:
            self.yindaoche += float(content.split()[33])
            self.feiji += float(content.split()[35])
            self.ketiche += float(content.split()[37])
            self.jiayouche += float(content.split()[39])
            self.qianyinche += float(content.split()[41])
            self.kecangmen += float(content.split()[43])
            self.huocangmen += float(content.split()[45])
            self.canche += float(content.split()[47])
        except:
            print("输入txt不符合要求")
        return (self.yindaoche, self.feiji, self.ketiche, self.jiayouche, self.qianyinche, self.kecangmen, self.huocangmen, self.canche)
