import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
#base demo account to connect to the terminal
account=27865035
authorized=mt5.login(account)  
if authorized:
    print("connected to account #27865035 ".format(account))
else:
    print("failed to connect at account #27865035 , error code:".format(account, mt5.last_error()))


 #demo account that we will use for data analysis
    account=28896895
authorized=mt5.login(account, password="xzrtv8do")
if authorized:
    # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #28896895, error code: ".format(account, mt5.last_error()))
 
# attempt to enable the display of the EURJPY symbol in MarketWatch
selected=mt5.symbol_select("EURUSD",True)
if not selected:
    print("Failed to select EURUSD")
    mt5.shutdown()
    quit()
 
# display EURJPY symbol properties
symbol_info=mt5.symbol_info("EURUSD")
if symbol_info!=None:
    # display the terminal data 'as is'    
    print(symbol_info)
    print("EURUSD: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
    # display symbol properties as a list
    print("Show symbol_info(\"EURUSD\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURUSD")._asdict()
    for prop in symbol_info_dict:
        print("".format(prop, symbol_info_dict[prop]))
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
