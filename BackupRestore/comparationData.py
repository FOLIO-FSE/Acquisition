import json
import uuid
import xlrd
import os
import xlwt
import xlsxwriter
import openpyxl
import os.path
import datetime
from datetime import datetime
import requests
import csv
import io

def get_OrgId(orgname):
        dic={}
        search=orgname
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        pathPattern="/organizations/organizations" #?limit=9999&query=code="
        okapi_url="https://okapi-cornell-test.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJfaWQiOiI5NjRlMGM5NS1iNjcxLTQ3OWItYmZmOC1mYTRkNzA1NzMwMWYiLCJpYXQiOjE2MTIxODY4MzEsInRlbmFudCI6ImZzMDAwMDEwMzQifQ.FyzUBRVpE5rh_9hIfYw-Z1-StwuBd3ubKqEMQ1nPuvY"
        okapi_tenant="fs00001034"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="organizations"
        query=f"query=name=="
        #/organizations-storage/organizations?query=code==UMPROQ
        paging_q = f"?{query}"+'"'+f"{search}"+'"'
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idorg=[]
        if (req.status_code != 201): 
            if (req.status_code != 400):
                json_str = json.loads(req.text)
                total_recs = int(json_str["totalRecords"])
                if (total_recs!=0):
                    rec=json_str[element]
                    #print(rec)
                    l=rec[0]
                    if 'id' in l:
                        idorg.append(l['name'])
                        #idorg.append(l['name'])
            else:
                idorg="0"
        return idorg
#END

if __name__ == "__main__":
    
    """This is the Starting point for the script"""
    dic=[]
    l = open ('du_vendedores.txt','w')
    f = open("cornell_pn_organizations.json",)
    data = json.load(f)
    count=0
    for i in data['organizations']:
        count+=1
        print("Record: "+str(count))
        a_line=str(i)
        org=i['name']
        alex=get_OrgId(org)
        if len(alex)>0:
            print(alex)
            l.write(str(alex)+"\n")
    f.close()
    l.close()
            #get_OrgId(orgname)