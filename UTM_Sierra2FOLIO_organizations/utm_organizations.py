import datetime
from datetime import datetime
import json
import uuid
import os
import os.path
import requests
import io
import math
import csv
import time
import random
import logging
import pandas as pd
import folioAcqfunctions as faf
from typing import List
import tkinter as tk
from tkinter import filedialog, messagebox, ttk



##############

def readInterfacesSpreadsheet(idSearch,path,sheetName,customerName):
    rowi=""
    col_types={"CTACT CODE":str}
    interfacesId=[]
    conID=""
    FN=""
    LN=""
    contcategories=""
    interface = pd.read_excel(path,sheet_name=sheetName, dtype=col_types)
    #print(interface)
    interface_filter = interface[interface['CTACT CODE']== idSearch]
    interface_filter = interface_filter.apply(lambda x: x.fillna(""))
    print("Interface founds: ",len(interface_filter))
    for inter, rowi in interface_filter.iterrows():
        intName=""
        inttype=""
        interNote=""
        interStanote=""
        intUri=""
        creuser=""
        crepass=""
        if rowi[1]:
            interId=str(uuid.uuid4())
            if rowi[1]:
                intName =str(rowi[1])
            if rowi[2]: inttype =faf.interfacetype(rowi[2])
            if rowi[3]: intUri =str(rowi[3])
            if rowi[4]: interNote =str(rowi[4])
            if rowi[5]: creuser =str(rowi[5])
            if rowi[6]: crepass =str(rowi[6])
            if rowi[7]: interStanote=str(rowi[7])
            org=faf.interfaces(interId,intName,intUri,inttype)
            org.printinterfaces(customerName, interNote,interStanote)
            if (crepass!="") or (creuser!=""):
                org.printcredentials(interId,creuser,crepass, customerName)
            
            interfacesId.append(interId)
    return interfacesId

def readContactsSpreadsheet(idSearch,path,sheetName,customerName,a):
    #Organizations
    if idSearch=="jstor":
        a=1
    rowc=""
    col_types={"SIERRA #":str}
    contactsId=""
    conID=""
    FN=""
    LN=""
    contcategories=""
    #contacts = pd.read_excel(path,sheet_name=sheetName, dtype=col_types)
    contacts = faf.readFileToDataFrame(path)
    #print(contacts)
    contact_filter = contacts[contacts['SIERRA #']== idSearch]
    contact_filter = contact_filter.apply(lambda x: x.fillna(""))
    print("Contacts founds: ",len(contact_filter))
    for c, rowc in contact_filter.iterrows():
            contactprefix=""
            if rowc[a]:
                if rowc[a-1]: contactprefix= rowc[a-1]
                #contactName_temp=str(rowc[a])+" "+str(rowc[a+1])
                #ContactName=faf.SplitString(contactName_temp)
                FN=rowc[a+1]
                LN=rowc[a]
            else:
                if rowc[a-1]: contactprefix= rowc[a-1]
                FN="NaN"
                LN="NaN"
                #Title go to notes and categorical
                #contactTitle="NULL"
                #if namesheet.cell_value(c,4)!="NULL":
                #    contactTitle=str(namesheet.cell_value(c,4))
                #address
            contactLang="en-us"
            contactnotes=""
            addcontnote=True
            if addcontnote:
                if rowc[48]:
                    contactnotes=rowc[48]

            addcono=False
            if addcono:
                if rowc[8]:
                    contactnotes= rowc[8]
                    
            #Contacts phone
            contactphoneN=[]
            addpho=True
            if addpho:
                contactphoneN=""
                contactphoneN=faf.org_phoneNumbers(contact_filter.loc[c],68,76,80)
                
                
            #Contact emails
            contactemail=[]
            addmails=True
            if addmails:
                contactemail=""
                contactemail=faf.org_emails(contact_filter.loc[c],56,64)

            #Contact Address
            contactaddresses=[]
            addadd=True
            if addadd:
                contactaddresses=""
                contactaddresses=faf.org_addresses(contact_filter.loc[c],88)

            #INACTIVE / ACTIVE
            contactinactive= False
            #Contact URL
            contacturls=[]
            addurl=False
            if addurl:
                contacturls="" 
                contacturls=faf.org_urls(contact_filter.loc[c],84)
                
            contcategories=[]
            if rowc[47]:
                contcategories.append(faf.SearchJsonFile(rowc[47],"categories"))
                print(contcategories)
            conID=str(uuid.uuid4())
            contactsId=conID
            #(self,contactID,contactfirstName, contactlastName, contactcategories):
            ctc=faf.contactsClass(conID,FN,LN,contcategories,contactLang)
            #def printcontacts(self,cont_phone,cont_email, cont_address,cont_urls,cont_categories,contactnotes,fileName):
            ctc.printcontactsClass(contactprefix,contactphoneN, contactemail, contactaddresses, contacturls,contcategories,contactnotes,customerName)  
    return contactsId


def readContactsSpreadsheet2(idSearch,path,sheetName,customerName,a):
    #Organizations
    if idSearch=="jstor":
        a=1
    rowc=""
    col_types={"SIERRA #":str}
    contactsId=""
    conID=""
    FN=""
    LN=""
    contcategories=""
    #contacts = pd.read_excel(path,sheet_name=sheetName, dtype=col_types)
    contacts = faf.readFileToDataFrame(path)
    #print(contacts)
    contact_filter = contacts[contacts['SIERRA #']== idSearch]
    contact_filter = contact_filter.apply(lambda x: x.fillna(""))
    print("Contacts founds: ",len(contact_filter))
    for c, rowc in contact_filter.iterrows():
            contactprefix=""
            if rowc[50]:
                if rowc[49]: contactprefix= rowc[49]
                #contactName_temp=str(rowc[a])+" "+str(rowc[a+1])
                #ContactName=faf.SplitString(contactName_temp)
                FN=rowc[51]
                LN=rowc[50]
            else:
                if rowc[a-1]: contactprefix= rowc[a-1]
                FN="NaN"
                LN="NaN"
                #Title go to notes and categorical
                #contactTitle="NULL"
                #if namesheet.cell_value(c,4)!="NULL":
                #    contactTitle=str(namesheet.cell_value(c,4))
                #address
            contactLang="en-us"
            contactnotes=""
            addcontnote=True
            if addcontnote:
                if rowc[48]:
                    contactnotes=rowc[55]

            addcono=False
            if addcono:
                if rowc[8]:
                    contactnotes= rowc[8]
                    
            #Contacts phone
            contactphoneN=[]
            addpho=True
            if addpho:
                contactphoneN=""
                contactphoneN=faf.org_phoneNumbers(contact_filter.loc[c],72)
                
                
            #Contact emails
            contactemail=[]
            addmails=True
            if addmails:
                contactemail=""
                contactemail=faf.org_emails(contact_filter.loc[c],60)

            #Contact Address
            contactaddresses=[]
            addadd=False
            if addadd:
                contactaddresses=""
                contactaddresses=faf.org_addresses(contact_filter.loc[c],88)

            #INACTIVE / ACTIVE
            contactinactive= False
            #Contact URL
            contacturls=[]
            addurl=False
            if addurl:
                contacturls="" 
                contacturls=faf.org_urls(contact_filter.loc[c],84)
                
            contcategories=[]
            if rowc[54]:
                contcategories.append(faf.SearchJsonFile(rowc[47],"categories"))
                print(contcategories)
            conID=str(uuid.uuid4())
            contactsId=conID
            #(self,contactID,contactfirstName, contactlastName, contactcategories):
            ctc=faf.contactsClass(conID,FN,LN,contcategories,contactLang)
            #def printcontacts(self,cont_phone,cont_email, cont_address,cont_urls,cont_categories,contactnotes,fileName):
            ctc.printcontactsClass(contactprefix,contactphoneN, contactemail, contactaddresses, contacturls,contcategories,contactnotes,customerName)  
    return contactsId


###########################
#ORGANIZATIONS
###########################
def readOrganizations(path,sheetName,customerName,fileToRead):
        try:
            list={}
            contact_Id=""
            interface_Id=""
            org_erpCode=""
            
            vendors=faf.readFileToDataFrame(path)
            cont=0            
            for i, row in vendors.iterrows():
                tic = time.perf_counter()
                print(row[1]) # Print the cell|
                #print(vendors.iloc[i])
                #ORG CODE    
                if row[2]: org_code=row[2]
                #ORG NAME
                if row[1]: org_name=row[1]
                #print all column
                #print(vendors.iloc[[i],['ORGANIZATION NAME']])
                activeVendor= True
                #ORG DESCRIPTION
                orgdescription=""
                addorgdesc=True
                if addorgdesc==True: 
                    if row[8]:
                        orgdescription=row[8]
                #Organization language code
                orglanguage=""
                addlan = True 
                if addlan:
                    orglanguage=faf.org_languages("english")

                #ORG ALIASES#################
                orgaliases=[]
                addAli = True 
                if addAli:
                    orgaliases=""
                    #print(vendors.loc[i])
                    orgaliases=faf.org_aliases(vendors.loc[i],9)

                #Categories nn=blank
                orgCategoria="nn"
                
                #Addresses
                orgaddresses=[]
                addAdd= True
                concat=True
                if addAdd:
                    orgaddresses=""
                    orgaddresses=faf.org_addresses_utm(vendors.loc[i],10,18)

                #phoneNumbers
                addpho= True
                orgphonNumbers=[]
                if addpho:
                    orgphonNumbers=""
                    orgphonNumbers=faf.org_phoneNumbers(vendors.loc[i],26,30)

                #emails
                orgemails=[]
                addmails=True
                if addmails:
                    orgemails=""
                    orgemails=faf.org_emails(vendors.loc[i],34)

                #vendorCurrencies
                orgvendorCurrencies=["USD"]
                
                #urlsOrg
                orgurls=[]
                addurl=True
                if addurl:
                    orgurls=""
                    orgurls=faf.org_urls(vendors.loc[i],38)

                #accounts
                accounts=[]
                addacc=False
                if addacc:
                    accounts="" 
                    accounts=faf.org_account(vendors.loc[i],0)
                    
                #Acquisition Unit
                acqUnitIds= []
                addacc=False
                if addacc:
                    acqUnitIds=""
                    acqUnitIds=faf.org_acqunit(vendors.loc[i],0)

                interface_Id=[]
                addinterface= False
                if addinterface:
                    #readInterfacesSpreadsheet(idSearch,path,sheetName,customerName):
                    interface_Id=(readInterfacesSpreadsheet(row[0],path,"INTERFACES",customerName))

                contact_Id=[]
                addcontact= True
                isoncurrentsheet= True
                if addcontact:
                        #contact_Id=""
                        contact_=(readContactsSpreadsheet(row[0],path,"CONTACTS",customerName,43))
                        contact_Id.append(contact_)
                        contact_1=(readContactsSpreadsheet2(row[0],path,"CONTACTS",customerName,50))
                        contact_Id.append(contact_1)
                        print(contact_Id)
                #ORG UUID
                uuidOrg=str(uuid.uuid4())
                cont=cont+1
                org=faf.Organizations(uuidOrg,org_name,org_code,activeVendor,orglanguage)
                org.printorganizations(orgdescription,orgaliases,orgaddresses,orgphonNumbers,orgemails,orgurls,orgvendorCurrencies,contact_Id,interface_Id,org_erpCode,customerName)
                #NOTES
                addnoteapp=False
                if addnoteapp:
                    typeId="10bc689f-df06-4e6e-ac92-a91b38b1f8e6"
                    orgnote=faf.notes()
                    #print_notes(self,dfRow,typeId,linkId,fileName,*argv):
                    orgnote.print_notes(vendors.loc[i],typeId,uuidOrg,customerName,15,16,17,19)
                interface_Id=[]
                #old_org=org_code
                contact_Id=[]
                org_erpCode=""
                toc = time.perf_counter()
                print(f"Record: {cont} "+str(org_name)+f"  procesing time in {toc - tic:0.4f} seconds")
                
        except ValueError:
            print("Main Error: "+str(ValueError))


if __name__ == "__main__":
    """This is the Starting point for the script"""
    customerName="UTM"
    path_dir: str=r"UTM"
    content_dir: List[str] = os.listdir(path_dir)
    filename="OrganizationsforFOLIO042121.csv"
    path_file: str = path_dir + "/" + filename  
    typeFile=1 #1 spreadsheet, 2 CSV
    faf.exitfile(f"{path_dir}/{customerName}_interfaces.json")
    faf.exitfile(f"{path_dir}/{customerName}_contacts.json")
    faf.exitfile(f"{path_dir}/{customerName}_organizations.json")
    faf.exitfile(f"{path_dir}/{customerName}_credentials.json")
    faf.exitfile(f"{path_dir}/{customerName}_notes.json")
    readOrganizations(f"{path_dir}\{filename}","ORGANIZATIONS" ,customerName,typeFile)