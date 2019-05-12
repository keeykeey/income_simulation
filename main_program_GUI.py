import numpy as np
import pandas as pd

# 毎年の昇給
assessment_low =pd.DataFrame({'assessment':[    0,4,4,4,4,4,4,4,
                                            4,4,4,4,4,4,4,4,4,4,
                                            4,4,4,4,4,4,4,4,4,4,
                                            4,4,4,4,4,0,0,0,0,0]},
                              index = range(23,61))
assessment_middle=pd.DataFrame({'assessment':[    0,4,4,6,5,5,4,4,
                                              4,4,4,4,4,6,5,5,4,4,
                                              4,4,4,4,4,6,5,5,4,4,
                                              4,4,4,4,4,2,1,1,0,0]},
                               index = range(23,61))
assessment_high  =pd.DataFrame({'assessment':[    0,5,5,6,5,5,5,5,
                                              5,5,5,5,5,6,5,5,5,5,
                                              5,5,5,5,5,6,5,5,5,5,
                                              5,5,5,5,5,2,1,1,1,1]},
                                index = range(23,61))
assessment_higer =pd.DataFrame({'assessment':[    0,6,6,6,6,6,6,6,
                                              6,6,6,6,6,6,6,6,6,6,
                                              6,6,6,6,6,6,6,6,6,6,
                                              6,6,6,6,6,2,2,2,2,2]},
                                index = range(23,61))
my_assessment_low  =pd.DataFrame({'assessment':[    0,0,0,0,4,4,4,4,
                                                5,4,4,4,4,4,4,4,4,5,
                                                5,4,4,4,4,4,4,4,4,5,
                                                5,4,4,4,4,0,0,0,0,0]},
                                index = range(23,61))
my_assessment_middle=pd.DataFrame({'assessment':[    0,0,0,0,4,4,4,4,
                                                 5,4,4,4,4,4,4,4,6,5,
                                                 5,4,4,4,4,4,4,4,6,5,
                                                 5,4,4,4,4,0,0,2,1,1]},
                                   index = range(23,61))

# 昇格するパターン
shoukaku_slow_pattern = pd.Series(range(1,6),index=[23,31,37,43,50])
shoukaku_middle_pattern = pd.Series(range(1,6),index=[23,29,35,40,45])
shoukaku_fast_pattern = pd.Series(range(1,6),index=[23,28,33,37,42])
shoukaku_my_pattern = pd.Series(range(1,6),index=[26,33,41,61,62])

def goukyuu(age = 26,
            shoukyuu_pattern = my_assessment_low,
            shoukaku_pattern = shoukaku_my_pattern,
            starting_salary = 29):
    '''
    age:入社した時の年齢
    shoukyuu_pattern:昇級パターン,pd.DataFrame
    shoukaku_pattern:昇格する年齢のパターン,pd.Series
    starting_salary:初任給
    役割　　入社から退職までの自身の毎年の級、号給を決める。
    引数　　age:入社時の号給　pattern:業績評価のパターンassessment_〇〇と言う変数の、データフレーム
    戻り値　pandasのDataFrame 
    '''

    # インデックスが年齢、１列が職級、２列が号給
    df_shoukakushoukyuu = pd.read_csv('g1_shoukaku.csv')
    df_getugakuh = pd.read_csv('g1_kyuuryou.csv') 
   
    shokukyuu_each_year = shoukaku_pattern.reindex(range(23,61),method='ffill')
    salary_table = pd.DataFrame(shokukyuu_each_year)
    salary_table['Step']=shoukyuu_pattern
    salary_table.iloc[age-23,1]=starting_salary
    salary_table= salary_table.rename(columns={0:'Grade'})
    
    for i in range(age+1,61):
        if int(salary_table.iloc[i-23,0])==5:
            salary_table.iloc[i-23,1]=2 #部長のランクは２給で固定となっている。この部分は改良の余地がある。
        elif salary_table.iloc[i-23,0]==salary_table.iloc[i-24,0]:
            salary_table.iloc[i-23,1]=int(salary_table.iloc[i-24,1])+int(salary_table.iloc[i-23,1])     
        elif (salary_table.iloc[i-23,0]>salary_table.iloc[i-24,0]) and (5>salary_table.iloc[i-23,0]):
            number = int(salary_table.iloc[i-23,0]-1)
            salary_table.iloc[i-23,1]=int(salary_table.iloc[i-24,1])+int(salary_table.iloc[i-23,1])#昇格した時の昇給
            salary_table.iloc[i-23,1]=int(df_shoukakushoukyuu.iloc[int(salary_table.iloc[i-23,1]-1),number]) 
    return salary_table
         
def monthly_salary(salary_table):
    '''
    役割    毎年の給料月額（/月）と地域手当（/月）を求める。
    引数    salary_table : goukyuu()の戻り値。DataFrameオブジェクト。
    戻り値  df_monthly_salary : 毎年の給料月額（/月）と地域手当（/月）の支給額が分かるデータフレーム
    ''' 

    df_monthly_salary = pd.DataFrame(index=range(23,61))
    df_monthly_salary['monthly_salary']=0
    df_monthly_salary['area_allowance']=0
    df_g1_kyuuryou = pd.read_csv('g1_kyuuryou.csv')
    for i in range(23,61):
        for j in range(1,6):
            if salary_table.iloc[i-23,0]==j:
                df_monthly_salary.iloc[i-23,0]=df_g1_kyuuryou.iloc[salary_table.iloc[i-23,1]-1,j]
                df_monthly_salary.iloc[i-23,1]=df_monthly_salary.iloc[i-23,0]*0.2
    return df_monthly_salary

def management_allowance(salary_table):
    df_management_allowance = pd.DataFrame(index=range(23,61))
    df_management_allowance['management_allowance']=0
    for i in range(23,61):
        if salary_table.iloc[i-23,0]==4:
            df_management_allowance.iloc[i-23,0]=80000
        elif salary_table.iloc[i-23,0]==5:
            df_management_allowance.iloc[i-23,0]=126900
    return df_management_allowance

def bounus(salary_table,df_monthly_salary):
    '''
    役割　毎年の特別給支給額を求める。
    引数　salary_table : goukyuu()の戻り値。データフレーム。
          df_monthly_salary() ; monthly_salary()の戻り値。
    戻り値　df_bounus : 毎年の特別給支給額が分かるデータフレーム。    
    '''
    
    df_bounus = pd.DataFrame(index=range(23,61))
    df_bounus['bounus']=0
    for i in range(23,61):
        kisogaku_large = df_monthly_salary.iloc[i-23,0]+df_monthly_salary.iloc[i-23,1]
        kisogaku_small = df_monthly_salary.iloc[i-23]
        df_bounus.iloc[i-23,0]=kisogaku_large*4.5

    return df_bounus


def simulate(age = 26,
             shoukyuu_pattern = my_assessment_low,
             shoukaku_pattern = shoukaku_my_pattern,
             starting_salary = 29):
    salary_table=goukyuu(age,shoukyuu_pattern,shoukaku_pattern,starting_salary)
    df_monthly_salary = monthly_salary(salary_table)
    df_management_allowance = management_allowance(salary_table)
    df_bounus = bounus(salary_table,df_monthly_salary)

    df_all = pd.concat([salary_table,df_monthly_salary,df_management_allowance,df_bounus],axis=1)

    df_all['monthly_income']=df_all.sum(axis=1)-df_all['bounus']
    df_all['annual_income']=df_all['monthly_income']*12+df_all['bounus']

    df_all['lifetime_annual_income'] = df_all['annual_income'].cumsum()
    return(df_all)

if __name__ == '__main__':
    df_all = simulate()
    print(df_all)

