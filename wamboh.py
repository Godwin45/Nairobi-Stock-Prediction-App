import streamlit as st
from datetime import date
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from PIL import Image

st.title('Nairobi Stock Price Prediction')
image = Image.open('stockpic.jpg')
st.image(image, caption='All rights Reserved @ Godwin')
# AGRICULTURE = ('Agricultural/AGRICULTURE.csv')
EGAD = ('Agricultural/EGAD Historical Data.csv')
KAPC = ('Agricultural/KAPC Historical Data.csv')
KUKZ = ('Agricultural/KUKZ Historical Data.csv')
SASN = ('Agricultural/SASN Historical Data.csv')
WTK = ('Agricultural/WTK Historical Data.csv')
# BANK = ('BANK.csv')
BBK = ('Banking/BBK Historical Data.csv')
CFC= ('Banking/CFC Historical Data.csv')
COOP = ('Banking/COOP Historical Data.csv')
DTK = ('Banking/DTK Historical Data.csv')
EQTY = ('Banking/EQTY Historical Data.csv')
HFCK = ('Banking/HFCK Historical Data.csv')
IMH = ('Banking/IMH Historical Data.csv')
KCB = ('Banking/KCB Historical Data.csv')
# KEGN = ('Banking/KEGN Historical Data.csv')
KPLC = ('Banking/KPLC Historical Data.csv')
NBK = ('Banking/NBK Historical Data.csv')
NIC = ('Banking/NIC Historical Data.csv')
SCBK = ('Banking/SCBK Historical Data.csv')
AUTOMOBILES = ('Automobiles_Accessories/CGKE Historical Data.csv')
# COMMERCIAL_SERVICES = ('Commercial_Services/COMMERCIAL_SERVICES.csv')
DCON = ('Commercial_Services/DCON Historical Data.csv')
EVRD = ('Commercial_Services/EVRD Historical Data.csv')
FIRE = ('Commercial_Services/FIRE Historical Data.csv')
KQNA = ('Commercial_Services/KQNA Historical Data.csv')
LKL = ('Commercial_Services/LKL Historical Data.csv')
NBV = ('Commercial_Services/NBV Historical Data.csv')
NMG = ('Commercial_Services/NMG Historical Data.csv')
SCAN = ('Commercial_Services/SCAN Historical Data.csv')
TPSE = ('Commercial_Services/TPSE Historical Data.csv')
UCHM = ('Commercial_Services/UCHM Historical Data.csv')
XPRS = ('Commercial_Services/XPRS Historical Data.csv')
# CONSTRUCTION = ('Construction_Allied/CONSTRUCTION.csv')
ARM = ('Construction_Allied/ARM Historical Data.csv')
BAMB = ('Construction_Allied/BAMB Historical Data.csv')
BERG = ('Construction_Allied/BERG Historical Data.csv')
CABL = ('Construction_Allied/CABL Historical Data.csv')
PORT = ('Construction_Allied/PORT Historical Data.csv')
# ENERGY = ('Energy_Petroleum/ENERGY.csv')
KENGEN = ('Energy_Petroleum/KEGN Historical Data.csv')
KENO = ('Energy_Petroleum/KENO Historical Data.csv')
KPLC = ('Energy_Petroleum/KPLC Historical Data.csv')
TOTL = ('Energy_Petroleum/TOTL Historical Data.csv')
UMME = ('Energy_Petroleum/UMME Historical Data.csv')
# INSURANCE = ('Insurance/BRIT Historical Data.csv')
BRIT = ('Insurance/BRIT Historical Data.csv')
CFCI = ('Insurance/CFCI Historical Data.csv')
CIC = ('Insurance/CIC Historical Data.csv')
KNRE = ('Insurance/KNRE Historical Data.csv')
PAFR = ('Insurance/PAFR Historical Data.csv')
HAFR = ('Investment/HAFR Historical Data.csv')
ICDC = ('Investment/ICDC Historical Data.csv')
OCH = ('Investment/OCH Historical Data.csv')
TCL = ('Investment/TCL Historical Data.csv')
INVESTMENT_SERVICES = ('Investment_services/NSE Historical Data.csv')
# MANUFACTURING = ('Manufacturing_Allied/MANUFACTURING Historical Data.csv')
BAT = ('Manufacturing_Allied/BAT Historical Data.csv')
BOC = ('Manufacturing_Allied/BOC Historical Data.csv')
CARB = ('Manufacturing_Allied/CARB Historical Data.csv')
EABL = ('Manufacturing_Allied/EABL Historical Data.csv')
MSC = ('Manufacturing_Allied/MSC Historical Data.csv')
ORCH = ('Manufacturing_Allied/ORCH Historical Data.csv')
UNGA = ('Manufacturing_Allied/UNGA Historical Data.csv')
REAL_ESTATE = ('Real_Estate_Investment/FAHR Historical Data.csv')
SAFARICOM = ('Telecommunication_Technology/SCOM Historical Data.csv')



stocks = ("🚜🌾🌽AGRICULTURE🥕🍅🥒","EGAD","KAPC","KUKZ","SASN","WTK","🏦💱🏧BANK💸💰💵🤑","BBK","CFC","COOP","DTK",
"EQTY","HFCK","IMH","KCB","KPLC","NBK","NIC","SCBK","AUTOMOBILES","🕵️COMMERCIAL_SERVICES🧑🏾‍💼","DCON","EVRD",
"FIRE","KQNA","LKL","NBV","NMG","SCAN","TPSE","UCHM","XPRS","🏗️🚧🛠️CONSTRUCTION🧱👷🏻🏗","ARM","BAMB","CABL","PORT",
"⚡🔋💥ENERGY🌟☀️🌌","KENGEN","KENO","KPLC","TOTL","UMME","🛡️📋INSURANCE🔐⚕","BRIT","CFCI","CIC","KNRE","PAFR","HAFR","ICDC","OCH",
"TCL","INVESTMENT_SERVICES","🧑‍💻MANUFACTURING👷🏼‍♀️","BAT","BOC","CARB","EABL","MSC","ORCH","UNGA","REAL_ESTATE","SAFARICOM")

selected_stock = st.selectbox('Select dataset for prediction', stocks)

# start = st.date_input('Start', value = pd.to_datetime('2013-01-01'))
# end = st.date_input('End', value = pd.to_datetime('today'))

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache
def load_data(data):
    
    if selected_stock == ("KAPC"):
        data = pd.read_csv(KAPC)
    elif selected_stock == ("KUKZ"):
        data = pd.read_csv(KUKZ)
    elif selected_stock == ("SASN"):
        data = pd.read_csv(SASN)
    elif selected_stock == ("WTK"):
        data = pd.read_csv(WTK) 
    elif selected_stock == ("BBK"):
        data = pd.read_csv(BBK)
    elif selected_stock == ("CFC"):
        data = pd.read_csv(CFC)
    elif selected_stock == ("COOP"):
        data = pd.read_csv(COOP)
    elif selected_stock == ("DTK"):
        data = pd.read_csv(DTK)
    elif selected_stock == ("EQTY"):
        data = pd.read_csv(EQTY)
    elif selected_stock == ("HFCK"):
        data = pd.read_csv(HFCK)
    elif selected_stock == ("IMH"):
        data = pd.read_csv(IMH)
    elif selected_stock == ("KCB"):
        data = pd.read_csv(KCB)
    elif selected_stock == ("KPLC"):
        data = pd.read_csv(KPLC)
    elif selected_stock == ("NBK"):
        data = pd.read_csv(NBK)
    elif selected_stock == ("NIC"):
        data = pd.read_csv(NIC)
    elif selected_stock == ("SCBK"):
        data = pd.read_csv(SCBK)
    elif selected_stock == ("AUTOMOBILES"):
        data = pd.read_csv(AUTOMOBILES)
    elif selected_stock == ("DCON"):
        data = pd.read_csv(DCON)
    elif selected_stock == ("EVRD"):
        data = pd.read_csv(EVRD)
    elif selected_stock == ("FIRE"):
        data = pd.read_csv(FIRE)
    elif selected_stock == ("KQNA"):
        data = pd.read_csv(KQNA)
    elif selected_stock == ("LKL"):
        data = pd.read_csv(LKL)
    elif selected_stock == ("NBV"):
        data = pd.read_csv(NBV)
    elif selected_stock == ("NMG"):
        data = pd.read_csv(NMG)
    elif selected_stock == ("SCAN"):
        data = pd.read_csv(SCAN)
    elif selected_stock == ("TPSE"):
        data = pd.read_csv(TPSE)
    elif selected_stock == ("UCHM"):
        data = pd.read_csv(UCHM)
    elif selected_stock == ("XPRS"):
        data = pd.read_csv(XPRS)
    elif selected_stock == ("ARM"):
        data = pd.read_csv(ARM)
    elif selected_stock == ("BAMB"):
        data = pd.read_csv(BAMB)
    elif selected_stock == ("CABL"):
        data = pd.read_csv(CABL)
    elif selected_stock == ("PORT"):
        data = pd.read_csv(PORT)
    elif selected_stock == ("KENGEN"):
        data = pd.read_csv(KENGEN)
    elif selected_stock == ("KENO"):
        data = pd.read_csv(KENO)
    elif selected_stock == ("KPLC"):
        data = pd.read_csv(KPLC)
    elif selected_stock == ("TOTL"):
        data = pd.read_csv(TOTL)
    elif selected_stock == ("UMME"):
        data = pd.read_csv(UMME)
    elif selected_stock == ("BRIT"):
        data = pd.read_csv(BRIT)
    elif selected_stock == ("CFCI"):
        data = pd.read_csv(CFCI)
    elif selected_stock == ("CIC"):
        data = pd.read_csv(CIC)
    elif selected_stock == ("KNRE"):
        data = pd.read_csv(KNRE)
    elif selected_stock == ("PAFR"):
        data = pd.read_csv(PAFR)
    elif selected_stock == ("HAFR"):
        data = pd.read_csv(HAFR)
    elif selected_stock == ("ICDC"):
        data = pd.read_csv(ICDC)
    elif selected_stock == ("OCH"):
        data = pd.read_csv(OCH)
    elif selected_stock == ("TCL"):
        data = pd.read_csv(TCL)
    elif selected_stock == ("INVESTMENT_SERVICES"):
        data = pd.read_csv(INVESTMENT_SERVICES)
    elif selected_stock == ("BAT"):
        data = pd.read_csv(BAT)
    elif selected_stock == ("BOC"):
        data = pd.read_csv(BOC)
    elif selected_stock == ("CARB"):
        data = pd.read_csv(CARB)
    elif selected_stock == ("EABL"):
        data = pd.read_csv(EABL)
    elif selected_stock == ("MSC"):
        data = pd.read_csv(MSC)
    elif selected_stock == ("ORCH"):
        data = pd.read_csv(ORCH)
    elif selected_stock == ("UNGA"):
        data = pd.read_csv(UNGA)
    elif selected_stock == ("REAL_ESTATE"):
        data = pd.read_csv(REAL_ESTATE)


    else:
         data = pd.read_csv(SAFARICOM)


    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Low'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

plot_raw_data()


# Predict forecast with Prophet.
df_train = data[['Date','Open']]
df_train = df_train.rename(columns={"Date": "ds", "Open": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Prediction data')
st.write(forecast.tail())


st.write(f'Prediction plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Prediction components")
fig2 = m.plot_components(forecast)
st.write(fig2)
