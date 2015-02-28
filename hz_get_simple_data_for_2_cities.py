from bs4 import BeautifulSoup
import urllib.request


towns={1:'Zagreb+Gl.+Kol.',2:'OGULIN',}

#default is Zagreb if no data is entered
i_key=1

def stripped(data,sub=''):
    if data==None:
        data=sub
    else:
        data=data.strip()
        
    return data
    

def get_data(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    b=BeautifulSoup(html)
    
    b=b.find_all('tr')
    
    print('TRAIN ID - ARRIVAL TIME - LATE - DESTINATION')
    
    for i in b:
        x=i.find_all('td')
        train_id=x[0].a.string.strip()
        
        arrival=x[1].string.strip()
        
        late=stripped(x[2].string,'On Time')
        
        
        from_town=stripped(x[6].string)
        print(train_id+' - '+arrival+' - '+late+' - '+from_town)
        


inpt=input('Select number for city: \n1-Zagreb\n2-Ogulin\n:')


if inpt.strip()!='':
    i_key=int(inpt)



if (inpt.strip()!='') and (i_key in towns):
    url='http://vred.hzinfra.hr/hzinfo/Default.asp?KO='+towns[i_key]+'&Category=hzinfo&Service=PANO&LANG=HR&OD1=D&SCREEN=2'
    print('Selected city: '+towns[i_key])
else:
    print('You have provided wrong input. Showing trains for Zagreb')
    url='http://vred.hzinfra.hr/hzinfo/Default.asp?KO='+towns[i_key]+'&Category=hzinfo&Service=PANO&LANG=HR&OD1=D&SCREEN=2'




get_data(url)







