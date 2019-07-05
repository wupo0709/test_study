import os
from AirplaneData.airplane_pro import AI, RG, LOU

jianchu_yindaoche = zhaohui_yindaoche = ""
jianchu_ketiche = zhaohui_ketiche = ""
jianchu_feiji = zhaohui_feiji = ""
jianchu_jiayouche = zhaohui_jiayouche = ""
jianchu_qianyinche = zhaohui_qianyinche = ""
jianchu_kecangmen = zhaohui_kecangmen = ""
jianchu_huocangmen = zhaohui_huocangmen = ""
jianchu_canche = zhaohui_canche = ""
# abspath = os.path.abspath(".")
# dirname = os.path.dirname(abspath)
ai = AI()
rg = RG()
lou = LOU()
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name == "result.txt":
            with open(os.path.join(root, name), "r", encoding="gbk") as f:
                content = f.read()

            ai_date = ai.get_date(content)
            ai.yindaoche = ai_date[0]
            ai.feiji = ai_date[1]
            ai.ketiche = ai_date[2]
            ai.jiayouche = ai_date[3]
            ai.qianyinche = ai_date[4]
            ai.kecangmen = ai_date[5]
            ai.huocangmen = ai_date[6]
            ai.canche = ai_date[7]

            rg_date = rg.get_date(content)
            rg.yindaoche = rg_date[0]
            rg.feiji = rg_date[1]
            rg.ketiche = rg_date[2]
            rg.jiayouche = rg_date[3]
            rg.qianyinche = rg_date[4]
            rg.kecangmen = rg_date[5]
            rg.huocangmen = rg_date[6]
            rg.canche = rg_date[7]

            lou_date = lou.get_date(content)
            lou.yindaoche = lou_date[0]
            lou.feiji = lou_date[1]
            lou.ketiche = lou_date[2]
            lou.jiayouche = lou_date[3]
            lou.qianyinche = lou_date[4]
            lou.kecangmen = lou_date[5]
            lou.huocangmen = lou_date[6]
            lou.canche = lou_date[7]

    count_yindaoche = rg.yindaoche+lou.yindaoche
    count_feiji = rg.feiji+lou.feiji
    count_ketiche = rg.ketiche+lou.ketiche
    count_jiayouche = rg.jiayouche+lou.jiayouche
    count_qianyinche = rg.qianyinche+lou.qianyinche
    count_kecangmen = rg.kecangmen+lou.kecangmen
    count_huocangmen = rg.huocangmen+lou.huocangmen
    count_canche = rg.canche+lou.canche
try:
    if rg.yindaoche == 0 and ai.yindaoche == 0:
        jianchu_yindaoche = "N"
    else:
        jianchu_yindaoche = '{:.3f}'.format(
            rg.yindaoche/ai.yindaoche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.feiji == 0 and ai.feiji == 0:
        jianchu_feiji = "N"
    else:
        jianchu_feiji = '{:.3f}'.format(rg.feiji/ai.feiji*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.ketiche == 0 and ai.ketiche == 0:
        jianchu_ketiche = "N"
    else:
        jianchu_ketiche = '{:.3f}'.format(rg.ketiche/ai.ketiche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.jiayouche == 0 and ai.jiayouche == 0:
        jianchu_jiayouche = "N"
    else:
        jianchu_jiayouche = '{:.3f}'.format(rg.jiayouche/ai.jiayouche)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.qianyinche == 0 and ai.qianyinche == 0:
        jianchu_qianyinche = "N"
    else:
        jianchu_qianyinche = '{:.3f}'.format(
            rg.qianyinche/ai.qianyinche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.kecangmen == 0 and ai.kecangmen == 0:
        jianchu_kecangmen = "N"
    else:
        jianchu_kecangmen = '{:.3f}'.format(rg.kecangmen/ai.kecangmen)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.huocangmen == 0 and ai.huocangmen == 0:
        jianchu_huocangmen = "N"
    else:
        jianchu_huocangmen = '{:.3f}'.format(
            rg.huocangmen/ai.huocangmen*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.canche == 0 and ai.canche == 0:
        jianchu_canche = "N"
    else:
        jianchu_canche = '{:.3f}'.format(rg.canche/ai.canche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.yindaoche == 0 and count_yindaoche == 0:
        zhaohui_yindaoche = "N"
    else:
        zhaohui_yindaoche = '{:.3f}'.format(
            rg.yindaoche/count_yindaoche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.feiji == 0 and count_feiji == 0:
        zhaohui_feiji = "N"
    else:
        zhaohui_feiji = '{:.3f}'.format(rg.feiji/count_feiji*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.ketiche == 0 and count_ketiche == 0:
        zhaohui_ketiche = "N"
    else:
        zhaohui_ketiche = '{:.3f}'.format(rg.ketiche/count_ketiche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.jiayouche == 0 and count_jiayouche == 0:
        zhaohui_jiayouche = "N"
    else:
        zhaohui_jiayouche = '{:.3f}'.format(
            rg.jiayouche/count_jiayouche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.qianyinche == 0 and count_qianyinche == 0:
        zhaohui_qianyinche = "N"
    else:
        zhaohui_qianyinche = '{:.3f}'.format(
            rg.qianyinche/count_qianyinche*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.kecangmen == 0 and count_kecangmen == 0:
        zhaohui_kecangmen = "N"
    else:
        zhaohui_kecangmen = '{:.3f}'.format(
            rg.kecangmen/count_kecangmen*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.huocangmen == 0 and count_huocangmen == 0:
        zhaohui_huocangmen = "N"
    else:
        zhaohui_huocangmen = '{:.3f}'.format(
            rg.huocangmen/count_huocangmen*100)[:5]+"%"
except Exception as e:
    print(e)
try:
    if rg.canche == 0 and count_canche == 0:
        zhaohui_canche = "N"
    else:
        zhaohui_canche = '{:.3f}'.format(rg.canche/count_canche*100)[:5]+"%"
except Exception as e:
    print(e)


class Read_txt():
    def __init__(self):
        pass

    def print_all_count(self):
        a1 = "引导车:%d,飞机:%d,客梯车:%d,加油车:%d,牵引车:%d,客舱门:%d,货舱门:%d,餐车:%d" % (count_yindaoche, count_feiji,
                                                                        count_ketiche, count_jiayouche, count_qianyinche, count_kecangmen, count_huocangmen, count_canche)
        a2 = "ai引导车:%.f,ai飞机:%.f,ai客梯车:%.f,ai加油车:%.f,ai牵引车:%.f,ai客舱门:%.f,ai货舱门:%.f,ai餐车:%.f" % (
            ai.yindaoche, ai.feiji, ai.ketiche, ai.jiayouche, ai.qianyinche, ai.kecangmen, ai.huocangmen, ai.canche)
        a3 = "rg引导车:%.f,rg飞机:%.f,rg客梯车:%.f,rg加油车:%.f,rg牵引车:%.f,rg客舱门:%.f,rg货舱门:%.f,rg餐车:%.f" % (
            rg.yindaoche, rg.feiji, rg.ketiche, rg.jiayouche, rg.qianyinche, rg.kecangmen, rg.huocangmen, rg.canche)
        a4 = "lou引导车:%.f,lou飞机:%.f,lou客梯车:%.f,lou加油车:%.f,lou牵引车:%.f,lou客舱门:%.f,lou货舱门:%.f,lou餐车:%.f" % (
            lou.yindaoche, lou.feiji, lou.ketiche, lou.jiayouche, lou.qianyinche, lou.kecangmen, lou.huocangmen, lou.canche)
        return (a1, a2, a3, a4)

    def print_precision(self):
        b1 = "引导车:%s,飞机:%s,客梯车:%s,加油车:%s,牵引车:%s,客舱门:%s,货舱门:%s,餐车:%s" % (jianchu_yindaoche, jianchu_feiji,
                                                                        jianchu_ketiche, jianchu_jiayouche, jianchu_qianyinche, jianchu_kecangmen, jianchu_huocangmen, jianchu_canche)
        return b1

    def print_recall(self):
        c1 = "引导车:%s,飞机:%s,客梯车:%s,加油车:%s,牵引车:%s,客舱门:%s,货舱门:%s,餐车:%s" % (zhaohui_yindaoche, zhaohui_feiji,
                                                                        zhaohui_ketiche, zhaohui_jiayouche, zhaohui_qianyinche, zhaohui_kecangmen, zhaohui_huocangmen, zhaohui_canche)
        return c1

    def output_txt(self):
        (a1, a2, a3, a4) = self.print_all_count()
        b1 = self.print_precision()
        c1 = self.print_recall()
        date_txt = "各类总数:"+"\r\n"+a1+"\r\n"+"\r\n"+"各类识别总数:" + \
            "\r\n"+a2+"\r\n"+"\r\n"+a3+"\r\n"+"\r\n"+a4 + \
            "\r\n"+"\r\n"+"检出准确率:"+"\r\n"+b1+"\r\n"+"\r\n"+c1
        with open("./output.txt", "w") as f:
            f.write(date_txt)
