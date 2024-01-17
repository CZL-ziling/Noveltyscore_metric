# '''Connect the table'''
# import pandas as pd
#
# df1=pd.read_excel("balance_ratio.xlsx")
# df2=pd.read_excel("2023.1.4.xlsx")
# print(df1)
# print(df2)
# df3=pd.merge(df2,df1,on="Id",how='left')
# df3.to_excel("2024.1.8.xlsx")
#
#
#
#
#
# '''Analyze gender team composition图1'''
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df=pd.read_excel("性别聚类2.xlsx")
#
# df_id=df[df.columns[0]].tolist()
# df_name=df[df.columns[1]].tolist()
# df_year=df[df.columns[2]].tolist()
# df_sex=df[df.columns[3]].tolist()
#
#
# df2=pd.read_excel("性别识别.xlsx")
# df2_name=df2[df2.columns[1]].tolist()
# df2_sex=df2[df2.columns[2]].tolist()
#
# name_sex={}
# for i,name in enumerate(df2_name):
#     name_sex[name]=df2_sex[i]
#
# years=[]
# names=[]
# result={}
# for i in df_id:
#     year=df_year[df_id.index(i)]
#     if year in result:
#         strings=df_name[df_id.index(i)]
#         string_list = strings.split(',')
#
#         result[year].append(string_list)
#     else:
#         strings = df_name[df_id.index(i)]
#         string_list = strings.split(',')
#         result[year]=[string_list]
#
# ratios={}
# new_lst=[]
# sexs=[]
# for year in result:
#     names=result[year]
#     for sublist in names:
#         for elem in sublist:
#             new_lst.append(elem)
#             names=list(set(new_lst))
#     for i in names:
#         sexs.append(name_sex[i])
#     count_f = sexs.count('F')
#     ratio=count_f/len(sexs)
#     ratios[year]=ratio
#
# years = list(ratios.keys())
# values = list(ratios.values())
#
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.plot(years, values, color='grey', linewidth=2)
# ax.set_ylabel('Percentage Of Female Scientists')
# plt.show()
#
# '''yearly avg team size'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df=pd.read_excel("性别聚类2.xlsx")
# yearly_avg_ratios = df.groupby('year')['members'].mean().reset_index()

# bar_width = 0.6
# bar_spacing = 0.3

# fig, ax = plt.subplots(figsize=(6, 6))
# ax.plot(yearly_avg_ratios['year'], yearly_avg_ratios['members'],color='grey', linewidth=2)
# ax.set_ylabel('Yearly Avg.Team Size')
#
# plt.show()





'''Different categories of teams change'''
# import pandas as pd
# import  matplotlib.pyplot as plt
#
# df=pd.read_excel("性别聚类2.xlsx")
# yearly_sex_counts = df.groupby('year')['sex'].value_counts().unstack()
# yearly_total_counts = df.groupby('year')['sex'].count()
# yearly_ratios = yearly_sex_counts.div(yearly_total_counts, axis=0)
#
# fig, ax = plt.subplots(figsize=(6, 6)) # 设置图形的长宽为10x6英寸
# yearly_ratios.plot(ax=ax, linewidth=4) # 设置线条宽度为2
#
# # 设置颜色
# # colors = ['red', 'green', 'yellow', 'blue'] # 为每个类别指定颜色
# # for i, category in enumerate(yearly_ratios.columns):
# #     yearly_ratios[category].plot(ax=ax, linewidth=2, color=colors[i % len(colors)]) # 根据类别设置颜色
# ax.set_ylabel('Team Gender Changes Over Time')
#
# plt.show()





'''Percentage of teams in different categories图4'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel("性别聚类2.xlsx")
# avg_ration = df.groupby(["year","sex"])["members"].mean().unstack()
#
# print(avg_ration)
# fig, ax = plt.subplots(figsize=(6, 6))
#
# for label in avg_ration.columns:
#     ax.plot(avg_ration.index, avg_ration[label], label=f"{label}",linewidth=4)
#
# ax.set_ylabel('Average Members by Year and Gender')
# ax.legend()
# plt.show()

# a = ["1979", "1989", "1999", "2009","2019"]
#
# b_only_M = [0.87, 0.59, 0.661, 0.551,0.585]
# b_only_F= [0.13, 0.225, 0.104,0.073,0.032 ]
# b_mixed_F= [0, 0.125, 0.113,0.154, 0.179]
# b_mixed_M=[0,0.06,0.122,0.222,0.204]
#
# width_bar = 0.2
#
# x_1 = list(range(len(a)))
# x_2 = [i + width_bar for i in x_1]
# x_3 = [i + width_bar * 2 for i in x_1]
# x_4 = [i + width_bar * 3 for i in x_1]
#
# plt.figure(figsize=(10, 5), dpi=80)
#
# plt.xticks(x_1, a)
#
# c_1 = plt.bar(range(len(a)), b_mixed_F, width=width_bar)
# c_2 = plt.bar(x_2, b_mixed_M, width=width_bar)
# c_3 = plt.bar(x_3, b_only_F, width=width_bar)
# c_4 = plt.bar(x_4, b_only_M, width=width_bar)
#
# plt.ylabel("Percentage of teams in different categories")
#
# plt.legend()
# plt.show()





'''简简单单占比图'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel("性别聚类2.xlsx")
#
# gender_data = df["sex"]
#
# label_counts = gender_data.value_counts()
#
# fig, ax = plt.subplots(figsize=(5, 3))
#
# colors = ['red', 'orange', 'blue','green'] # 自定义每个标签的颜色
# ax.barh(label_counts.index, label_counts.values, color=colors)
# ax.set_ylabel('Percentage of Composition of Different Genders')
#
# plt.show()





'''多标签女性占比图'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel("性别聚类2.xlsx")
#
#
# avg_ration = df.groupby(["year","sex"])["ratio"].mean().unstack()
#
# print(avg_ration)
# fig, ax = plt.subplots(figsize=(6, 6))
#
# for label in avg_ration.columns:
#     ax.plot(avg_ration.index, avg_ration[label], label=f"{label}",linewidth=4)
#
# ax.set_ylabel('Average Ration by Year and Gender')
# ax.legend()
# plt.show()
#
# a = ["1979", "1989", "1999", "2009","2019"]
#
# b_only_M = [0, 0, 0.0125,0.021171,0.066711]
# b_only_F= [1, 1, 1,0.963596,0.836487 ]
# b_mixed_F= [0, 0.5, 0.530769,0.434687, 0.427277]
# b_mixed_M=[0,0.5833,0.440476,0.450742,0.400260]
#
# width_bar = 0.2
#
# x_1 = list(range(len(a)))
# x_2 = [i + width_bar for i in x_1]
# x_3 = [i + width_bar * 2 for i in x_1]
# x_4 = [i + width_bar * 3 for i in x_1]
#
# plt.figure(figsize=(10, 5), dpi=80)
#
# plt.xticks(x_1, a)
#
# c_1 = plt.bar(range(len(a)), b_mixed_F, width=width_bar)
# c_2 = plt.bar(x_2, b_mixed_M, width=width_bar)
# c_3 = plt.bar(x_3, b_only_F, width=width_bar)
# c_4 = plt.bar(x_4, b_only_M, width=width_bar)
#
# plt.ylabel("Percentage of women in different categories")
#
# plt.legend()
# plt.show()




'''性别与创新性分析'''
'''1.控制团队规模'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_excel("genderswithnovelty.xlsx")
#
# # filtered_df = df[df["members"] >= 2]
# avg_ration = df.groupby(["members", "sex"])["score2"].mean().unstack()
#
# fig, ax = plt.subplots(figsize=(6, 3))
#
# bar_width = 0.2
# opacity = 0.8
# index = np.arange(len(avg_ration))
#
# # 绘制每个类别的条形图
# for i, label in enumerate(avg_ration.columns):
#     ax.bar(index + bar_width * i, avg_ration[label], bar_width,
#            alpha=opacity)
#
# ax.set_ylabel('Average innovation score')
#
# ax.set_xticks(index + (bar_width * (len(avg_ration.columns) - 1)) / 2)
# ax.set_xticklabels(avg_ration.index)
# ax.legend()
#
# plt.tight_layout()
# plt.show()




'''2.控制年份'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_excel("genderswithnovelty.xlsx")
#
# filtered_df = df[df["year"] >= 2000]
# avg_ration = filtered_df.groupby(["year", "sex"])["score2"].mean().unstack()
#
#
#
# print(avg_ration)
# fig, ax = plt.subplots(figsize=(6, 3))
#
# for label in avg_ration.columns:
#     ax.plot(avg_ration.index, avg_ration[label], label=f"{label}",linewidth=2)
#
# ax.set_ylabel('Average Ration by Year and Gender')
# ax.legend()
# plt.show()





'''性别与创新性类型'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_excel("genderswithnovelty.xlsx")
#
# # filtered_df = df[df["metric3"]>=1]
# avg_ration = df.groupby(["sex"])["tool3"].count()
# print(avg_ration)
# #
#
# a=["method","dataset","tool","metric"]
# b_only_M=[792,890,936,1007]
# b_only_F=[82,76,67,56]
# b_mixed_M=[316,295,340,334]
# b_mixed_F=[310,243,273,261]

# c_only_M=[1500,8835]
# c_only_F=[1505,785]
# c_mixed_M=[1617,2912]
# c_mixed_F=[1659,2520]
#
# d_only_M=[0.528,0.591,0.579,0.607]
# d_only_F=[0.055,0.05,0.041,0.034]
# d_mixed_M=[0.211,0.196,0.21,0.201]
# d_mixed_F=[0.206,0.163,0.17,0.158]
#
# b_only_M=[792,890,936,1007]
# b_only_F=[82,76,67,56]
# b_mixed_M=[316,295,340,334]
# b_mixed_F=[310,243,273,261]
#
# e_only_M=[]
# for i in b_only_M:
#     d=i/8835
#     e_only_M.append(d)
#
# e_only_F=[]
# for i in b_only_F:
#     d=i/785
#     e_only_F.append(d)
#
# e_mixed_M=[]
# for i in b_mixed_M:
#     d=i/2912
#     e_mixed_M.append(d)
#
# e_mixed_F=[]
# for i in b_mixed_F:
#     d=i/2520
#     e_mixed_F.append(d)
# print(e_only_M)
# width_bar = 0.2

# x_1 = list(range(len(a)))
# x_2 = [i + width_bar for i in x_1]
# x_3 = [i + width_bar * 2 for i in x_1]
# x_4 = [i + width_bar * 3 for i in x_1]
#
# plt.figure(figsize=(10, 5), dpi=80)
#
# plt.xticks(x_2, a)
#
# c_1 = plt.bar(range(len(a)), d_mixed_F, width=width_bar)
# c_2 = plt.bar(x_2, d_mixed_M, width=width_bar)
# c_3 = plt.bar(x_3, d_only_F, width=width_bar)
# c_4 = plt.bar(x_4, d_only_M, width=width_bar)
#
# plt.ylabel("Percentage of teams in different categories")
#
# plt.legend()
# plt.show()

# x_1 = list(range(len(a)))
# x_2 = [i + width_bar for i in x_1]
# x_3 = [i + width_bar * 2 for i in x_1]
# x_4 = [i + width_bar * 3 for i in x_1]
#
# plt.figure(figsize=(10, 5), dpi=80)
#
# plt.xticks(x_2, a)
#
# c_1 = plt.bar(range(len(a)), e_mixed_F, width=width_bar)
# c_2 = plt.bar(x_2, e_mixed_M, width=width_bar)
# c_3 = plt.bar(x_3, e_only_F, width=width_bar)
# c_4 = plt.bar(x_4, e_only_M, width=width_bar)
#
# plt.ylabel("Percentage of teams in different categories")
#
# plt.legend()
# plt.show()



'''性别与影响力'''
'''1.控制团队规模'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_excel("genderswithimpact.xlsx")
#
#
# avg_ration = df.groupby(["member", "sex"])["logcited"].mean().unstack()
#
# fig, ax = plt.subplots(figsize=(6, 3))
#
# bar_width = 0.2
# opacity = 0.8
# index = np.arange(len(avg_ration))
#
# # 绘制每个类别的条形图
# for i, label in enumerate(avg_ration.columns):
#     ax.bar(index + bar_width * i, avg_ration[label], bar_width,
#            alpha=opacity)
#
# ax.set_ylabel('Average innovation score')
#
# ax.set_xticks(index + (bar_width * (len(avg_ration.columns) - 1)) / 2)
# ax.set_xticklabels(avg_ration.index)
# ax.legend()
#
# plt.tight_layout()
# plt.show()
#
#
#
#
#
#
# '''2.控制年份'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_excel("genderswithimpact.xlsx")
#
# filtered_df = df[df["year"] >= 1999]
# avg_ration = filtered_df.groupby(["year", "sex"])["logcited"].mean().unstack()
#
#
#
# print(avg_ration)
# fig, ax = plt.subplots(figsize=(6, 3))
#
# for label in avg_ration.columns:
#     ax.plot(avg_ration.index, avg_ration[label], label=f"{label}",linewidth=2)
# plt.xticks(np.arange(min(avg_ration.index), max(avg_ration.index)+1, 5))
#
# ax.set_ylabel('Average Ration by Year and Gender')
# ax.legend()
# plt.show()





'''给工业界和学术界打标签'''
# import pandas as pd
#
#
# df2 = pd.read_excel("国际合作论文id.xlsx",sheet_name="Sheet2")
# df4 = pd.read_excel("国际合作论文id.xlsx",sheet_name="工业界")
# ids=[]
# qss=[]
# names=[]
# countrys=[]
# scores=[]
# types=[]
# for i in range(0, len(df2)):
#     id = df2.iloc[i]['Id']
#     aff = df2.iloc[i]['affiliation']
#     country=df2.iloc[i]['Country']
#     name = df2.iloc[i]['Author_id']
#     if aff in df4['Affiliation'].values:
#             ids.append(id)
#             qss.append(aff)
#             countrys.append(country)
#             names.append(name)
#             types.append("Company")
#     else:
#         ids.append(id)
#         qss.append(aff)
#         countrys.append(country)
#         names.append(name)
#         types.append("Education")
# result_excel = pd.DataFrame()
#
#
# result_excel["Id"] = ids
# result_excel["Author_id"] = names
# result_excel["Affiliation"] = qss
#
# result_excel["Country"] = countrys
# result_excel["Type"] = types
# # result_excel.to_excel("QS7.xlsx",sheet_name="Sheet5")
# # with pd.ExcelWriter("国际合作论文id.xlsx", mode='a', engine='openpyxl') as writer:
# #     result_excel.to_excel(writer, sheet_name="学术界")
# result_excel.to_excel("555.xlsx")

'''中间插着这个刚开始从附属地区分是公司还是学校的'''
# ids=[]
# qss=[]
# names=[]
# country=[]
# for i in range(0, len(df2)):
#     id = df2.iloc[i]['Paper_id']
#     qsname = df2.iloc[i]['affiliation']
#     guojia=df2.iloc[i]['Country']
#     name=df2.iloc[i]['Author_id']
#     if 'University' in qsname or 'College'  in qsname or 'university' in qsname or 'college' in qsname:
#         ids.append(id)
#         qss.append(qsname)
#         country.append(guojia)
#         names.append(name)
# print(len(ids))
#
# result_excel = pd.DataFrame()
#
# result_excel["paper_id"] = ids
#
# result_excel["affiliation"] = qss
# result_excel["country"] = country
# result_excel["name"] = names
# result_excel.to_excel("QS7.xlsx")



'''连接两表'''
# import pandas as pd
#
# df1=pd.read_excel("222.xlsx")
# df2=pd.read_excel("444.xlsx")
#
# df3=pd.merge(df1,df2,on="Id",how='left')
# df3.to_excel("2222.xlsx")




# import pandas as pd
#
# df2=pd.read_excel("222.xlsx",sheet_name="Sheet1")
#
# df1=pd.read_excel("作者信息.xlsx",sheet_name="Sheet2")
# ids=df2["Id"].tolist()
# print(len(ids))
# types=[]
# idss=[]
# for i in range(0,len(df1)):
#     id=df1.iloc[i]['Id']
#     type=df1.iloc[i]['Type11']
#     if id in ids:
#         types.append(type)
#         idss.append(id)
#
# print(len(idss))
# print(len(types))
# df3=pd.DataFrame()
# df3["Type"]=types
# df3["id"]=idss
#
# df3.to_excel("888.xlsx")
# #

'''上下合并表格'''
# import pandas as pd
#
# df1=pd.read_excel("quchong.xlsx",sheet_name="Sheet1")
# df2=pd.read_excel("666.xlsx")
# # df_concatenated = pd.concat([df1, df2], ignore_index=True)
#
# #
'''根据id聚类'''
# df3=pd.merge(df2,df1,on="Id",how='left')
# df3.to_excel("777.xlsx")
# grouped = df2.groupby('Id')['Country'].apply(list).reset_index()
# grouped.to_excel('888.xlsx', index=False)


'''分id，将纯的和混合的区分开'''
# import pandas as pd
#
# df=pd.read_excel("国际合作论文id.xlsx",sheet_name="Sheet8")
# mixed=[]
# only_e=[]
# only_c=[]
# for i in range(0, len(df)):
#     qsname = df.iloc[i]['Type']
#     id = df.iloc[i]['Id']
#     if 'Education' in qsname and 'Company' in qsname:
#         mixed.append(id)
#     elif  'Education' not in qsname:
#         only_c.append(id)
#     else:
#         only_e.append(id)
# result_excel1=pd.DataFrame()
# result_excel1["id"]=mixed
# result_excel2=pd.DataFrame()
# result_excel2["id"]=only_e
# result_excel3=pd.DataFrame()
# result_excel3["id"]=only_c
# with pd.ExcelWriter("111.xlsx", mode='a', engine='openpyxl') as writer:
#     result_excel1.to_excel(writer, sheet_name="sheet1")
#     result_excel2.to_excel(writer, sheet_name="sheet2")
#     result_excel3.to_excel(writer, sheet_name="sheet3")





'''打标签'''
# import pandas as pd
#
#
# df_111 = pd.read_excel('111.xlsx',sheet_name="sheet1")
# df_222 = pd.read_excel('111.xlsx',sheet_name="sheet2")
# df_333 = pd.read_excel('111.xlsx',sheet_name="sheet3")
# international_id_table=pd.read_excel("国际合作论文id.xlsx",sheet_name="Sheet8")
# international_id_table_with_mixed = international_id_table.copy()
# international_id_table_with_mixed['Mixed'] = ''
#
# for index, row in international_id_table_with_mixed.iterrows():
#     id_value = row['Id']
#
#     if not df_111[df_111['Id'] == id_value].empty:
#
#         international_id_table_with_mixed.at[index, 'Mixed'] = 'mixed'
#     if not df_222[df_222['Id'] == id_value].empty:
#
#         international_id_table_with_mixed.at[index,'Mixed'] = 'only_e'
#     if not df_333[df_333['Id'] == id_value].empty:
#
#         international_id_table_with_mixed.at[index, 'Mixed'] = 'only_c'
#
#
# international_id_table_with_mixed.to_excel("222.xlsx")





import pandas as pd

# df=pd.read_excel("222.xlsx",sheet_name="Sheet1")
# ratios=[]
# idss=[]
# for i in range(0,len(df)):
#     aff=df.iloc[i]["Type"]
#     ids=df.iloc[i]["Id"]
#     idss.append(ids)
#     # print(type(ids))
#     aff=eval(aff)
#     company=0
#     for i in aff:
#         if i =='Company':
#             company=company+1
#     ratio=company/len(aff)
#     ratios.append(ratio)
#
# reslut_excel=pd.DataFrame()
# reslut_excel['Id']=idss
# reslut_excel['Ratio']=ratios
# reslut_excel.to_excel("ratio.xlsx",index=False)



import pandas as pd
#
# df1 = pd.read_excel("国际合作论文id.xlsx", sheet_name="工业界")
# com = df1["Affiliation"].tolist()
# df2 = pd.read_excel("作者信息.xlsx", sheet_name="Sheet2")
# mixed = []
#
# for i in range(0, len(df2)):
#     aff = df2.iloc[i]["Affiliation"]
#     if aff in com:
#         mixed.append("Company")
#     else:
#         mixed.append("Education")
#
# result = pd.DataFrame(mixed)
# result.to_excel("666.xlsx")



'''找到重复的id'''
import pandas as pd

# df = pd.read_excel("888.xlsx", sheet_name="Sheet1")
# duplicates = df[df.duplicated(subset='Id')]
# result_excel=pd.DataFrame()
# result_excel['Id']=duplicates['Id']
# result_excel.to_excel("999.xlsx")


'''根据ration判断重复id的类型'''
# import pandas as pd
#
# df1 = pd.read_excel("ratio.xlsx")
# df2 = pd.read_excel("999.xlsx")
# types = []
#
# for i in range(len(df2)):
#     if df2.iloc[i]["Id"] in df1["Id"].tolist():
#         m = df1[df1["Id"] == df2.iloc[i]["Id"]].index[0]
#         if df1.iloc[m]["Ratio"] > 0.5:
#             types.append("Company")
#         else:
#             types.append("Education")
#
# result_excel = pd.DataFrame()
# result_excel['Id'] = df2['Id']
# result_excel['Type'] = types
# result_excel.to_excel("333.xlsx")

'''整合代码，将所有id数据的给匹配类型'''

# import pandas as pd
# df2 = pd.read_excel("333.xlsx")
# df1 = pd.read_excel("222.xlsx")
# type=[]
# for i in range(len(df1)):
#     id=df1.iloc[i]["Id"]
#     mixed=df1.iloc[i]["Mixed2"]
#     ratio=df1.iloc[i]["Ratio"]
#     if mixed=="mixed":
#         if id in df2["Id"].tolist():
#             m = df1[id].index[0]
#             type.append(df1.iloc[m]["Type"])
#     if mixed=="only":
#         if ratio == 0:
#             type.append("Education")
#         if ratio==1:
#             type.append("Company")
# result_excel = pd.DataFrame()
# result_excel['Id'] = id
# result_excel['Type'] = type
# result_excel.to_excel("444.xlsx")



'''ctm的一开始思路不清楚'''
# import pandas as pd
#
# df1 = pd.read_excel("作者信息.xlsx", sheet_name="Sheet2")
# df2 = pd.read_excel("333.xlsx")
#
# types = []
# for i in range(len(df1)):
#     id_value = df1.iloc[i]["Id"]
#     tt = df1.iloc[i]["Type"]
#
#     if id_value in df2["Id"].tolist():
#         m = df2[df2["Id"] == id_value].index[0]
#         type_value = df2.iloc[m]["Type"]
#         types.append(type_value)
#     else:
#         types.append(tt)
#
# result_excel = pd.DataFrame()
# result_excel['Id'] = df1['Id']
# result_excel['Type'] = types
# result_excel.to_excel("444.xlsx")


# 控制变量的获取#



# import pandas as pd
#
# df = pd.read_excel("三大会议机构信息.xlsx")
# paper_ids = []
# affiliations = []
# countrys = []
# author_ids = []
# rights=[]
# wrongs=[]
# for i in range(0, len(df)):
#     paper_id = df.iloc[i]["Id"]
#
#     affiliation = df.iloc[i]["Affiliation"]
#     try:
#         affiliation = eval(affiliation)
#         # affiliation = list(set(affiliation))
#         country = df.iloc[i]["Country"]
#         country = eval(country)
#         # country = list(set(country))
#         author_id = df.iloc[i]["Author_id"]
#         author_id = eval(author_id)
#         # author_id = list(set(author_id))
#         paper_ids.append(paper_id)
#         affiliations.append(len(affiliation))
#         countrys.append(len(country))
#         author_ids.append(len(author_id))
#         if len(affiliation)==len(author_id)==len(country):
#             rights.append(paper_id)
#
#     except NameError:
#         print("wenti ")
#         wrongs.append(paper_id)
#         print(len(wrongs))
# print(len(rights))
# result_excel = pd.DataFrame()
# result_excel['Id'] = paper_ids
# result_excel['affiliations'] = affiliations
# result_excel['countrys'] = countrys
# result_excel['author_ids'] = author_ids
# result_excel.to_excel("控制变量.xlsx",index=False)


# 判断机构数据是否对应

# import pandas as pd
# df1 = pd.read_excel("2二分类.xlsx")
# df2 = pd.read_excel("机构类别.xlsx")
# queshi=[]
# zong=[]
# paper_ids=[]
# affiliations=[]
# aff_sum=df2["Top_affiliation"].tolist()
# types=df2["Type"].tolist()
# for i in range(0,len(df1)):
#     paper_id = df1.iloc[i]["Id"]
#     paper_ids.append(paper_id)
#     affiliation = df1.iloc[i]["type"]
#     affiliations.append(affiliation)
#     affiliation = eval(affiliation)
#     leixin = []
#     for aff in affiliation:
#         if aff =="Education" or aff=="Company" or aff == "Other":
#             leixin.append(aff)
#         elif aff in aff_sum:
#             type=types[aff_sum.index(aff)]
#             leixin.append(type)
#         elif "University" in aff or "university" in aff or "College" in aff or "college" in aff or "Health" in aff or "Medical" in aff:
#             leixin.append("Education")
#         elif "(" in aff or "ABBYY" in aff or "Metagram" in aff or "HNC Software" in aff or "HNC Software" in aff or "TCC Communications" in aff or "Thinking Machines Corporation" in aff or "Association for Computing Machinery" in aff or "LINGLINK" in aff or "The Harlequin Group" in aff or "Analytics Center of Excellence" in aff:
#             leixin.append("Company")
#         elif "Institute" or "institute" or "Independent" in aff:
#             leixin.append("Other")
#         else:
#             queshi.append(aff)
#
#
#     zong.append(leixin)
#
#
# queshi=list(set(queshi))
# print(queshi)
# print(len(queshi))
# result_excel = pd.DataFrame()
#
# result_excel['Id'] = paper_ids
# result_excel['affiliation'] = affiliations
# result_excel['type'] = zong
# # result_excel['affiliations'] = affiliations
# # result_excel['countrys'] = countrys
# # result_excel['author_ids'] = author_ids
# result_excel.to_excel("2二分类2.xlsx",index=False)

# import pandas as pd
# df1 = pd.read_excel("2二分类.xlsx")
#
# queshi=[]
# type1s=[]
# type2s=[]
# paper_ids=[]
# affiliations=[]
# for i in range(0,len(df1)):
#     paper_id = df1.iloc[i]["Id"]
#     paper_ids.append(paper_id)
#     affiliation = df1.iloc[i]["affiliation"]
#     # affiliations.append(affiliation)
#     affiliation = eval(affiliation)
#     type1 = df1.iloc[i]["type"]
#     type1 = eval(type1)
#     type2 = df1.iloc[i]["type1"]
#
#     type2 = eval(type2)
#     if len(type1)!=len(affiliation)!=len(type2):
#         print(paper_id)

#         queshi.append(paper_id)
#
# queshi=list(set(queshi))
# print(queshi)
# print(len(queshi))
# result_excel = pd.DataFrame()
#
# result_excel['Id'] = paper_ids
# result_excel['affiliation'] = affiliations
# result_excel['type'] = zong
# # result_excel['affiliations'] = affiliations
# # result_excel['countrys'] = countrys
# # result_excel['author_ids'] = author_ids
# result_excel.to_excel("2二分类2.xlsx",index=False)

# import pandas as pd
# leixin=[]
# paper_ids=[]
# df = pd.read_excel("2二分类.xlsx")
# for i in range(0, len(df)):
#     paper_id = df.iloc[i]["Id"]
#     paper_ids.append(paper_id)
#     affiliation = df.iloc[i]["affiliation"]
#     affiliation = eval(affiliation)
#     type1 = df.iloc[i]["type"]
#     type1 = eval(type1)
#     if "Company" in type1 and "Education" not in type1 and "Other" not in type1:
#         leixin.append(2)
#     elif "Company" in type1 and "Education" in type1 and "Other" not in type1:
#         leixin.append(1)
#     elif "Company" not in type1 and "Education" in type1 and "Other" not in type1:
#         leixin.append(0)
#     else:
#         leixin.append(4)
#
# result_excel = pd.DataFrame()
# result_excel['Id'] = paper_ids
# result_excel['type'] = leixin
#
# result_excel.to_excel("2二分类3.xlsx",index=False)

'''控制变量'''
# import pandas as pd
#
# df = pd.read_excel("2二分类.xlsx")
# df1 = pd.read_excel("国际合作论文id.xlsx",sheet_name="Sheet1")
# df2 = pd.read_excel("区分顶级.xlsx")
# dingji=df2["Name"].tolist()
# # paper_ids=df["Id"].tolist()
# # hezuo_ids=df1["Paper_id"].tolist()
# #
# # hezuo=[]
# # for i in paper_ids:
# #     if i in paper_ids:
# #         hezuo.append(1)
# #     else:
# #         hezuo.append(0)
# alljigou=[]
# for i in range(0,len(df)):
#     paper_id=df.iloc[i]["Id"]
#     affiliation = df.iloc[i]["affiliation"]
#     affiliation = eval(affiliation)
#     for aff in affiliation:
#         alljigou.append(aff)
# alljigou=list(set(alljigou))
# panduans=[]
# kydj=[]
# queshi=[]
# for aff in alljigou:
#     if aff in dingji:
#         panduan=df2.iloc[dingji.index(aff)]["类型"]
#         panduans.append(panduan)
#         kydj.append(aff)
#     else:
#         queshi.append(aff)

# result_excel = pd.DataFrame()
# result_excel1 = pd.DataFrame()
# result_excel['aff'] = kydj
# result_excel['type'] = panduans
# result_excel1['queshi']=queshi
#
# result_excel.to_excel("3控制变量.xlsx",index=False)
# result_excel1.to_excel("3控制变量1.xlsx",index=False)


# import pandas as pd
#
# df = pd.read_excel("3控制变量1.xlsx")
# df1 = pd.read_excel("排名.xlsx", sheet_name="CompaniesMarketCap")
# df2 = pd.read_excel("排名.xlsx", sheet_name="cs rangking")
#
# jigou = df["queshi"].tolist()
#
# dingjixuexiao = [str(item).lower() for item in df2["Institution"].tolist()]
#
# dingjigs = [str(item).lower() for item in df1["company"].tolist()]
# types = []
# haojigou = []
# queshi = []
#
# for i in jigou:
#     i_lower = str(i).lower()
#     if i_lower in dingjixuexiao:
#         haojigou.append(i)
#         types.append(1)
#     elif i_lower in dingjigs:
#         haojigou.append(i)
#         types.append(3)
#     else:
#         queshi.append(i)
#
# result_excel = pd.DataFrame()
# result_excel1 = pd.DataFrame()
# result_excel['aff'] = haojigou
# result_excel['type'] = types
# result_excel1['queshi'] = queshi
#
# result_excel.to_excel("3控制变量2.xlsx", index=False)
# result_excel1.to_excel("3控制变量3.xlsx", index=False)

'''检查实体总数是否正确'''
# import pandas as pd
#
# df= pd.read_excel("2二分类.xlsx")
# df2 = pd.read_excel("3控制变量.xlsx")
# djid=[]
# djjg=df2["aff"].tolist()
# for i in range(0,len(df)):
#     paper_id=df.iloc[i]["Id"]
#     aff=df.iloc[i]["affiliation"]
#     aff=eval(aff)
#     for a in aff:
#
#         type=df2.iloc[djjg.index(a)]["type"]
#         if type==1:
#             djid.append(paper_id)
#         elif type==3:
#             djid.append(paper_id)
#
# result_excel = pd.DataFrame()
# result_excel['Id'] = djid
#
#
# result_excel.to_excel("3控制变量3.xlsx", index=False)
#         zong.append(a)
#
# zong=list(set(zong))
#
# print(len(zong))

'''控制变量连表'''

# import pandas as pd
#
# df1=pd.read_excel("2二分类.xlsx")
# df2=pd.read_excel("国际合作论文id.xlsx",sheet_name="Sheet1")
# df3 = pd.read_excel("3控制变量3.xlsx")
#
# kz1=df2["Id"].tolist()
# kz2=df3["Id"].tolist()
# id1=[]
# paper_ids=[]
# id2=[]
# for i in range(0,len(df1)):
#     paper_id =df1.iloc[i]["Id"]
#     paper_ids.append(paper_id)
#     if paper_id in kz1:
#         id1.append(1)
#     else:
#         id1.append(0)
#     if paper_id in kz2:
#         id2.append(1)
#     else:
#         id2.append(0)
# result_excel = pd.DataFrame()
# result_excel['Id'] = paper_ids
# result_excel["ifguoji"]=id1
# result_excel["ifdj"]=id2
#
#
# result_excel.to_excel("3控制变量4.xlsx", index=False)

'''控制变量——团队规模、数量'''

# import pandas as pd
#
#
# df1=pd.read_excel("2二分类.xlsx")
#
# num_a=[]
# num_aff=[]
# num_coun=[]
# paper_ids=[]
#
# for i in range(0,len(df1)):
#     paper_id =df1.iloc[i]["Id"]
#     paper_ids.append(paper_id)
#     authors = df1.iloc[i]["Author_id"]
#     authors=eval(authors)
#     authors=list(set(authors))
#     num_a.append(len(authors))
#
#     affiliations=df1.iloc[i]["affiliation"]
#     affiliations=eval(affiliations)
#     affiliations=list(set(affiliations))
#     num_aff.append(len(affiliations))
#
#     countrys=df1.iloc[i]["Country"]
#     countrys=eval(countrys)
#     countrys=list(set(countrys))
#     num_coun.append(len(countrys))
#
# result_excel = pd.DataFrame()
# result_excel['Id'] = paper_ids
# result_excel["num_a"]=num_a
#
# result_excel["num_aff"]=num_aff
# result_excel["num_coun"]=num_coun
# result_excel.to_excel("3控制变量2.xlsx", index=False)


# import numpy as np
# import pandas as pd
# import datetime as dt
# #
# np.random.seed(0)
# pd.DataFrame(
#     {
#         "random":np.random.rand(5),
#         'text': ['hot', 'warm', 'cool', 'cold', 'warm'],
#         "truth":[np.random.choice([True,False]) for _ in range(5)]
#     },
#     index=pd.date_range(
#         end=dt.date(2019,4,21),
#         freq='1D',
#         periods=5,
#         name='date'
#     )
# )
# np.random.seed(0) # set seed so result is reproducible
# pd.DataFrame(
#     {
#         'random': np.random.rand(5),
#         'text': ['hot', 'warm', 'cool', 'cold', None],
#         'truth': [np.random.choice([True, False]) for _ in range(5)]
#     },
#     index=pd.date_range(
#         end=dt.date(2019, 4, 21),
#         freq='1D',
#         periods=5,
#         name='date'
#     )
# )

# import pandas as pd
import matplotlib.pyplot as plt
#
# # 从Excel文件中读取数据
# df = pd.read_excel('2二分类.xlsx',index_col='Id',sheet_name='Sheet1')
#
# # # 统计type列的值并进行可视化
# # counts = df['type2'].value_counts()
# # print(counts)
# # # 绘制计数频率直方图
# # plt.figure(figsize=(5, 5))
# # plt.bar(counts.index, counts.values)
# # plt.xlabel('Type')
# # plt.ylabel('Frequency')
# # plt.show()
#
# df.type2.value_counts().plot(
#     kind = 'barh',
#     figsize = (5,5),
#     title = '',
# )
# # 设置x轴刻度标签倾斜
# # plt.xticks(rotation=45)
#
# plt.show()

import pandas as pd

# df = pd.read_excel('2二分类.xlsx',index_col='Id',sheet_name='Sheet1')
# affs=[]
# company=[]
# education=[]
# rations=[]
# for i in range(0,len(df)):
#     # aff =  df.iloc[i]['affiliation']
#     ty = df.iloc[i]['type']
#     # dff = eval(aff)
#     ty = eval(ty)
# #     for j,af in enumerate(dff):
# #         affs.append(af)
# #         type = ty[j]
# #         if type == 'Company':
# #             company.append(af)
# #         elif type == 'Education':
# #             education.append(af)
# # affs=list(set(affs))
# # company=list(set(company))
# # education=list(set(education))
# # print(len(affs),len(company),len(education))
#     ration= ty.count('Company')/len(ty)
#     rations.append(ration)
#
# df=df.assign(
#     ratio = rations
# )
# df.to_excel('2二分类1.xlsx',index=False,index_label='Id')

# import pandas as pd
# import matplotlib.pyplot as plt
#
# fb = pd.read_excel('2二分类1.xlsx', index_col='year', parse_dates=True, usecols=['year', 'type2', 'ratio', 'Id'])
# fb.index = fb.index.to_period('Y')
#
# types = fb['type2'].unique()
#
# if len(types) > 0:
#     colors = ['blue', 'red', 'green', 'orange']  # 可根据类型数量自定义颜色列表
#     plt.figure(figsize=(10, 5))
#
#     for i, t in enumerate(types):
#         filtered_fb = fb[fb['type2'] == t]
#         if not filtered_fb.empty:
#             counts = filtered_fb.groupby(filtered_fb.index)['Id'].count()
#             counts.plot(kind='line', color=colors[i])
#
#     plt.xlabel('Year')
#     plt.ylabel('Count')
#     plt.legend(types)
#     plt.show()
# else:
#     print("No data satisfies the condition.")

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# df = pd.read_excel('2二分类.xlsx',sheet_name='Sheet2',usecols=['year','type','Id','num_a','num_aff'])
# # fb=df.assign(shangmian=lambda row: row.type.value_counts('Company'))
# str1 = 'good sjgj doog  good'
# # print(str1.count('good'))
# # print(df['type'].tolist())
# output = [con.count('Company') for con in df['type'].tolist()]
# output = pd.concat([df, pd.DataFrame(data=output, columns=['count'])], axis=1)
# result = output.assign(a= lambda x: x['count'] / x['num_a'])
# print(result)


'''工业界每年参与的不同机构与总机构数的比例'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import json
#
# df1 = pd.read_excel('工业界和学术界_type3.xlsx',usecols=['year','affiliation','Id'])
# df2 = pd.read_excel('消歧后所有机构.xlsx')
#
# df_id = df1['Id'].tolist()
# df_year = df1['year'].tolist()
# df_jgname = df1['affiliation'].tolist()
#
# dic_jigou = {}
# df2_jgname=df2[df2.columns[1]].tolist()
# df2_type=df2[df2.columns[0]].tolist()
#
# for i,name in enumerate(df2_jgname):
#     dic_jigou[name]=df2_type[i]
#
# years=[]
# jgs=[]
# result={}
# for i in df_id:
#     year=df_year[df_id.index(i)]
#     if year in result:
#         strings=df_jgname[df_id.index(i)]
#         string_list = eval(strings)
#         for i in string_list:
#             result[year].append(i)
#     else:
#         strings = df_jgname[df_id.index(i)]
#         string_list = eval(strings)
#         result[year]=string_list
#
# ratios={}
#
# types=[]
# for year in result:
#     names=result[year]
#     # names=list(set(names))
#     types=[]
#     for i in names:
#         types.append(dic_jigou[i])
#
#     count_f = types.count(3)+types.count(4)
#     print(count_f)
#     ratio=count_f/len(names)
#     ratios[year]=ratio
#
# years = list(ratios.keys())
# values = list(ratios.values())
# ratios = dict(sorted(ratios.items(), key=lambda x: x[0]))
#
# print(ratios)
# start_year = 2010
# end_year = 2021
#
# ratios = {year: value for year, value in ratios.items() if start_year <= year <= end_year}
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.plot(ratios.keys(), ratios.values(), color='grey', linewidth=2)
# ax.set_ylabel('Percentage Of Female Scientists')
# plt.show()

'''连接两表'''
# import pandas as pd
#
# df1=pd.read_excel("工业界和学术界_被引_性别.xlsx")
# df2=pd.read_excel("三大会议任务2023-3-21.xlsx",sheet_name='合并')
# df3=pd.merge(df1,df2,on="Id",how='left')
# df3.to_excel("工业级和学术界_最终.xlsx")

'''根据第一作者进行绝对的二分类'''
# import pandas as pd
#
# df = pd.read_excel('工业界和学术界.xlsx')
#
# type3=[]
# for i in range(0,len(df)):
#     if df.iloc[i]['type2']=='education&industry':
#         types = df.iloc[i]['type']
#         types=eval(types)
#         type3.append(types[0])
#     else:
#         type3.append(df.iloc[i]['type2'])
#
# print(type3.count('Company')+type3.count('industry'))
# output = pd.concat([df, pd.DataFrame(data=type3, columns=['type3'])], axis=1)
# output.to_excel('工业界和学术界_type3.xlsx')

'''对姓名进行排序'''

# import pandas as pd
#
# df = pd.read_excel('作者信息.xlsx',sheet_name='Sheet1')
#
# Ids = []
# namess=[]
# affiliationss=[]
# countryss=[]
# for i in range(0,len(df)):
#     paper_id = df.iloc[i]['Id']
#     if paper_id not in Ids and len(Ids)!=0:
#
#         affiliationss.append(affiliations)
#         affiliations = []
#         affiliations.append(df.iloc[i]['Affiliation'])
#
#         namess.append(names)
#         names=[]
#         Ids.append(paper_id)
#         names.append(df.iloc[i]['Author_id'])
#
#         countryss.append(countrys)
#         countrys = []
#         countrys.append(df.iloc[i]['Country'])
#
#
#     elif paper_id in Ids:
#         names.append(df.iloc[i]['Author_id'])
#         affiliations.append(df.iloc[i]['Affiliation'])
#         countrys.append(df.iloc[i]['Country'])
#
#     elif  len(Ids)==0:
#
#         countrys=[]
#         countrys.append(df.iloc[i]['Country'])
#
#         affiliations=[]
#         affiliations.append(df.iloc[i]['Affiliation'])
#
#         names=[]
#         Ids.append(paper_id)
#         names.append(df.iloc[i]['Author_id'])
#
#
#
# if len(names) > 0:
#     namess.append(names)
#
# if len(affiliations)>0:
#     affiliationss.append(affiliations)
#
# if len(countrys)>0:
#     countryss.append(countrys)
#
# print(len(affiliationss))
# print(len(namess))
# print(len(countryss))
#
# print(len(Ids))
# result ={}

# for i in range(0,len(Ids)):
#     result[Ids[i]]=namess[i]

# df = pd.DataFrame(result)
'''简易方法'''
#
# import pandas as pd
#
#
# df = pd.read_excel('作者信息.xlsx',sheet_name='Sheet4')
#
# fb = pd.read_excel('消歧后所有机构.xlsx')
#
# jigou={}
# for i in range(0,len(fb)):
#     jigou_name = fb.iloc[i]['affiliation']
#     types = fb.iloc[i]['type']
#     jigou[jigou_name] = types
#
# print(jigou)
#
# new_types = []
# for i in range(0,len(df)):
#     top_name = df.iloc[i]['Top_affiliation']
#     top_name = str(top_name).lower()
#     types =  jigou[top_name]
#     if types == 1:
#         new_types.append(1)
#     elif types == 2:
#         new_types.append(1)
#     elif types == 3:
#         new_types.append(0)
#     elif types == 4:
#         new_types.append(0)
#     elif types == 0:
#         new_types.append(2)
#
#
#
# ids = df['Id'].tolist()
# new_typess={}
# for i in range(0,len(df)):
#     new_typess[ids[i]] = new_types[i]
# # df = pd.concat([df,pd.DataFrame(new_types,columns=['new_types'])],axis=1)
# # # output = pd.concat([df, pd.DataFrame(data=type3, columns=['type3'])], axis=1)
# # df.to_excel('1111.xlsx')
#
# this_types=[]
# df1 = pd.read_excel('工业界和学术界_被引.xlsx')
# for i in range(0,len(df1)):
#     if df1.iloc[i]['type3']=='education&industry':
#         this_types.append(new_typess[df1.iloc[i]['Id']])
#     if df1.iloc[i]['type3']=='industry':
#         this_types.append(0)
#     if df1.iloc[i]['type3']=='education':
#         this_types.append(1)
#
#
# output = pd.concat([df1, pd.DataFrame(data=this_types, columns=['type22'])], axis=1)
#
#
# df2 = pd.read_excel('性别识别.xlsx',sheet_name='字典')
#
# result_sex={}
#
# for i in range(0,len(df2)):
#     result_sex[str(df2.iloc[i]['Id']).lower()]=df2.iloc[i]['Sex']
#
# df3 = pd.read_excel('作者信息.xlsx',sheet_name='Sheet5')
#
# diyi_sex=[]
# for i in range(0,len(df3)):
#     diyi_sex.append(result_sex[str(df3.iloc[i]['Author_id']).lower()])
#
# output = pd.concat([df1, pd.DataFrame(data=this_types, columns=['type22']),pd.DataFrame(data=diyi_sex,columns=['first_sex'])], axis=1)
#
#
# output.to_excel("工业界和学术界_被引_性别.xlsx",index=False)


'''主题数据连接'''
# import pandas as pd
# df1 = pd.read_excel('三大会议任务2023-3-21.xlsx',sheet_name='ACL')
# df2 = pd.read_excel('三大会议任务2023-3-21.xlsx',sheet_name='NAACL')
# df3 = pd.read_excel('三大会议任务2023-3-21.xlsx',sheet_name='EMNLP')
#
# result = pd.concat([df1, df2, df3], axis=0)
#
# result.to_excel("三大会议任务2023-3-21_合并.xlsx",index=False)
'''性别平衡比例'''
import pandas as pd

# df = pd.read_excel('性别聚类2.xlsx')
# df2 = pd.read_excel('2023.1.4.xlsx')
# result={}
# for i in range(0,len(df)):
#     sex = df.genders_y[i]
#     M_num =sex.count('M')
#     F_num =sex.count('F')
#     balance_ratio = min([M_num,F_num])/max([M_num,F_num])
#     paper_id = df.Id[i]
#     result[paper_id]=balance_ratio
#
# pd.DataFrame(result.items(),columns=['paper_id','balance_ratio']).to_excel('balance_ratio.xlsx',index=False)



'''最后的数据处理'''
# import pandas as pd
#
# df = pd.read_excel('工业界和学术界_被引_性别.xlsx',sheet_name='Sheet1')
#
# df2 = pd.read_excel('工业级和学术界_最终.xlsx',sheet_name='Sheet1')
#
# the_id =[id for id in df['Id'].tolist() if id not in df2['Id'].tolist()]
#
#
# print(the_id)
# industry_ratio=[]
# for i in range(0,len(df)):
#     typess=eval(df.iloc[i]['typess'])
#     industry_ratio.append((typess.count(3)+typess.count(4))/len(typess))
#
# output = pd.concat([df2, pd.DataFrame(data=industry_ratio,columns=['industry_ratio'])],axis=1)
#
# output.to_excel("工业界和学术界_last.xlsx",index=False)


# import pandas as pd
#
# df = pd.read_excel('工业界和学术界_被引.xlsx')
# fb = pd.read_excel('消歧后所有机构.xlsx')
#
# suoyoujigou=[]
# for i in range(0,len(df)):
#     aff = eval(df.iloc[i]['affiliation'])
#     for af in aff:
#         suoyoujigou.append(af)
# suoyoujigou=list(set(suoyoujigou))
#
# print(len(suoyoujigou))
#
# jigouleix={}
# for i in range(0,len(fb)):
#     jigouleix[fb.iloc[i]['affiliation']] = fb.iloc[i]['type']
#
# typess=[]
# for i in suoyoujigou:
#     types = jigouleix[i]
#
#     typess.append(types)
#     if types == 0:
#         print(i)
# print(typess.count(1)+typess.count(2))
# print(typess.count(3)+typess.count(4))
# print(typess.count(0))

'''绘制饼状图'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel('2023.1.4.xlsx',index_col='Id')
# counts=df['type2'].value_counts()
# type_percentages = counts / counts.sum() * 100
# type_percentages.index = type_percentages.index.to_series().replace({0: 'education', 1: 'industry'})
# type_percentages.plot(
#     kind='pie',
#     figsize=(10, 5),
#     autopct=lambda p: f'{p:.1f}%  ({int(p * counts.sum() / 100)})' if p >= 5 else '',
#     explode=[0.05] * len(type_percentages)  # 调整此处的数值以控制每个区域的间距
# )
#
# # 添加标题
# plt.title('Pie Chart of Type Percentages')
#
# # 添加图例
# plt.legend(labels=type_percentages.index, loc='upper right')
#
# # 调整图例和标签的字体大小
# plt.rcParams['font.size'] = 10
#
# # 去除边框
# plt.axis('off')
#
# # 显示图表
# plt.show()



'''绘制三种（四种）类型的时间序列图'''
# import pandas as pd
# import matplotlib.pyplot as plt
# #
# fb = pd.read_excel('2023.1.4.xlsx', index_col='year', parse_dates=True, usecols=['year', 'type3', 'ratio', 'Id'])
#
# #四条曲线图
# types = fb['type3'].unique()
# colors = ['blue', 'red', 'green']
# for i, t in enumerate(types):
#     filtered_fb = fb[fb['type3'] == t]
#     if not filtered_fb.empty:#必须有的一步判断，目前不确定为什么有这个
#             fb[fb['type3'] == t].groupby(filtered_fb.index)['Id'].count().plot(
#             kind='line',
#             figsize=(6, 5),
#             color=colors[i],
#             label=t,
#             legend=True,
#             linewidth = 2
#             )
# plt.show()
#
# #隔五年有一条的条形图
#
# df = pd.read_excel('2023.1.4.xlsx', index_col='year', parse_dates=True, usecols=['year', 'type3', 'ratio', 'Id'])
#
# # 获取特定年份的数据
# selected_years =  [x for x in range(1980, 2021) if x % 5 == 0] # 指定需要显示的年份
# df.index = df.index.to_period('Y')
# df[df.index.year.isin(selected_years)].groupby(['year', 'type3'])['Id'].count().unstack().plot(
#     kind='bar',
#     figsize=(6, 5),
#     legend=True
# )
#
# plt.show()
# import pandas as pd
# df1 = pd.read_excel('2023.1.4.xlsx')
# df2 = pd.read_excel('工业界和学术界_type3.xlsx')
#
# df1_id = df1['Id'].tolist()
# df2_id = df2['Id'].tolist()
# print(len(df1_id))
# print(len(df2_id))
# for i in df2_id:
#     if i not in df1_id:
#         print(i)

'''绘制新颖性变化趋势'''
# import pandas as pd
# import seaborn as sns
#
# # 读取数据
# df = pd.read_excel('score/score.xlsx')
#
# # 提取四列连续性变量
# variable1 = df['score2']
# variable2 = df['method2']
# variable3 = df['dataset2']
# variable4 = df['metric2']
# variable5 = df['tool2']
# # 创建包含四列变量的DataFrame
# data = pd.concat([variable1, variable2, variable3, variable4,variable5 ], axis=1)
#
# # 计算相关系数矩阵
# correlation_matrix = data.corr()
#
# # 可视化相关性矩阵
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
#
# # 显示图表
# plt.title('Correlation Matrix')
# plt.show()

'''绘制新颖性得分的变化趋势图'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel('2023.1.4.xlsx')
#
# df.groupby(['year'])['score'].mean().plot(
#     kind='line',
#     figsize=(10, 5),
#     legend=True
# )
#
# plt.show()

'''根据任务来区分'''
# import pandas as pd
# import matplotlib.pyplot as plt
# colors = [(0.6, 0.2, 0.1), (0.3, 0.5, 0.9), (0.4, 0.7, 0.2)]
# colors=[plt.cm.Set2(0),plt.cm.Set2(1),plt.cm.Set2(2)]
# df = pd.read_excel('2023.1.4.xlsx')
# df[df.task=='Sentiment Analysis and Opinion Mining'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(5, 6),
#     color = colors
# )
# plt.title('Sentiment Analysis and Opinion Mining')
# plt.xticks(range(len(df[df.task=='Sentiment Analysis and Opinion Mining'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Information Extraction'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v ,'%.2f'%v, ha='center', va='bottom')
#
#
# plt.show()
#
# df[df.task=='Dialogue'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Dialogue')
# plt.xticks(range(len(df[df.task=='Dialogue'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Dialogue'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v ,'%.2f'%v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Natural Language Generation'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Natural Language Generation')
# plt.xticks(range(len(df[df.task=='Natural Language Generation'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Natural Language Generation'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Resources and Evaluation'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Resources and Evaluation')
# plt.xticks(range(len(df[df.task=='Resources and Evaluation'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Resources and Evaluation'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Representation Learning and Text Representation'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Representation Learning and Text Representation')
# plt.xticks(range(len(df[df.task=='Representation Learning and Text Representation'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Representation Learning and Text Representation'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Parsing'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Parsing')
# plt.xticks(range(len(df[df.task=='Parsing'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Parsing'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Machine Learning'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Machine Learning')
# plt.xticks(range(len(df[df.task=='Machine Learning'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Machine Learning'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()
#
# df[df.task=='Information Extraction'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#
#     color=colors
# )
# plt.xticks(range(len(df[df.task=='Information Extraction'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Information Extraction'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.title('Information Extraction')
# plt.show()
#
# df[df.task=='Semantics'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.xticks(range(len(df[df.task=='Semantics'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Semantics'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.4f' % v, ha='center', va='bottom')
# plt.title('Semantics')
# plt.show()
#
# df[df.task=='Machine Translation'].groupby(['type3'])['score'].mean().plot(
#     kind='bar',
#     figsize=(4, 5),
#     color=colors
# )
# plt.title('Machine Translation')
# plt.xticks(range(len(df[df.task=='Machine Translation'].groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
# for i, v in enumerate(df[df.task=='Machine Translation'].groupby(['type3'])['score'].mean()):
#     plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
# plt.show()


'''不同机构类型不同类型新颖性的kw检验'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from statannotations.Annotator import Annotator
plt.figure(figsize=(10,10))


colors=[plt.cm.Set2(0),plt.cm.Set2(1),plt.cm.Set2(2)]
df = pd.read_excel("2024.1.6.xlsx",sheet_name='Sheet1')
a = df['type3']
b = df['method']
c = df['dataset']
d = df['metric']
e = df['tool']
plt.xticks(size=15)
plt.yticks(size=15)

# ax= seaborn.barplot(data = df,x=a,y=e)
# plt.bar_label(ax.containers[0],size=15)
# # box_pairs=[('education','education&industry'),('education','industry'),('education&industry','industry')]
# box_pairs=[(0,1),(0,2),(1,2)]

# annotator = Annotator(ax,pairs=box_pairs,x=a,y=b)
# annotator.configure(test='Mann-Whitney',text_format='star',line_height=0.05,line_width=3)
# annotator.apply_and_annotate()
# plt.xlabel('the types of institutions')
# plt.ylabel('the novelty of paper')
# plt.title('Different types of institutions and method novelty')
#
# # plt.title('Different types of institutions and method novelty')
# plt.show()


plt.title('Different types of institutions and dataset novelty')
plt.show()
df.groupby(['type3'])['dataset'].mean().plot(
    kind='bar',
    figsize=(5, 5),
    color=colors
)
plt.title('Different types of institutions and dataset novelty')
plt.xticks(range(len(df.groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
for i, v in enumerate(df.groupby(['type3'])['dataset'].mean()):
    plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
plt.show()

df.groupby(['type3'])['method'].mean().plot(
    kind='bar',
    figsize=(5, 5),
    color=colors
)
plt.title('Different types of institutions and method novelty')
plt.xticks(range(len(df.groupby(['type3']))), ['education', 'education&industry', 'industry'],rotation=0)
for i, v in enumerate(df.groupby(['type3'])['method'].mean()):
    plt.text(i, v, '%.2f' % v, ha='center', va='bottom')
plt.show()

df.groupby(['type3'])['tool'].mean().plot(
    kind='bar',
    figsize=(4, 5),
    color=colors
)
plt.title('Different types of institutions and tool novelty')
plt.show()

# from scipy.stats import kruskal
#
# df = pd.read_excel("2024.1.6.xlsx",sheet_name='Sheet1')
#
# group1 = df[df['type3'] == '0']['method'].tolist()
# group2 = df[df['type3'] == '1']['method'].tolist()
# group3 = df[df['type3'] == '2']['method'].tolist()
# statistic, p_value = kruskal(group1, group2, group3)
#
# # 输出检验结果
# print("Kruskal-Wallis 检验统计量：", statistic)
# print("p 值：", p_value)