import os


def write_time(file_list, list_all):
    for file in file_list:
        enter = input("视频%s,是否跳过y/n：" % file)
        while True:
            if enter == "y":
                print("%s此视频已跳过" % file)
                break
            elif enter == "n":
                list_all.append("name:"+file+"\n")
                start_time = input("输入开始截取时间(格式应为00:00:00)：")
                list_all.append(start_time+" ")
                end_time = input("输入结束截取时间(格式应为00:00:00)：")
                list_all.append(end_time+"\n")
                break
            else:
                enter = input("视频%s,是否跳过y/n：" % file)
    return list_all


def write_txt(list_all, txt_name):
    with open(txt_name, "w") as f:
        f.writelines(list_all)
    print("写入完毕")


def main():
    txt_name = input("请输入txt文件名字：")
    list_all = ['output_name:xxx.264']
    file_list = os.listdir()
    list_all = write_time(file_list, list_all)
    write_txt(list_all, txt_name)


if __name__ == "__main__":
    main()
