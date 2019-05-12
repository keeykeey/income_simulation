import tkinter as tk 

root = tk.Tk()
root.title('Income_simulation')
root.geometry('600x700')

label0 =tk.Label(root,text="生涯年収を計算します",font=('',20))
label0.place(x=0,y=0)
#label0.pack()

label1 = tk.Label(root,text='(1) 入社する時の年齢を入力してください（23歳以上）。')
label1.place(x=5,y=35)
editbox1 = tk.Entry(root,width=2,borderwidth=1)
editbox1.place(x=15,y=55)

label2_1 = tk.Label(root,text='(2) 以下の入力欄に、各年齢での昇給幅(0〜6)を入力して下さい')
label2_1.place(x=5,y=75)
label2_2 = tk.Label(root,text='とても悪い→1 / 悪い→2 / やや悪い→3 / 普通→4 / まあまあ良い→5 / 大変良い→6')
label2_2.place(x=15,y=95)

label2_23 = tk.Label(root,text='23歳          号昇給')
#label2_23.place(x=15,y=175)
ebox23 = tk.Entry(width=2,borderwidth=1)
ebox23.insert(tk.END,4)
#ebox23.place(x=55,y=175)

label2_24 = tk.Label(root,text='24歳          号昇給')
label2_24.place(x=15,y=195)
ebox24 = tk.Entry(width=2,borderwidth=1)
ebox24.insert(tk.END,4)
ebox24.place(x=55,y=195)

label2_25 = tk.Label(root,text='25歳          号昇給')
label2_25.place(x=15,y=215)
ebox25 = tk.Entry(width=2,borderwidth=1)
ebox25.insert(tk.END,4)
ebox25.place(x=55,y=215)

label2_26 = tk.Label(root,text='26歳          号昇給')
label2_26.place(x=15,y=235)
ebox26 = tk.Entry(width=2,borderwidth=1)
ebox26.insert(tk.END,4)
ebox26.place(x=55,y=235)

label2_27 = tk.Label(root,text='27歳          号昇給')
label2_27.place(x=15,y=255)
ebox27 = tk.Entry(width=2,borderwidth=1)
ebox27.insert(tk.END,4)
ebox27.place(x=55,y=255)

label2_28 = tk.Label(root,text='28歳          号昇給')
label2_28.place(x=15,y=275)
ebox28 = tk.Entry(width=2,borderwidth=1)
ebox28.insert(tk.END,4)
ebox28.place(x=55,y=275)

label2_29 = tk.Label(root,text='29歳          号昇給')
label2_29.place(x=15,y=295)
ebox29 = tk.Entry(width=2,borderwidth=1)
ebox29.insert(tk.END,4)
ebox29.place(x=55,y=295)

label2_30 = tk.Label(root,text='30歳          号昇給')
label2_30.place(x=15,y=315)
ebox30 = tk.Entry(width=2,borderwidth=1)
ebox30.insert(tk.END,4)
ebox30.place(x=55,y=315)

label2_31 = tk.Label(root,text='31歳          号昇給')
label2_31.place(x=155,y=135)
ebox31 = tk.Entry(width=2,borderwidth=1)
ebox31.insert(tk.END,4)
ebox31.place(x=195,y=135)

label2_32 = tk.Label(root,text='32歳          号昇給')
label2_32.place(x=155,y=155)
ebox32 = tk.Entry(width=2,borderwidth=1)
ebox32.insert(tk.END,4)
ebox32.place(x=195,y=155)

label2_33 = tk.Label(root,text='33歳          号昇給')
label2_33.place(x=155,y=175)
ebox33 = tk.Entry(width=2,borderwidth=1)
ebox33.insert(tk.END,4)
ebox33.place(x=195,y=175)

label2_34 = tk.Label(root,text='34歳          号昇給')
label2_34.place(x=155,y=195)
ebox34 = tk.Entry(width=2,borderwidth=1)
ebox34.insert(tk.END,4)
ebox34.place(x=195,y=195)

label2_35 = tk.Label(root,text='35歳          号昇給')
label2_35.place(x=155,y=215)
ebox35 = tk.Entry(width=2,borderwidth=1)
ebox35.insert(tk.END,4)
ebox35.place(x=195,y=215)

label2_36 = tk.Label(root,text='36歳          号昇給')
label2_36.place(x=155,y=235)
ebox36 = tk.Entry(width=2,borderwidth=1)
ebox36.insert(tk.END,4)
ebox36.place(x=195,y=235)

label2_37 = tk.Label(root,text='37歳          号昇給')
label2_37.place(x=155,y=255)
ebox37 = tk.Entry(width=2,borderwidth=1)
ebox37.insert(tk.END,4)
ebox37.place(x=195,y=255)

label2_38 = tk.Label(root,text='38歳          号昇給')
label2_38.place(x=155,y=275)
ebox38 = tk.Entry(width=2,borderwidth=1)
ebox38.insert(tk.END,4)
ebox38.place(x=195,y=275)

label2_39 = tk.Label(root,text='39歳          号昇給')
label2_39.place(x=155,y=295)
ebox39 = tk.Entry(width=2,borderwidth=1)
ebox39.insert(tk.END,4)
ebox39.place(x=195,y=295)

label2_40 = tk.Label(root,text='40歳          号昇給')
label2_40.place(x=155,y=315)
ebox40 = tk.Entry(width=2,borderwidth=1)
ebox40.insert(tk.END,4)
ebox40.place(x=195,y=315)

label2_41 = tk.Label(root,text='41歳          号昇給')
label2_41.place(x=295,y=135)
ebox41 = tk.Entry(width=2,borderwidth=1)
ebox41.insert(tk.END,4)
ebox41.place(x=335,y=135)

label2_42 = tk.Label(root,text='42歳          号昇給')
label2_42.place(x=295,y=155)
ebox42 = tk.Entry(width=2,borderwidth=1)
ebox42.insert(tk.END,4)
ebox42.place(x=335,y=155)

label2_43 = tk.Label(root,text='43歳          号昇給')
label2_43.place(x=295,y=175)
ebox43 = tk.Entry(width=2,borderwidth=1)
ebox43.insert(tk.END,4)
ebox43.place(x=335,y=175)

label2_44 = tk.Label(root,text='44歳          号昇給')
label2_44.place(x=295,y=195)
ebox44 = tk.Entry(width=2,borderwidth=1)
ebox44.insert(tk.END,4)
ebox44.place(x=335,y=195)

label2_45 = tk.Label(root,text='45歳          号昇給')
label2_45.place(x=295,y=215)
ebox45 = tk.Entry(width=2,borderwidth=1)
ebox45.insert(tk.END,4)
ebox45.place(x=335,y=215)

label2_46 = tk.Label(root,text='46歳          号昇給')
label2_46.place(x=295,y=235)
ebox46 = tk.Entry(width=2,borderwidth=1)
ebox46.insert(tk.END,4)
ebox46.place(x=335,y=235)

label2_47 = tk.Label(root,text='47歳          号昇給')
label2_47.place(x=295,y=255)
ebox47 = tk.Entry(width=2,borderwidth=1)
ebox47.insert(tk.END,4)
ebox47.place(x=335,y=255)

label2_48 = tk.Label(root,text='48歳          号昇給')
label2_48.place(x=295,y=275)
ebox48 = tk.Entry(width=2,borderwidth=1)
ebox48.insert(tk.END,4)
ebox48.place(x=335,y=275)

label2_49 = tk.Label(root,text='49歳          号昇給')
label2_49.place(x=295,y=295)
ebox49 = tk.Entry(width=2,borderwidth=1)
ebox49.insert(tk.END,4)
ebox49.place(x=335,y=295)

label2_50 = tk.Label(root,text='50歳          号昇給')
label2_50.place(x=295,y=315)
ebox50 = tk.Entry(width=2,borderwidth=1)
ebox50.insert(tk.END,4)
ebox50.place(x=335,y=315)

label2_51 = tk.Label(root,text='51歳          号昇給')
label2_51.place(x=435,y=135)
ebox51 = tk.Entry(width=2,borderwidth=1)
ebox51.insert(tk.END,4)
ebox51.place(x=475,y=135)

label2_52 = tk.Label(root,text='52歳          号昇給')
label2_52.place(x=435,y=155)
ebox52 = tk.Entry(width=2,borderwidth=1)
ebox52.insert(tk.END,4)
ebox52.place(x=475,y=155)

label2_53 = tk.Label(root,text='53歳          号昇給')
label2_53.place(x=435,y=175)
ebox53 = tk.Entry(width=2,borderwidth=1)
ebox53.insert(tk.END,4)
ebox53.place(x=475,y=175)

label2_54 = tk.Label(root,text='54歳          号昇給')
label2_54.place(x=435,y=195)
ebox54 = tk.Entry(width=2,borderwidth=1)
ebox54.insert(tk.END,4)
ebox54.place(x=475,y=195)

label2_55 = tk.Label(root,text='55歳          号昇給')
label2_55.place(x=435,y=215)
ebox55 = tk.Entry(width=2,borderwidth=1)
ebox55.insert(tk.END,4)
ebox55.place(x=475,y=215)

label2_56 = tk.Label(root,text='56歳          号昇給')
label2_56.place(x=435,y=235)
ebox56 = tk.Entry(width=2,borderwidth=1)
ebox56.insert(tk.END,0)
ebox56.place(x=475,y=235)

label2_57 = tk.Label(root,text='57歳          号昇給')
label2_57.place(x=435,y=255)
ebox57 = tk.Entry(width=2,borderwidth=1)
ebox57.insert(tk.END,0)
ebox57.place(x=475,y=255)

label2_58 = tk.Label(root,text='58歳          号昇給')
label2_58.place(x=435,y=275)
ebox58 = tk.Entry(width=2,borderwidth=1)
ebox58.insert(tk.END,0)
ebox58.place(x=475,y=275)

label2_59 = tk.Label(root,text='59歳          号昇給')
label2_59.place(x=435,y=295)
ebox59 = tk.Entry(width=2,borderwidth=1)
ebox59.insert(tk.END,0)
ebox59.place(x=475,y=295)

label2_60 = tk.Label(root,text='60歳          号昇給')
label2_60.place(x=435,y=315)
ebox60 = tk.Entry(width=2,borderwidth=1)
ebox60.insert(tk.END,0)
ebox60.place(x=475,y=315)



label3_1 = tk.Label(root,text='(3)-1 主任に昇任する年齢を入力してください')
label3_1.place(x=5,y=335)
editbox3_1 = tk.Entry(width=2,borderwidth=1)
editbox3_1.place(x=15,y=355)

label3_2 = tk.Label(root,text='(3)-2 係長に昇任する年齢を入力してください')
label3_2.place(x=5,y=375)
editbox3_2 = tk.Entry(width=2,borderwidth=1)
editbox3_2.place(x=15,y=395)

label3_3 = tk.Label(root,text='(3)-3 課長に昇任する年齢を入力してください')
label3_3.place(x=5,y=415)
editbox3_3 = tk.Entry(width=2,borderwidth=1)
editbox3_3.place(x=15,y=435)

label3_4 = tk.Label(root,text='(3)-4 部長に昇任する年齢を入力してください')
label3_4.place(x=5,y=455)
editbox3_4 = tk.Entry(width=2,borderwidth=1)
editbox3_4.place(x=15,y=475)

label4 = tk.Label(root,text='(4) 入社時の初任給（号給）を入力して下さい（通常２９号給）。')
label4.place(x=5,y=495)
editbox4 = tk.Entry(width=2,borderwidth=1)
editbox4.place(x=15,y=515)



def program():
    '''
    GUIに入力された値に基づいて、シミュレーションプログラムを実行する。
    '''

    import main_program_GUI as mp
    import pandas as pd
    import numpy as np 
    from tkinter import messagebox

    # 入社年齢
    if (int(editbox1.get())<23) or (int(editbox1.get())>60) :
        editbox1.delete(0,tk.END)
        editbox1.insert(tk.END,23)
    val1 = int(editbox1.get())

    # 入社してから退職までの一年毎の昇給幅
    class out_of_range_exception(Exception):
        pass
    list_of_ebox2 = [ebox23,ebox24,ebox25,ebox26,ebox27,ebox28,ebox29,ebox30,
                     ebox31,ebox32,ebox33,ebox34,ebox35,ebox36,ebox37,ebox38,ebox39,ebox40,
                     ebox41,ebox42,ebox43,ebox44,ebox45,ebox46,ebox47,ebox48,ebox49,ebox50,
                     ebox51,ebox52,ebox53,ebox54,ebox55,ebox56,ebox57,ebox58,ebox59,ebox60]
    assessments = [assessment.get() for assessment in list_of_ebox2]
    for i in assessments:
        if (int(i) < 0 ) or (6 < int(i)):
            messagebox.showwarning('入力エラー','昇給幅は０から６までの数字を入力して下さい。')
            raise out_of_range_exception(i)
    val2 = pd.DataFrame({'assessment':assessments},index=range(23,61)) 
    

    list = [editbox3_1.get(),editbox3_2.get(),editbox3_3.get(),editbox3_4.get()]
    list_of_val3=[]
    over_60 = 61
    for j in list:
        if j == '':
            j = over_60
            over_60 = over_60 + 1   
        list_of_val3.append(int(j))
    val3_1=list_of_val3[0]
    val3_2=list_of_val3[1]
    val3_3=list_of_val3[2]
    val3_4=list_of_val3[3]


    '''
    val3_1=int(editbox3_1.get())
    val3_2=int(editbox3_2.get())
    val3_3=int(editbox3_3.get())
    val3_4=int(editbox3_4.get())
    '''
    val3 = pd.Series(range(1,6),index=[val1,val3_1,val3_2,val3_3,val3_4])   
    val4 = int(editbox4.get())

    df_all = mp.simulate(val1,val2,val3,val4)
    print(df_all)
    how_much_i_earn = str(df_all.iloc[37,8])[:-3] 
    print(how_much_i_earn)
    
    editbox5 = tk.Entry(width=30,borderwidth=1)
    editbox5.insert(tk.END,how_much_i_earn + '円       ')
    editbox5.place(x=5,y=595)


button = tk.Button(root,text='上の条件で生涯年収を計算する(PUSH ME!)',command = program,width=59,borderwidth=3)
button.place(x=5,y=535)

label5 = tk.Label(root,text='上のボタンを押すと、ここにシミュレーション結果が表示されます。')
label5.place(x=5,y=575)




root.mainloop()
