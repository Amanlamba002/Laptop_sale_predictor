import streamlit as st
import pickle
import numpy as np
# from xgboost import XGBRegressor

df = pickle.load(open('df1.pkl','rb'))
nav=st.sidebar.radio("Navigation",["Home","Predict"])

if nav=="Home":
    st.title("WECOME TO THE LAPTOP SALE PREDICTION SITE ")
    st.image("https://digiday.com/wp-content/uploads/sites/3/2021/01/gaming.gif?w=1030&h=579&crop=1")
     
    if st.checkbox("Show Data"):
        st.write(df)
    gr=st.selectbox("Do you want bar of price and company",['Yes','No'])
    if gr=="Yes":
        st.bar_chart(data=df,x='Company',y="Price")
        st.snow()
    else:
        st.subheader("Thank you ")
        st.balloons()




if nav=="Predict":
    # import the model
    pipe = pickle.load(open('pipe1.pkl','rb'))
    df = pickle.load(open('df1.pkl','rb'))

    st.title("Laptop Sale Predictor")

    # brand
    company = st.selectbox('Brand',df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type',df['TypeName'].unique())

    # Ram
    ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

    # weight
    weight = st.number_input('Weight of the Laptop')

    # Touchscreen
    touchscreen = st.selectbox('Touchscreen',['No','Yes'])

    # IPS
    ips = st.selectbox('IPS',['No','Yes'])

    # screen size
    screen_size = st.number_input('Screen Size in Inches')

    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

    #cpu
    cpu = st.selectbox('CPU',df['CpuType'].unique())

    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

    gpu = st.selectbox('GPU',df['GpuType'].unique())

    os = st.selectbox('OS',df['OS_Type'].unique())

    if st.button('Predict Price'):
        st.balloons()
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

        query = query.reshape(1,12)
        st.title("The predicted price is " + str(int(np.exp(pipe.predict(query)[0]))))
