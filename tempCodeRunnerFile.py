
# import pickle
# def storeData():
#    # initializing data to be stored in db
#    amazon = {'key' : 'amazon', 'product_name' : 'amazonProductName', 'price' : amazonProductPrice}
#    flipkart = {'key' : 'flipkart', 'product_name' : 'flipkartProductName', 'price' : flipkartProductPrice}
   

#    # database
#    db = {}
#    db['amazon'] = amazon
#    db['flipkart'] = flipkart


    
#    # Its important to use binary mode
#    dbfile = open('price_data', 'ab')
    
#    # source, destination
#    pickle.dump(db, dbfile)                    
#    dbfile.close()

#    #Loading Stored Data
# def read_data():
#    dbfile = open('price_data', 'rb')    
#    sb_store = pickle.load(dbfile)
#    for items in db_store:
#        print(items, ' :: ', db[items])
#    dbfile.close()