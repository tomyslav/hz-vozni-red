# -*- coding: windows-1250 -*-

from tkinter import *
from bs4 import BeautifulSoup
import urllib.request




def replace(str):
    
    rep={'Č':'%C8', 'Ć':'%C6', 'Ž':'%8E', 'Š':'%8A', 'Đ':'%D0',}
    if str!=None:
        for i,j in rep.items():
            str=str.replace(i, j)
    return str
    


#stgripping and substituting None type of data if needed
def stripped(data,sub=''):
    if data==None:
        data=sub
    else:
        data=data.strip()
        
    return data


#get trains that are leaving from destination, check are they late and thie final destination (if applicable)
def get_data_for_departing(depa,dest,d_or_a):
    des=dest
    dep=depa
    da=d_or_a
    if da=='D':
        t='TRAIN ID - DEPARTURE TIME - LATE - SRRIVING FROM \n'
    else:
        t='TRAIN ID - ARRIVAL TIME - LATE - DESTINATION \n'
    url='http://vred.hzinfra.hr/hzinfo/Default.asp?KO='+dep+'&Category=hzinfo&Service=PANO&LANG=HR&OD1='+da+'&SCREEN=2'
    all_trains=[]
    all_trains_return=[]
    all_trains_return.append(t)
    print(url)
    
    try:
        response=urllib.request.urlopen(url)
        html=response.read()
        b=BeautifulSoup(html)
        b=b.find_all('tr')
        
        print(t)
        
        
        all_trains.append(t)
        for i in b:
            x=i.find_all('td')
            train_id=x[0].a.string.strip()
            arrival=x[1].string.strip()
            late=stripped(x[2].string,'On Time')
            from_town=stripped(x[6].string)
            all_trains.append(train_id+' - '+arrival+' - '+late+' - '+from_town+'\n')
            
            print(train_id+' - '+arrival+' - '+late+' - '+from_town)
    except urllib.error.HTTPError:
        print('404 - page not found')
        all_trains.append('No trains found')
        
    
    if des!=None:
        for i in all_trains:
            if des in str(i):
                all_trains_return.append(i)
    else:
        all_trains_return=all_trains
    print(all_trains_return)

       
    return all_trains_return


class MainFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.countrynames = ('ZAGREB GL. KOL.', 'ANDRIJAŠEVCI', 'ANDRIJEVCI', 'ANTUNOVAC', 'BADLJEVINA', 'BAKOVIĆI', 
'BANOVA JARUGA', 'BANJA', 'BEDEKOVČINA', 'BELAVIĆI', 'BELI MANASTIR', 'BENKOVAC', 'BIBINJE', 'BIJELA', 'BIJELO BRDO', 
'BIZOVAC', 'BJELOVAR', 'BLACKO JAKŠIĆ', 'BLATA', 'BLINJSKI KUT', 'BOROVO-TRPINJA', 'BORUT', 'BOTOVO', 'BOŽJAKOVINA', 
'BRDAŠCE', 'BRDOVEC', 'BRĐANI KRAJIŠKI', 'BREGI', 'BREZINE BUJAVICA', 'BREZOVLJANI', 'BRGUD', 'BRIJEST', 
'BRLOG GRAD', 'BROD MORAVICE', 'BRODSKI STUPNIK', 'BRŠADIN', 'BRŠADIN LIPOVAČA', 'BUBNJARCI', 'BUČJE-KOPRIVNICA', 
'BUDINŠĆINA', 'BUDROVCI', 'BULIĆ', 'BUZET', 'CABUNA', 'CAREVDAR', 'CERA', 'CERJE TUŽNO', 'CERNA', 'CEROVLJANI', 
'CEROVLJE', 'CIGLENIK', 'CIRKVENA', 'CRET', 'ČABRUNIĆI', 'ČABRUNIĆI SELO', 'ČAČINCI', 'ČAGLIN', 'ČAKOVEC', 
'ČAKOVEC-BUZOVEC', 'ČEHOVEC', 'ČEMINAC', 'ČEPIN', 'ČUKOVEC', 'ČULINEC', 'DABAR', 'DALMATIN. OSTROVICA', 'DALJ', 'DARDA', 
'DARUVAR', 'DEANOVEC', 'DEBELJAK', 'DELNICE', 'DESINEC', 'DOBROVAC', 'DOLIĆE', 'DOMAGOVIĆ', 'DONJA STUBICA', 
'DONJA VRBA', 'DONJA VRIJESKA', 'DONJE DUBRAVE', 'DONJI DOLAC', 'DONJI KRALJEVEC', 'DONJI LIPOVEC', 
'DONJI MIHALJEVEC', 'DOPSIN', 'DRAGALIĆ', 'DRAGANIĆI', 'DRAGOVCI', 'DRENOVCI', 'DRIVENIK', 'DRNIŠ', 'DRNJE', 
'DUBRAVA ZABOČKA', 'DUGA RESA', 'DUGO SELO', 'DUKOVEC', 'DUNJKOVEC', 'ĐAKOVO', 'ĐEVRSKE', 'ĐULOVAC', 
'ĐURĐENOVAC', 'ĐURĐEVAC', 'ĐURMANEC', 'ERDUT', 'ERNESTINOVO', 'FERIČANCI', 'FRIGIS', 'FUŽINE', 
'GABOS', 'GAJNICE', 'GALIŽANA', 'GALOVCI', 'GARČIN', 'GENERALSKI STOL', 'GOLUBOVEC', 'GOMIRJE', 
'GORNJA STUBICA', 'GORNJE DUBRAVE', 'GORNJI ZVEČAJ', 'GOSPIĆ', 'GRABOŠTANI', 'GRAČAC', 'GRADEC', 
'GRADIŠTE', 'GREDA', 'GRGINAC', 'GRGINAC NOVI', 'GUNJA', 'HARMICA', 'HEKI', 'HEKI TOVARIŠTE', 
'HORVATI', 'HRASTOVAC', 'HRASTOVAC-VUČKI', 'HRAŠĆINA-TRGOVIŠĆE', 'HROMEC', 'HRSOVO', 'HRVATSKA DUBICA', 
'HRVATSKA KOSTAJNICA', 'HRVATSKI LESKOVAC', 'HUM LUG', 'HUM U ISTRI', 'ILAČA', 'ILOVA', 'IVANEC', 'IVANIĆ GRAD', 
'IVANKOVO', 'IVOŠEVCI', 'JALŽABET', 'JASENOVAC', 'JASTREBARSKO', 'JELISAVAC', 'JOSIPDOL', 'JOSIPOVAC', 
'JURDANI', 'JURŠIĆI', 'JUŠIĆI', 'KALDRMA', 'KALINOVAC', 'KAMANJE', 'KANFANAR', 'KARLOVAC', 'KARLOVAC-CENTAR', 
'KAŠTEL GOMILICA', 'KAŠTEL KAMBELOVAC', 'KAŠTEL STARI', 'KAŠTEL SUĆURAC', 'KISTANJE', 'KLOKOČEVAC', 'KLOŠTAR', 
'KNEŽCI', 'KNIN', 'KOMIN', 'KONJŠĆINA', 'KOPANICA-BERAVCI', 'KOPRIVNICA', 'KOPRNO', 'KORENIČANI', 'KOSOVO', 
'KOŠARE', 'KOŠKA', 'KOTORIBA', 'KOŽLOVAC', 'KRAJCAR BRIJEG', 'KRAPINA', 'KRIŽEVCI', 'KRNJEVO', 'KRUŠLJEVEC', 
'KRVAVAC', 'KUKAČA', 'KUKUNJEVAC', 'KULA NORINSKA', 'KULJEVČICA', 'KUNOVEC SUBOTICA', 'KUPJAK', 'KUPLJENOVO', 
'KUSTOŠIJA', 'KUTI', 'KUTINA', 'LABIN DALMATINSKI', 'LADUČ', 'LASLOVO-KORODJ', 'LATIN', 'LATINOVAC', 'LAZINA', 
'LEKENIK', 'LEPAVINA', 'LEPOGLAVA', 'LEPURI', 'LIČ', 'LIČKA JESENICA', 'LIČKI PODHUM', 'LIČKO LEŠĆE', 'LIPIK', 
'LIPOVAC-KORITNA', 'LIPOVLJANI', 'LOKVE', 'LONDŽICA', 'LOVINAC', 'LUDBREG', 'LUDINA', 'LUKA', 'LUPOGLAV', 
'LUŽANI-MALINO', 'LJESKOVICA', 'LJUBOŠINA', 'MACINEC', 'MAĐAREVO', 'MAHIČNO', 'MAJUR', 'MAJUREC', 'MAKSIMIR', 
'MALA SUBOTICA', 'MANDALINA', 'MARKUSICA-ANTIN', 'MARTIJANEC', 'MASLENJAČA', 'MAVRAČIĆI', 'MEDAK', 'MEĐURIĆ', 
'MEJA', 'MELNICE', 'METKOVIĆ', 'MIHALJEVCI', 'MIKLEUŠ', 'MIRKOVCI', 'MIŠULINOVAC', 'MORAVICE', 'MOSLAVAČKA GRAČENICA', 
'MRACLIN', 'MRZLO POLJE', 'MUČNA REKA', 'MURSKO SREDIŠĆE', 'NADIN', 'NAŠICE', 'NAŠICE GRAD', 'NAŠIČKA BREZNICA', 
'NIZA', 'NORMANCI', 'NOVA BUKOVICA', 'NOVA GRADIŠKA', 'NOVA KAPELA-BATRINA', 'NOVAKI', 'NOVAKOVEC', 'NOVI DALJ', 
'NOVI DVORI', 'NOVI MAROF', 'NOVIGRAD PODRAVSKI', 'NOVO SELO ROK', 'NOVOSELCI', 'NOVOSELEC', 'NOVSKA', 'NUGLA', 
'NUŠTAR STAJALIŠTE', 'OĆESTOVO', 'ODRA', 'OGULIN', 'OGULINSKI HRELJIN', 'OKUČANI', 'OPATIJA-MATULJI', 'OPUZEN', 
'ORIOVAC', 'OROLIK', 'OROSLAVJE', 'OSIJEK', 'OSIJEK DONJI GRAD', 'OSIJEK DRAVSKI MOST', 'OSIJEK LUKA', 'OSIJEK OLT', 
'OSTRNA', 'OSTROVO', 'OŠTARIJE', 'OŠTARIJE RAVNICE', 'OTOK', 'OZALJ', 'PAKRAC', 'PAKRAC GRAD', 'PAPIĆI', 'PAULOVAC', 
'PAZIN', 'PČELIĆ', 'PEPELANA', 'PERKOVCI', 'PERKOVIĆ', 'PERMANI', 'PERUŠIĆ', 'PEŠĆENICA', 'PETROVE GORE', 'PITOMAČA', 
'PIVNICA', 'PLANJANE', 'PLASE', 'PLAŠKI', 'PLAVČA DRAGA', 'PLAVNO', 'PLETERNICA', 'PLOČE', 'PODRAVSKA BISTRICA', 
'PODRUTE', 'PODSUSED STAJALIŠTE', 'PODSUSED TVORNICA', 'POJATNO', 'POLJANA', 'POLJANKA', 'POPOVAČA', 'POTOČANI-KATINAC', 
'POZNANOVEC', 'POŽEGA', 'PREČEC STAJALIŠTE', 'PRESLO', 'PRGOMET', 'PRIMORSKI DOLAC', 'PRIMORSKI SV. JURAJ', 
'PRIMORSKO VRPOLJE', 'PRIVLAKA', 'PRISTAV-KRAPINSKI-ST', 'PRKOS', 'PULA', 'RADUČIĆ', 'RAJIĆ', 'RASINJA', 'RAŠTEVIĆ', 
'RATKOVICA', 'RAŽINE', 'REMETINEC', 'REPINEC', 'REPUŠNICA', 'RIJEKA', 'RIPIŠTE', 'ROČ', 'ROČKO POLJE', 'ROGOTIN', 'ROKOVCI', 
'ROVIŠĆE', 'RUDOPOLJE', 'RUKAVAC', 'SADINE', 'SAMATOVCI', 'SARVAŠ', 'SAVIČENTA', 'SAVSKI MAROF', 'SEDRAMIĆ', 'SEMELJCI', 
'SESVETE', 'SESVETSKI KRALJEVEC', 'SIBINJ', 'SIKIREVCI', 'SIRAČ', 'SIROVA KATALENA', 'SISAK', 'SISAK CAPRAG', 'SIVERIĆ', 
'SKRAD', 'SLADOJEVCI', 'SLAKOVCI', 'SLATINA', 'SLAVONSKI BROD', 'SLAVONSKI ŠAMAC', 'SLOBODNICA', 'SMOLJANCI', 'SOKOLOVAC', 
'SOLIN', 'SPAČVA', 'SPLIT', 'SPLIT PREDGRAĐE', 'SREMSKE LAZE', 'STABLINA', 'STANDARD', 'STARA SUBOCKA', 'STARE PLAVNICE', 
'STARI MIKANOVCI', 'STARI SLATINIK', 'STARO PETROVO SELO', 'STARO TOPOLJE', 'STAZA', 'STAŽNJEVEC', 'STRIZIVOJNA VRPOLJE', 
'STUBIČKE TOPLICE', 'STUPNO', 'SUHOPOLJE', 'SUKOŠAN', 'SULKOVCI', 'SUNJA', 'SUŠAK PEĆINE', 'SUTLA', 'SV. IVAN ŽABNO', 
'SV. KRIŽ ZAČRETJE', 'SVETI ILIJA', 'SVETI PETAR U ŠUMI', 'ŠAPJANE', 'ŠAŠ', 'ŠIBENIK', 'ŠIDSKI BANOVCI', 'ŠIJANA', 
'ŠIRINEC', 'ŠKABRNJE', 'ŠKODINOVAC', 'ŠKRINJARI', 'ŠKRLJEVO', 'ŠOPOT', 'ŠPIČKOVINA', 'ŠPIŠIĆ BUKOVICA', 'ŠTRUCLJEVO', 
'ŠUŠNJEVO SELO', 'TENJSKI-ANTUNOVAC', 'TEPLJUH', 'TOUNJ', 'TOVARNIK', 'TRENKOVO', 'TRNAVA', 'TURČIN', 'TUROPOLJE', 
'UNEŠIĆ', 'VARAŽDIN', 'VELIKA', 'VELIKA GORICA', 'VELIKA VES', 'VELIKO TRGOVIŠĆE', 'VELIKO TROJSTVO', 'VELIMIROVAC', 
'VIDOVEC', 'VINKOVAČKI BANOVCI', 'VINKOVAČKO NOVO SELO', 'VINKOVCI', 'VINKOVCI BOLNICA', 'VIRJE', 'VIROVITICA', 
'VIROVITICA GRAD', 'VIŠKOVCI', 'VIŠNJEVAC', 'VIŠNJEVAC IPK', 'VIŠNJICA', 'VLADISLAVCI', 'VODNJAN', 'VODNJAN STAJALIŠTE', 
'VODOVOD', 'VOĐINCI', 'VOJAKOVAČKI KLOŠTAR', 'VOJNOVAC', 'VOLINJA', 'VOLODER', 'VRAPČE', 'VRATA', 'VRATIŠINEC', 
'VRBANJA', 'VRBOVA', 'VRBOVEC', 'VRBOVSKO', 'VRHOVINE', 'VUJASINOVIĆI', 'VUKOSAVLJEVICA', 'VUKOVAR', 'VUKOVAR-BOROVO NAS.', 
'VUKOVJE', 'ZABOK', 'ZADAR', 'ZADUBRAVLJE', 'ZAGREB GL. KOL.', 'ZAGREB KLARA', 'ZAGREB ZAP. KOL.', 'ZALESINA', 
'ZALUKA', 'ZAPOLJE', 'ZAPREŠIĆ', 'ZAPREŠIĆ-SAVSKA', 'ZARILAC', 'ZBELAVA', 'ZDENCI-ORAHOVICA', 'ZDENČINA', 
'ZLATAR-BISTRICA', 'ZLOBIN', 'ZOLJAN', 'ZORKOVAC', 'ZRMANJA', 'ZVEČAJ', 'ŽABJAK', 'ŽEINCI', 'ŽITNIĆ', 'ŽIVAJA', 
'ŽMINJ', 'ŽRNOVAC', 'ŽUPANJA', 'ŽUTNICA')
        
        self.cnames = StringVar(value=self.countrynames)
        
        self.countrynames2 = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland', 'Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
        self.cnames2 = StringVar(value=self.countrynames)
        
        self.GUI()
    

    def GUI(self):
        
        #first frame with first listbox and scrollbar
        self.departureFrame=Frame(self,bg='red')
        self.departureFrame.grid(row=0,column=0)
        self.departureLabel=Label(self.departureFrame,text='FROM:')
        self.departureLabel.grid(row=0,column=0)
        self.departureBox=Listbox(self.departureFrame,height=25,selectmode=SINGLE,listvariable=self.cnames,exportselection=0)
        self.departureBox.grid(row=1,column=0)
        self.departureScroll=Scrollbar(self.departureFrame)
        self.departureScroll.grid(row=1,column=5,sticky='ns')
        self.departureScroll.config(command=self.departureBox.yview)
        
        self.departureBox.config(yscrollcommand=self.departureScroll.set)
               
               
        #second frame with second listbox and scrollbar      
        self.arrivalFrame=Frame(self,bg='blue')
        self.arrivalFrame.grid(row=0,column=6)
        self.arrivalLabel=Label(self.arrivalFrame,text='TO:')
        self.arrivalLabel.grid(row=0,column=6)
        self.arrivalBox=Listbox(self.arrivalFrame,height=25,selectmode=SINGLE,listvariable=self.cnames2,exportselection=0)
        self.arrivalBox.grid(row=1,column=6)
        self.arrivalScroll=Scrollbar(self.arrivalFrame)
        self.arrivalScroll.grid(row=1,column=10,sticky='ns')
        self.arrivalScroll.config(command=self.arrivalBox.yview)
        
        self.arrivalBox.config(yscrollcommand=self.arrivalScroll.set)
        
        #third frame with buttons
        self.buttonFrame=Frame(self,bg='green')
        self.buttonFrame.grid(row=0,column=15)
        self.arrivalButton=Button(self.buttonFrame,text='Get time of arriving trains \nand their destination')
        self.arrivalButton.grid(row=0,column=16)
        self.arrivalButton.config(command=lambda:self.GetData('D'))
        self.departureButton=Button(self.buttonFrame,text='Get times of departing Trains \nand their destinations')
        self.departureButton.config(command=lambda:self.GetData('O'))
        self.departureButton.grid(row=1,column=16)


        #fourth frame with label and text
        self.textFrame=Frame(self)
        self.textFrame.grid(row=0,column=20)
        
        self.textLabel=Label(self.textFrame,text='where and when')
        self.textLabel.grid(row=0,column=21)
        
        self.textBox=Text(self.textFrame)
        self.textBox.config(width=50)
        self.textBox.grid(row=1,column=21)
        
        #text
    
    
    def GetDestinations(self):
        pass
    
    
    def GetData(self,d):

        self.d_or_a=d
        #d_or_a decides do we want to se departing trains or trains that are arriving
        
        
        self.textBox.delete('1.0', END)
        
        try: 
            #selected departure 
            self.curDeparInd=self.departureBox.curselection()[0]
            self.curDepar=self.departureBox.get(self.curDeparInd)
            
            self.textBox.insert(END,self.curDepar+'\n') 
        except IndexError:
            self.textBox.insert(END,'departure not selected')   
            self.curDepar=None
            
            
        
        
        try:    
            self.curArrInd=self.arrivalBox.curselection()[0]
            self.curArr=self.arrivalBox.get(self.curArrInd)      
            #self.textBox.delete('1.0', END)
            self.textBox.insert(END, self.curArr+'\n')
        except IndexError:    
            #self.textBox.delete('1.0', END)
            self.textBox.insert(END, 'Arrival not selected \n')
            self.curArr=None
            
        except IndexError:
            #self.textBox.delete('1.0', END)
            self.textBox.insert(END, 'Did you selected both trains?')

        
     
        dta=get_data_for_departing(replace(self.curDepar), replace(self.curArr),self.d_or_a)

        for i in dta:
            self.textBox.insert(END, i)
        

def main(): 
    root=Tk()
    mf=MainFrame(root)
    root.geometry('800x600')
    mf.grid(row=0,column=0)
    mf.mainloop()

main()

        