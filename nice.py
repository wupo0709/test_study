import os
from airplane_pro import AI, RG, LOU

jianchu_yindaoche = zhaohui_yindaoche = 0
jianchu_ketiche = zhaohui_ketiche = 0
jianchu_feiji = zhaohui_feiji = 0
jianchu_jiayouche = zhaohui_jiayouche = 0
jianchu_qianyinche = zhaohui_qianyinche = 0
jianchu_kecangmen = zhaohui_kecangmen = 0
jianchu_huocangmen = zhaohui_huocangmen = 0
jianchu_canche = zhaohui_canche = 0


def read_txt(path_read, count):
    global jianchu_yindaoche
    global jianchu_feiji
    global jianchu_ketiche
    global jianchu_jiayouche
    global jianchu_qianyinche
    global jianchu_kecangmen
    global jianchu_huocangmen
    global jianchu_canche
    global zhaohui_yindaoche
    global zhaohui_ketiche
    global zhaohui_feiji
    global zhaohui_jiayouche
    global zhaohui_qianyinche
    global zhaohui_kecangmen
    global zhaohui_huocangmen
    global zhaohui_canche
    ai = AI()
    rg = RG()
    lou = LOU()
    for root, dirs, files in os.walk(path_read, topdown=False):
        for name in files:
            if name == "result.txt":
                count += 1
                with open(os.path.join(root, name), "r", encoding="gbk") as f:
                    content = f.read()
                try:
                   # print(os.path.join(root,name),content.split()[23],content.split()[9],content.split()[37])
                    ai.yindaoche += float(content.split()[1])
                    ai.feiji += float(content.split()[3])
                    ai.ketiche += float(content.split()[5])
                    ai.jiayouche += float(content.split()[7])
                    ai.qianyinche += float(content.split()[9])
                    ai.kecangmen += float(content.split()[11])
                    ai.huocangmen += float(content.split()[13])
                    ai.canche += float(content.split()[15])

                    rg.yindaoche += float(content.split()[17])
                    rg.feiji += float(content.split()[19])
                    rg.ketiche += float(content.split()[21])
                    rg.jiayouche += float(content.split()[23])
                    rg.qianyinche += float(content.split()[25])
                    rg.kecangmen += float(content.split()[27])
                    rg.huocangmen += float(content.split()[29])
                    rg.canche += float(content.split()[31])

                    lou.yindaoche += float(content.split()[33])
                    lou.feiji += float(content.split()[35])
                    lou.ketiche += float(content.split()[37])
                    lou.jiayouche += float(content.split()[39])
                    lou.qianyinche += float(content.split()[41])
                    lou.kecangmen += float(content.split()[43])
                    lou.huocangmen += float(content.split()[45])
                    lou.canche += float(content.split()[47])
                except:
                    print("第%d个文件" % count, os.path.join(root, name))
                # print(os.path.join(root,name),rg.qianyinche,ai.qianyinche,lou.qianyinche)
    # print("各类总数据:")
    # print("引导车:%d,飞机:%d,客梯车:%d,加油车:%d,牵引车:%d,客舱门:%d,货舱门:%d" % (count_yindaoche, count_feiji,count_ketiche, count_jiayouche, count_qianyinche, count_kecangmen,count_huocangmen))
    # print("ai引导车:%.f,ai飞机:%.f,ai客梯车:%.f,ai加油车:%.f,ai牵引车:%.f,ai客舱门:%.f,ai货舱门:%.f," % (
    #     ai.yindaoche, ai.feiji, ai.ketiche, ai.jiayouche, ai.qianyinche, ai.kecangmen, ai.huocangmen))
    # print("rg引导车:%.f,rg飞机:%.f,rg客梯车:%.f,rg加油车:%.f,rg牵引车:%.f,rg客舱门:%.f,rg货舱门:%.f," % (rg.yindaoche, rg.feiji, rg.ketiche, rg.jiayouche,rg.qianyinche, rg.kecangmen, rg.huocangmen))
    # print("loug引导车:%.f,lou飞机:%.f,lou客梯车:%.f,lou加油车:%.f,lourg牵引车:%.f,lou客舱门:%.f,lou货舱门:%.f," % (lou.yindaoche, lou.feiji, lou.ketiche, lou.jiayouche,lou.qianyinche, lou.kecangmen, lou.huocangmen))
    count_yindaoche = rg.yindaoche+lou.yindaoche
    count_feiji = rg.feiji+lou.feiji
    count_ketiche = rg.ketiche+lou.ketiche
    count_jiayouche = rg.jiayouche+lou.jiayouche
    count_qianyinche = rg.qianyinche+lou.qianyinche
    count_kecangmen = rg.kecangmen+lou.kecangmen
    count_huocangmen = rg.huocangmen+lou.huocangmen
    count_canche = rg.canche+lou.canche

    print("各类总数:")
    print("引导车:%d,飞机:%d,客梯车:%d,加油车:%d,牵引车:%d,客舱门:%d,货舱门:%d,餐车:%d" % (count_yindaoche, count_feiji,
                                                                     count_ketiche, count_jiayouche, count_qianyinche, count_kecangmen, count_huocangmen, count_canche))
    print("")
    print("各类识别总数：")
    print("ai引导车:%.f,ai飞机:%.f,ai客梯车:%.f,ai加油车:%.f,ai牵引车:%.f,ai客舱门:%.f,ai货舱门:%.f,ai餐车:%.f" % (
        ai.yindaoche, ai.feiji, ai.ketiche, ai.jiayouche, ai.qianyinche, ai.kecangmen, ai.huocangmen, ai.canche))
    print("rg引导车:%.f,rg飞机:%.f,rg客梯车:%.f,rg加油车:%.f,rg牵引车:%.f,rg客舱门:%.f,rg货舱门:%.f,rg餐车:%.f" % (
        rg.yindaoche, rg.feiji, rg.ketiche, rg.jiayouche, rg.qianyinche, rg.kecangmen, rg.huocangmen, rg.canche))
    print("lou引导车:%.f,lou飞机:%.f,lou客梯车:%.f,lou加油车:%.f,lou牵引车:%.f,lou客舱门:%.f,lou货舱门:%.f,lou餐车:%.f" % (
        lou.yindaoche, lou.feiji, lou.ketiche, lou.jiayouche, lou.qianyinche, lou.kecangmen, lou.huocangmen, lou.canche))
    print("")

    try:
        jianchu_yindaoche = rg.yindaoche/ai.yindaoche
    except:
        pass
    try:
        jianchu_feiji = rg.feiji/ai.feiji
    except:
        pass
    try:
        jianchu_ketiche = rg.ketiche/ai.ketiche
    except:
        pass
    try:
        jianchu_jiayouche = rg.jiayouche/ai.jiayouche
    except:
        pass
    try:
        jianchu_qianyinche = rg.qianyinche/ai.qianyinche
    except:
        pass
    try:
        jianchu_kecangmen = rg.kecangmen/ai.kecangmen
    except:
        pass
    try:
        jianchu_huocangmen = rg.huocangmen/ai.huocangmen
    except:
        pass
    try:
        jianchu_canche = rg.canche/ai.canche
    except:
        pass
    try:
        zhaohui_yindaoche = rg.yindaoche/count_yindaoche
    except:
        pass
    try:
        zhaohui_feiji = rg.feiji/count_feiji
    except:
        pass
    try:
        zhaohui_ketiche = rg.ketiche/count_ketiche
    except:
        pass
    try:
        zhaohui_jiayouche = rg.jiayouche/count_jiayouche
    except:
        pass
    try:
        zhaohui_qianyinche = rg.qianyinche/count_qianyinche
    except:
        pass
    try:
        zhaohui_kecangmen = rg.kecangmen/count_kecangmen
    except:
        pass
    try:
        zhaohui_huocangmen = rg.huocangmen/count_huocangmen
    except:
        pass
    try:
        zhaohui_canche = rg.canche/count_canche
    except:
        pass

    return (count, count_yindaoche, count_feiji, count_ketiche, count_jiayouche, count_qianyinche, count_kecangmen, count_huocangmen, count_canche, jianchu_yindaoche, jianchu_feiji, jianchu_ketiche, jianchu_jiayouche, jianchu_qianyinche, jianchu_kecangmen, jianchu_huocangmen, jianchu_canche, zhaohui_yindaoche, zhaohui_feiji, zhaohui_ketiche, zhaohui_jiayouche, zhaohui_qianyinche, zhaohui_kecangmen, zhaohui_huocangmen, zhaohui_canche)


def main():
    count = 0
    path_read = "."
    (count, count_yindaoche, count_feiji, count_ketiche, count_jiayouche, count_qianyinche, count_kecangmen, count_huocangmen, count_canche, jianchu_yindaoche, jianchu_feiji, jianchu_ketiche, jianchu_jiayouche, jianchu_qianyinche, jianchu_kecangmen, jianchu_huocangmen, jianchu_canche, zhaohui_yindaoche,
     zhaohui_feiji, zhaohui_ketiche, zhaohui_jiayouche, zhaohui_qianyinche, zhaohui_kecangmen, zhaohui_huocangmen, zhaohui_canche) = read_txt(path_read, count)
    print("检出准确率：")
    print("引导车:%.5f,飞机:%.5f,客梯车:%.5f,加油车:%.5f,牵引车:%.5f,客舱门:%.5f,货舱门:%.5f,餐车:%.5f" % (jianchu_yindaoche, jianchu_feiji,
                                                                                     jianchu_ketiche, jianchu_jiayouche, jianchu_qianyinche, jianchu_kecangmen, jianchu_huocangmen, jianchu_canche))
    print("")
    print("召回率:")
    print("引导车:%.5f,飞机:%.5f,客梯车:%.5f,加油车:%.5f,牵引车:%.5f,客舱门:%.5f,货舱门:%.5f,餐车:%.5f" % (zhaohui_yindaoche, zhaohui_feiji,
                                                                                     zhaohui_ketiche, zhaohui_jiayouche, zhaohui_qianyinche, zhaohui_kecangmen, zhaohui_huocangmen, zhaohui_canche))


if __name__ == "__main__":
    main()
