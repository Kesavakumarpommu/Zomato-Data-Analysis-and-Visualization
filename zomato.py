import pandas as pd
import plotly.express as px
#read a csv file
df1=pd.read_csv('zomato.csv')
df2=pd.read_csv('Country-Code.xlsx - Sheet1.csv',index_col=0)

df2.dropna(inplace = True)
df3=df2.to_dict()
df3=df3['Country']

#add column country name
df1['Country_name']=df1['Country Code'].apply(lambda x:df3[x])

#take a all currency values
cur=[]
for s in df1['Currency']:
    if s not in cur:
        cur.append(s)
        
        
        
        
        
        
        
#Add a column with rupees as the currency 

rupe={'Botswana Pula(P)':6.29, 'Brazilian Real(R$)':15.768,'Dollar($)':82.81, 'Emirati Diram(AED)':22.52, 'Indian Rupees(Rs.)':1,
          'Indonesian Rupiah(IDR)':0.0055, 'NewZealand($)':51.937,  'Pounds(專)':99.432,  'Qatari Rial(QR)':22.73,'Rand(R)':0.22, 'Sri Lankan Rupee(LKR)':0.23,
          'Turkish Lira(TL)':4.39}

print(len(rupe))

df1['Rupees']=df1['Currency'].apply(lambda x:rupe[x])


#compares indian currency with other country’s currency 

fig1 = px.bar(df1, x='Rupees', y='Country_name')
fig1.show()



fig2 = px.bar(df1, y='Cuisines', x='Average Cost for two', text_auto='.2s',
            title="Default: various text sizes, positions and angles")
fig2.show()




fig3 = px.pie(df1, values='Cuisines', names='Rupees')
fig3.show()



# which cuisines are costly in India
fig3 = px.pie(df1, values='Rupees', names='Cuisines', title='costlier cuisine ')
fig3.show()




fig = px.pie(df1, values='Rupees', names='Cuisines', color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()



