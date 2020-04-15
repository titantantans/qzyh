# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:12:52 2020

@author: user
"""
import pandas as pd
import pyecharts as pe
import matplotlib.pyplot as plt
import matplotlib.style as psl
import os
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
os.chdir('D:/数据分析/关注Necklace的潜在购买用户研究/')
df=pd.read_excel('D:/数据分析/关注Necklace的潜在购买用户研究/某电商用户消费数据.xlsx')
psl.use('ggplot')

'''
第一步先来处理一下需要用到的字段,也就是整理数据需求
'''

'''******计算用户平台年龄'''
df['用户平台年龄']=pd.to_datetime('20190601')-df['客户注册日期']
'''******用户平台年龄以年为单位,用.dt.days获取了天数后除以365'''
df['用户平台年龄']=df['用户平台年龄'].dt.days/365
'''******用行为时间字段得出行为时刻'''
df['行为时刻']=df['行为时间'].dt.hour
'''
获取需要用到的necklace的数据data
'''
data=df[df['产品类别']=='Necklace']

'''
第二步指标的量化及初判
'''

'''
行为类别
'''
'''全样本的行为类别'''
pie=pe.Pie('全样本的行为类别环形图',title_pos='center',height=500,width=600)
attr=df['行为类别'].value_counts().index.tolist()
d=df['行为类别'].value_counts().values.tolist()
pie.add('全样本的行为类别环形图',attr,d,
        is_more_utils=True,
        is_label_show=True,
        is_legend_show=False,
        radius=[40,75])
pie.render('全样本的行为类别环形图.html')
order_all=df['行为类别'].value_counts()['Order']/len(df['行为类别'])
print('最终实现了购买行为占所有关注用户的行为的%.2f%%'%(order_all*100))
#所有有购买行为的用户(去重)/所有用户
order_cust_all=len(df[df['行为类别']=='Order']['客户编码'].value_counts())/len(df['客户编码'].value_counts())
print('最终实现了购买行为的用户占所有用户的%.2f%%'%(order_cust_all*100))

'''Necklace的行为类别'''
pie=pe.Pie('Necklace的行为类别环形图',title_pos='center',height=500,width=600)
attr=data['行为类别'].value_counts().index.tolist()
d=data['行为类别'].value_counts().values.tolist()
pie.add('Necklace的行为类别环形图',attr,d,
        is_more_utils=True,
        is_label_show=True,
        is_legend_show=False,
        radius=[40,75])
pie.render('Necklace的行为类别环形图.html')
order_necklace=data['行为类别'].value_counts()['Order']/len(data['行为类别'])
print('最终实现了necklace的购买行为占所有关注necklace用户的行为%.2f%%'%(order_necklace*100))
order_cust_necklace=len(data[data['行为类别']=='Order']['客户编码'].value_counts())/len(data['客户编码'].value_counts())
print('最终实现了购买行为的用户占所有用户的%.2f%%'%(order_cust_necklace*100))
'''
结论:
    对于全样本
    最终实现了购买行为占所有关注用户的行为的5.82%
    最终实现了购买行为的用户占所有用户的7.57%
    对于Necklace
    最终实现了necklace的购买行为占所有关注necklace用户的行为20.86%
    最终实现了购买行为的用户占所有用户的21.16%
    necklace两项数据都高于全样本数据,说明necklace引起用户的购买欲望高于平均水平,
    用户倾向于买necklace的可能性比较大,也就是说在这53个产品中，necklace是一个热门商品
'''

'''有购买行为的用户的行为特征分析'''
#获取所有跟Necklace有关的用户的数据
data_buy=data[data['行为类别']=='Order']
'''
性别
'''
#查看购买的用户中男女占比如何(画环形图)
pie=pe.Pie('Necklace产品真实购买用户特征-性别',title_pos='center',height=500,width=600)
attr=['男性','女性','未知']
pie.add('Necklace产品真实购买用户特征-性别',attr,data_buy['性别'].value_counts().values,
        is_more_utils=True,
        is_legend_show=False,
        is_label_show=True,
        radius=[45,70])
pie.render('Necklace产品真实购买用户特征-性别.html')
nan=data_buy['性别'].value_counts().values.tolist()[0]/len(data_buy['性别'])
nv=data_buy['性别'].value_counts().values.tolist()[1]/len(data_buy['性别'])
weizhi=data_buy['性别'].value_counts().values.tolist()[2]/len(data_buy['性别'])
print('男性用户占比为%2.f%%,女性用户占比为%2.f%%,未知性别用户占比为%2.f%%'%(nan*100,nv*100,weizhi*100))
'''
结论:
    [性别]:男性用户为59%,女性用户为40%,说明购买Necklace的男性用户比女性用户更多,
    按照常识,戴项链的女性比男性多,猜测这个结果是由于男性买项链送给女朋友老婆母亲所导致
'''

'''
年龄分段
'''
pie=pe.Pie('Necklace产品真实购买用户特征-年龄分段',title_pos='center',height=500,width=600)
attr=data_buy['年龄分段'].value_counts().sort_index().index
nlfd=data_buy['年龄分段'].value_counts().sort_index().values
pie.add('Necklace产品真实购买用户特征-年龄分段',attr,nlfd,
        is_more_utils=True,
        is_legend_show=False,
        is_label_show=True,
        radius=[45,70])
pie.render('Necklace产品真实购买用户特征-年龄分段.html')

n1=nlfd[0]/len(data_buy['年龄分段'])
n2=nlfd[1]/len(data_buy['年龄分段'])
n4=nlfd[2]/len(data_buy['年龄分段'])
n5=nlfd[3]/len(data_buy['年龄分段'])
n6=nlfd[4]/len(data_buy['年龄分段'])
print('1:%.2f%%,\n2:%.2f%%,\n4:%.2f%%,\n5:%.2f%%,\n6:%.2f%%'%(n1*100,n2*100,n4*100,n5*100,n6*100))
'''
结论:
    可以知道年龄段5购买的人数最多为45%,年龄段0购买的人数最少.所以这个Necklace在年龄段5中是比较受欢迎的
'''

'''
会员级别
'''
pie=pe.Pie('Necklace产品真实购买用户特征-会员级别',height=500,width=600)
attr=data_buy['会员级别'].value_counts().sort_index().index
hyjb=data_buy['会员级别'].value_counts().sort_index().values
pie.add('Necklace产品真实购买用户特征-会员级别',attr,hyjb,
        is_more_utils=True,
        is_legend_show=False,
        is_label_show=True,
        radius=[45,70])
pie.render('Necklace产品真实购买用户特征-会员级别.html')
h1=hyjb[0]/len(data_buy['会员级别'])
h3=hyjb[1]/len(data_buy['会员级别'])
h4=hyjb[2]/len(data_buy['会员级别'])
h5=hyjb[3]/len(data_buy['会员级别'])
h6=hyjb[4]/len(data_buy['会员级别'])
h7=hyjb[5]/len(data_buy['会员级别'])
print('1:%.2f%%,\n3:%.2f%%,\n4:%.2f%%,\n5:%.2f%%,\n6:%.2f%%,\n7:%.2f%%'%(h1*100,h3*100,h4*100,h5*100,h6*100,h7*100))
'''
结论:
    会员级别1跟6段购买最多34段购买最少
'''
'''
用户平台年龄
'''
data_buy['用户平台年龄'].plot(kind='kde',figsize=(12,6),
        label='Necklace产品真实购买用户特征-用户平台年龄',
        legend=True)
data['用户平台年龄'].plot(kind='kde',figsize=(12,6),
    label='Necklace产品用户特征-用户平台年龄',
    legend=True)
plt.savefig('Necklace产品用户平台年龄.jpg',dpi=400)
'''
结论:
    关注Necklace的用户平台使用年龄主要是2.5~7.5,其中2-3和6-7年用户有小波峰;
    实际购买Necklace的用户平台使用年龄再2到-8年，可见老用户购买可能性低于新用户，或者说老用户更纠结
'''
'''
行为时间
'''
data_buy['行为时刻'].plot(label='Necklace-购买时刻',kind='kde',figsize=(12,6),legend=True)
plt.savefig('Necklace产品购买时刻.jpg',dpi=400)
'''
结论:
    真实购买用户主要集中在9-21点这些时间,其中12点和20点有个峰值
'''

'''真实购买用户购买前的购买路径分析'''
'''
购买Necklace的用户购买前做过什么
'''
print('关注Necklace的用户数一共有%i个'%(len(data['客户编码'].value_counts())))
print('最后共有%i个用户购买了Necklace产品'%(len(data_buy['客户编码'].value_counts())))
#先拿出已经购买了的用户的客户编码
data_buy_id=data_buy[['客户编码']]
#将这个data_buy_id的列名修改一下 
data_buy_id.rename(columns={'客户编码':'真实购买客户编码'},inplace=True)
#将这个data_buy_id跟所有和Necklace有关的data连接一下,得出购买用户的行为路径
data_buy_lj=pd.merge(data,data_buy_id,left_on='客户编码',
                       right_on='真实购买客户编码',how='left')

data_buy_lj=data_buy_lj[data_buy_lj['真实购买客户编码'].notnull()]

b=data_buy_lj[data_buy_lj['行为类别']!='Order']
'''
结论:
    只有8个用户在购买前进行了浏览的行为,说明用户购买的目的还是挺明确的,也不怎么犹豫
'''
'''
购买Necklace的用户还看过什么其他的产品
'''
data_buy_qt=pd.merge(df,data_buy_id,left_on='客户编码',right_on='真实购买客户编码',how='left')
data_buy_qt=data_buy_qt[data_buy_qt['真实购买客户编码'].notnull()]
data_buy_qtcp=data_buy_qt[data_buy_qt['产品类别']!='Necklace']
data_buy_qtcp.groupby(by='产品类别')['客户编码'].count()
'''
结论:
    购买Necklace的用户还有11个看了Phone,3个看了Notebook还有PerfumeCoat等等
'''
'''
初判：
性别、年龄分段、会员级别、平台使用年龄对购买Necklace的可能性有所影响
而行为时间,购买前的路径分析等都没有太大影响,因此主要用这4个有效字段来进行分析
'''
'''
第三步:
    构建指标体系
'''
'''
年龄分段指标-10分
'''
dic=data_buy['年龄分段'].value_counts().to_dict()
for i in dic:
    dic[i]=dic[i]/data_buy['年龄分段'].value_counts().sum()*10
    
'''
用户平台年龄指标-10分
'''
data_buy['用户平台年龄分段']=pd.cut(data_buy['用户平台年龄'],bins=[0,1,2,3,4,5,10],
        labels=['1年以内','1-2年','2-3年','3-4年','4-5年','5年以上'])
dic=data_buy['用户平台年龄分段'].value_counts().to_dict()
for i in dic:
    dic[i]=dic[i]/data_buy['用户平台年龄分段'].value_counts().sum()*10

'''
性别指标-10分
'''
dic=data_buy['性别'].value_counts().to_dict()
for i in dic:
    dic[i]=dic[i]/data_buy['性别'].value_counts().sum()*10

'''
会员级别指标-10分
'''
dic=data_buy['会员级别'].value_counts().to_dict()
for i in dic:
    dic[i]=dic[i]/data_buy['性别'].value_counts().sum()*10

'''
指标量化
'''
import warnings
warnings.filterwarnings('ignore')
#筛选出数据后进行'客户编码'字段的去重
data_necklace=df[df['产品类别']=='Necklace'].drop_duplicates(subset='客户编码')
data_necklace['用户平台年龄分段']=pd.cut(data_necklace['用户平台年龄'],bins=[0,1,2,3,4,5,10],
        labels=['1年以内','1-2年','2-3年','3-4年','4-5年','5年以上'])
data_necklace=data_necklace[['客户编码','性别','年龄分段','会员级别','用户平台年龄分段']]
'''年龄分段'''
data_necklace['年龄分段_score']=0.83
data_necklace['年龄分段_score'][data_necklace['年龄分段']==2]=0.53
data_necklace['年龄分段_score'][data_necklace['年龄分段']==4]=1.69
data_necklace['年龄分段_score'][data_necklace['年龄分段']==5]=4.53
data_necklace['年龄分段_score'][data_necklace['年龄分段']==6]=2.41
'''性别'''
data_necklace['性别_score']=0.08
data_necklace['性别_score'][data_necklace['性别']=='M']=5.88
data_necklace['性别_score'][data_necklace['性别']=='W']=4.03
'''会员级别'''
data_necklace['会员级别_score']=3.33
data_necklace['会员级别_score'][data_necklace['会员级别']==3]=0.03
data_necklace['会员级别_score'][data_necklace['会员级别']==4]=0.08
data_necklace['会员级别_score'][data_necklace['会员级别']==5]=2
data_necklace['会员级别_score'][data_necklace['会员级别']==6]=3.23
data_necklace['会员级别_score'][data_necklace['会员级别']==7]=1.3
'''用户平台年龄分段'''
data_necklace['用户平台年龄分段_score']=2.35
data_necklace['用户平台年龄分段_score'][data_necklace['用户平台年龄分段']=='2-3年']=2.01
data_necklace['用户平台年龄分段_score'][data_necklace['用户平台年龄分段']=='3-4年']=1.91
data_necklace['用户平台年龄分段_score'][data_necklace['用户平台年龄分段']=='4-5年']=1.68
data_necklace['用户平台年龄分段_score'][data_necklace['用户平台年龄分段']=='5年以上']=2.04


'''
构建评估模型体系
'''
#把真实购买的客户编码标记出来
data_buy_id['是否购买']=1
#将购买的客户编码与data_necklace连接一下
data_necklace=pd.merge(data_necklace,data_buy_id,left_on='客户编码',
                       right_on='真实购买客户编码',how='left')
#将其他空值也就是没有购买的用户填充为0
data_necklace['是否购买'].fillna(0,inplace=True)
#筛选没有购买用户的客户编码
data_necklace_wgm=data_necklace[data_necklace['是否购买']==0]
#分别计算出四个字段指标中位数
a1=data_necklace[data_necklace['是否购买']==1]['年龄分段_score'].median()
a2=data_necklace[data_necklace['是否购买']==1]['性别_score'].median()
a3=data_necklace[data_necklace['是否购买']==1]['会员级别_score'].median()
a4=data_necklace[data_necklace['是否购买']==1]['用户平台年龄分段_score'].median()
print('年龄分段指标中位数:',a1) 
print('性别指标中位数:',a2)    
print('会员级别指标中位数:',a3) 
print('用户平台年龄指标中位数:',a4)
#选择出4个指标均大于中位数的潜在用户
data_necklace_qzyh=data_necklace_wgm[(data_necklace_wgm['年龄分段_score']>=a1)&
                                     (data_necklace_wgm['性别_score']>=a2)&
                                     (data_necklace_wgm['会员级别_score']>=a3)&
                                     (data_necklace_wgm['用户平台年龄分段_score']>=a4)]
#汇总潜在用户的list
qzyh=data_necklace_qzyh['客户编码'].value_counts().index.tolist()








