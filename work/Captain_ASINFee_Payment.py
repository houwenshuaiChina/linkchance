import zipfile
# -*- coding:utf-8 -*-
import os
import pandas as pd


def rename_csv( data_dir_args ):
    # data_dir = '.\data'
    data_dir_list = os.listdir(data_dir_args)  # 列出文件夹下所有的目录与文件
    rename_count = 0  # 重命名的文件数量

    for i in range(0, len(data_dir_list)):
        csv_dir = os.path.join(data_dir, data_dir_list[i])
        if os.path.isdir(csv_dir):
            csv_file_list = os.listdir(csv_dir)  # 列出文件夹下所有的目录与文件
            for csvname in  csv_file_list:
                csvpath = os.path.join(csv_dir, csv_file_list[0])
                if os.path.isfile(csvpath):
                    # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
                    os.rename(csvpath, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
                    rename_count += 1
    print('csv文件：总共重命名了 ' + str(rename_count) + ' 个文件！')


# def rename_csv( data_dir_args ):
#     # data_dir = '.\data'
#     data_dir_list = os.listdir(data_dir_args)  # 列出文件夹下所有的目录与文件
#     rename_count = 0  # 重命名的文件数量
#
#     for i in range(0, len(data_dir_list)):
#         csv_dir = os.path.join(data_dir, data_dir_list[i])
#         print (csv_dir)
#         if os.path.isdir(csv_dir):
#             csv_file_list = os.listdir(csv_dir)  # 列出文件夹下所有的目录与文件
#             csv_file_len = len(csv_file_list)
#             if csv_file_len = 0 ：
#                 #for j in range(0,len(csv_file_list)):  # in csv_file_list:
#                 csvpath = os.path.join(csv_dir, csv_file_list[0])
#                 if os.path.isfile(csvpath):
#                     # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
#                     os.rename(csvpath, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
#                     rename_count += 1
#             else:
#                 for j in range(0, len(csv_file_list)):  # in csv_file_list:
#                     csvpath = os.path.join(csv_dir, csv_file_list[j])
#                     if os.path.isfile(csvpath):
#                         # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
#                         os.rename(csvpath, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
#                         rename_count += 1
#     # else:
#             #     rename_count += 1
#     print(rename_count)

def open_csv(data_dir_args):
    try:
        open_dir_list = os.listdir(data_dir_args)  # 列出文件夹下所有的目录与文件
        # print(data_dir_args)
        print(open_dir_list)
        for openfile in open_dir_list:
            csv_file = os.path.join(data_dir_args,openfile)
            if os.path.isfile(openfile):
        #     # df_dict = pd.read_csv(csv_file,sep=',',encoding='utf-8')
                print(csv_file)
            # print(df_dict)
        # df_dict_total = pd.DataFrame()
        # # print（df_dict_total)
        # for csvname in csv_file_list:
        #     df_dict = pd.read_csv(csv_file, sep=',', encoding="utf-8")
        #     df_dict['StroeName']=left(csvname)
        #     df_csv_total.append(df_dict)
        # # df_dict = pd.read_csv(csv_file, sep='\t', encoding="utf-8")
        # return df_dict_total
    except:
        print("open csv file failed!")


if __name__ == "__main__":

    data_dir = '.\data'
    rename_csv(data_dir)
    # open_csv(data_dir)
    # csv_file = '.\data\OMB1_EU_UK-Payment_2021-04-01_2021-04-05.csv'
    # df_dict = pd.read_csv(csv_file, sep=',', encoding="utf-8")
    # print(type(df_dict))

    # data_dir_list = os.listdir(data_dir)  # 列出文件夹下所有的目录与文件
    #
    # for i in range(0, len(data_dir_list)):
    #     count =1
    #     csv_dir = os.path.join(data_dir, data_dir_list[i])
    #     print (csv_dir)
    #     if os.path.isdir(csv_dir):
    #         csv_file_list = os.listdir(csv_dir)  # 列出文件夹下所有的目录与文件
    #         for csvname in csv_file_list:
    #             csvpath = os.path.join(csv_dir,csvname)
    #             if os.path.isfile(csvpath):
    #                 # os.rename(csvpath, os.path.join(csv_dir, data_dir_list[i]) + '.csv')  # 在原来目录中重命名csv文件
    #                 os.rename(csvpath, csv_dir + '.csv')  # 重命名csv文件并移动到./data目录中
    #                 count += 1
