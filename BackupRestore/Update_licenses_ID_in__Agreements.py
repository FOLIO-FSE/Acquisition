import argparse
import pathlib
import json
import requests
import sys


def search(code_search):
    pass
    idlicense=""
    with open("licenses_cornell_ebsco.json",'r',encoding = 'utf-8') as h:
        for lineh in h:
            if (lineh.find(code_search) != -1):
                #print(lineh)
                foundc=True
                if (foundc):
                    pass
                    idlicense=lineh[8:44]
                    break
                else:
                    pass
    return idlicense


def search_newid(code_search):
    pass
    idlicense=""
    with open("licenses_cornell_ebsco.json",'r',encoding = 'utf-8') as h:
        for lineh in h:
            if (lineh.find(code_search) != -1):
                #print(lineh)
                foundc=True
                if (foundc):
                    pass
                    idlicense=lineh[8:44]
                    break
                else:
                    pass
    return idlicense


def main():
    linea_nueva={}
    
    new_file=open('agreement_new.json','w') #file to create
    log_file=open('LOG_agreement_new.json','w') #file to create
    print("iniciando la busqueda en el archivo Agreements_modified")
    log_file.write("iniciando la busqueda en el archivo Agreements_modified")
    cont=0
    with open("agreements_modified_2.json",'r',encoding = 'utf-8') as f: #cornell con remoteId old
        for line in f:
            linea_nueva=json.loads(line)
            #print(json.dumps(linea_nueva,indent=2))
            #print(linea_nueva['id'])
            #linea_nueva['linkedLicenses'][0]['status']['id']
            #linea_nueva['linkedLicenses'][0]['status']['id']
            #linea_nueva['linkedLicenses'][0]['remoteId']
            #print(linea_nueva['linkedLicenses'][0]['owner']['id'])
            #print(linea_nueva['periods'][0]['owner']['id'])
            #print(linea_nueva['orgs'][1]['owner']['id'])
            #print(linea_nueva['orgs'][1]['owner']['id'])
            #print(linea_nueva['currentPeriod']['owner']['id'])
            #linea_nueva=linea_nueva.replace("''","""")
            print("iniciando registro ",cont)
            #val=str(cont)
            #log_file.write("iniciando registro"+val)
            #log_file.write("iniciando registro,"+cont)
            if (line.find('historyLines') != -1):
                inicio=line.find('historyLines')
                foundA=True
                if (foundA):
                    print("Encontré HISTORYLINES reg:",cont)
                    log_file.write("Encontré HISTORYLINES reg:"+str(cont))
                    if (line.find('orgs') != -1):
                        foundB=True
                        if (foundB):
                            print("Encontré  ORGS en registro:",cont)
                            val=str(cont)
                        
                            log_file.write("Encontré ORGS en registro"+val)
                            Fin=line.find('orgs')                            
                            license_name=line[inicio+27:Fin-3]
                            print("iniciaré la busqueda de la licencia: ",license_name)
                            idlic=search(license_name)
                            if (idlic):#encontró
                               print("encontré el id para la licencia: "+license_name+" el nuevo Id  de la licencia es: "+idlic)
                               if (line.find('remoteId') != -1):
                                   rini=line.find('remoteId')
                                   remoteid=line[rini+12:rini+48]
                                   print("el id a cambiar es:", remoteid)
                                   print("Original registro ",line)                                   
                                   del linea_nueva["id"]
                                   if 'items' in linea_nueva:
                                       del linea_nueva["items"]
                                   #linea_nueva['linkedLicenses'][0]['id']=""
                                   #linea_nueva['periods'][1]['id']=""
                                   linea_nueva['linkedLicenses'][0]['remoteId']=idlic                                   
                                   linea_nueva['linkedLicenses'][0]['status']['id']=""
                                   #linea_nueva['linkedLicenses'][0]['id']=""
                                   #linea_nueva['linkedLicenses'][0]['id']=""
                                   #linea_nueva['linkedLicenses'][0]['id']=""
                                   #urlori=linea_nueva['linkedLicenses'][0][remoteId_object]['docs'][0]['url']    
                                   #nameori=linea_nueva['linkedLicenses'][0]['name']
                                   #orgori=linea_nueva['orgs'][0]['org']['orgsUuid']
                                   #perstartori=linea_nueva['periods'][0]['startDate']
                                   #pernoteori=linea_nueva['periods'][0]['note']

                                   #nameori=linea_nueva['name']
                                    #datos={                                       
                                       #"contacts":[],
                                       #"tags":[],
                                       #"inwardRelationships": [],
                                       #"linkedLicenses": [{"amendments" : [],"remoteId" : idlic,}],
                                       #"docs" : [],
                                       #"items" : [],
                                       #"periods" :[{"startDate":perstartori,"note":pernoteori}],
                                       #"historyLines" : [],
                                       #"name" : nameori,
                                       #"orgs" : [{"id": "", "org":{"id":"","orgsUuid":orgori}}],
                                       #"_links" : {"linkedResources": {"href" : "/licenses/licenseLinks?filter=owner.id%"}},
                                       #"status" : {"value":"active", "label":"Active"},
                                       #"usageDataProviders" : [],
                                       #"supplementaryDocs" :[],
                                       #"outwardRelationships" :[],
                                       #"externalLicenseDocs" :[],
                                       #"currentPeriod": "Null,
                                       #"startDate": Null,
                                       #"endDate": Null, 
                                       #"cancellationDeadline": null, 
                                       #}
                                   
                                   print(json.dumps(linea_nueva,indent=2))
                                   str_json=json.dumps(linea_nueva)
                                   print("En el archivo agreements modified tiene el id",remoteid,"se debe cambiar por", idlic)
                                   #linea_nueva=linea_nueva.replace(idlic,remoteid)
                                   #print("se modificó")
                                   new_file.write(str_json+"\n")
                                   print(linea_nueva)
                                   pass
                            else:
                                pass
                                #linea_nueva['linkedLicenses'][0]['remoteId']=idlic
                                #linea_nueva['linkedLicenses'][0]['status']['id']=""
                                del linea_nueva["id"]
                                if 'items' in linea_nueva:
                                       del linea_nueva["items"]
                                print("no encontro: ", line[1:56])
                                log_file.write("sin licencia: "+line[1:56])
                                print(json.dumps(linea_nueva,indent=2))
                                str_json=json.dumps(linea_nueva)
                                new_file.write(str_json+"\n")
                        else:  
                            
                            #linea_nueva['linkedLicenses'][0]['remoteId']=idlic
                            linea_nueva['linkedLicenses'][0]['status']['id']=""
                            if 'items' in linea_nueva:
                                       del linea_nueva["items"]
                            print("no se encontro org: ", line[1:56])
                            log_file.write("sin licencia: "+line[1:56])
                            log_file.write("sin licencia: "+line[1:56])
                            print(json.dumps(linea_nueva,indent=2))
                            str_json=json.dumps(linea_nueva)
                            new_file.write(str_json+"\n")
                else:
                    print("no se encontró")
                    print(json.dumps(linea_nueva,indent=2))
                    str_json=json.dumps(linea_nueva)
                    #cont=+1
                
                
                        #with open("licenses_cornell_ebsco.json",'r',encoding = 'utf-8') as cor:
                        #    for line_cor in cor:
                        #        if (line_cor.find(remoteIdtofind) != -1):
                        #            s=line.find('remoteId')
                        #            remoteId=line_cor[s+12:s+48]

            #string.replace("geeks", "Geeks"))  
            #print(line, end = '')
            #new_file.write(line)
    


if __name__ == "__main__":
    """This is the Starting point for the script"""
    main()

