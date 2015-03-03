# -*- coding: windows-1250 -*-

from tkinter import *
from bs4 import BeautifulSoup
import urllib.request




def replace(str):
    
    rep={'�':'%C8', '�':'%C6', '�':'%8E', '�':'%8A', '�':'%D0',}
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
        self.countrynames = ('ZAGREB GL. KOL.', 'ANDRIJA�EVCI', 'ANDRIJEVCI', 'ANTUNOVAC', 'BADLJEVINA', 'BAKOVI�I', 
'BANOVA JARUGA', 'BANJA', 'BEDEKOV�INA', 'BELAVI�I', 'BELI MANASTIR', 'BENKOVAC', 'BIBINJE', 'BIJELA', 'BIJELO BRDO', 
'BIZOVAC', 'BJELOVAR', 'BLACKO JAK�I�', 'BLATA', 'BLINJSKI KUT', 'BOROVO-TRPINJA', 'BORUT', 'BOTOVO', 'BO�JAKOVINA', 
'BRDA�CE', 'BRDOVEC', 'BR�ANI KRAJI�KI', 'BREGI', 'BREZINE BUJAVICA', 'BREZOVLJANI', 'BRGUD', 'BRIJEST', 
'BRLOG GRAD', 'BROD MORAVICE', 'BRODSKI STUPNIK', 'BR�ADIN', 'BR�ADIN LIPOVA�A', 'BUBNJARCI', 'BU�JE-KOPRIVNICA', 
'BUDIN��INA', 'BUDROVCI', 'BULI�', 'BUZET', 'CABUNA', 'CAREVDAR', 'CERA', 'CERJE TU�NO', 'CERNA', 'CEROVLJANI', 
'CEROVLJE', 'CIGLENIK', 'CIRKVENA', 'CRET', '�ABRUNI�I', '�ABRUNI�I SELO', '�A�INCI', '�AGLIN', '�AKOVEC', 
'�AKOVEC-BUZOVEC', '�EHOVEC', '�EMINAC', '�EPIN', '�UKOVEC', '�ULINEC', 'DABAR', 'DALMATIN. OSTROVICA', 'DALJ', 'DARDA', 
'DARUVAR', 'DEANOVEC', 'DEBELJAK', 'DELNICE', 'DESINEC', 'DOBROVAC', 'DOLI�E', 'DOMAGOVI�', 'DONJA STUBICA', 
'DONJA VRBA', 'DONJA VRIJESKA', 'DONJE DUBRAVE', 'DONJI DOLAC', 'DONJI KRALJEVEC', 'DONJI LIPOVEC', 
'DONJI MIHALJEVEC', 'DOPSIN', 'DRAGALI�', 'DRAGANI�I', 'DRAGOVCI', 'DRENOVCI', 'DRIVENIK', 'DRNI�', 'DRNJE', 
'DUBRAVA ZABO�KA', 'DUGA RESA', 'DUGO SELO', 'DUKOVEC', 'DUNJKOVEC', '�AKOVO', '�EVRSKE', '�ULOVAC', 
'�UR�ENOVAC', '�UR�EVAC', '�URMANEC', 'ERDUT', 'ERNESTINOVO', 'FERI�ANCI', 'FRIGIS', 'FU�INE', 
'GABOS', 'GAJNICE', 'GALI�ANA', 'GALOVCI', 'GAR�IN', 'GENERALSKI STOL', 'GOLUBOVEC', 'GOMIRJE', 
'GORNJA STUBICA', 'GORNJE DUBRAVE', 'GORNJI ZVE�AJ', 'GOSPI�', 'GRABO�TANI', 'GRA�AC', 'GRADEC', 
'GRADI�TE', 'GREDA', 'GRGINAC', 'GRGINAC NOVI', 'GUNJA', 'HARMICA', 'HEKI', 'HEKI TOVARI�TE', 
'HORVATI', 'HRASTOVAC', 'HRASTOVAC-VU�KI', 'HRA��INA-TRGOVI��E', 'HROMEC', 'HRSOVO', 'HRVATSKA DUBICA', 
'HRVATSKA KOSTAJNICA', 'HRVATSKI LESKOVAC', 'HUM LUG', 'HUM U ISTRI', 'ILA�A', 'ILOVA', 'IVANEC', 'IVANI� GRAD', 
'IVANKOVO', 'IVO�EVCI', 'JAL�ABET', 'JASENOVAC', 'JASTREBARSKO', 'JELISAVAC', 'JOSIPDOL', 'JOSIPOVAC', 
'JURDANI', 'JUR�I�I', 'JU�I�I', 'KALDRMA', 'KALINOVAC', 'KAMANJE', 'KANFANAR', 'KARLOVAC', 'KARLOVAC-CENTAR', 
'KA�TEL GOMILICA', 'KA�TEL KAMBELOVAC', 'KA�TEL STARI', 'KA�TEL SU�URAC', 'KISTANJE', 'KLOKO�EVAC', 'KLO�TAR', 
'KNE�CI', 'KNIN', 'KOMIN', 'KONJ��INA', 'KOPANICA-BERAVCI', 'KOPRIVNICA', 'KOPRNO', 'KORENI�ANI', 'KOSOVO', 
'KO�ARE', 'KO�KA', 'KOTORIBA', 'KO�LOVAC', 'KRAJCAR BRIJEG', 'KRAPINA', 'KRI�EVCI', 'KRNJEVO', 'KRU�LJEVEC', 
'KRVAVAC', 'KUKA�A', 'KUKUNJEVAC', 'KULA NORINSKA', 'KULJEV�ICA', 'KUNOVEC SUBOTICA', 'KUPJAK', 'KUPLJENOVO', 
'KUSTO�IJA', 'KUTI', 'KUTINA', 'LABIN DALMATINSKI', 'LADU�', 'LASLOVO-KORODJ', 'LATIN', 'LATINOVAC', 'LAZINA', 
'LEKENIK', 'LEPAVINA', 'LEPOGLAVA', 'LEPURI', 'LI�', 'LI�KA JESENICA', 'LI�KI PODHUM', 'LI�KO LE��E', 'LIPIK', 
'LIPOVAC-KORITNA', 'LIPOVLJANI', 'LOKVE', 'LOND�ICA', 'LOVINAC', 'LUDBREG', 'LUDINA', 'LUKA', 'LUPOGLAV', 
'LU�ANI-MALINO', 'LJESKOVICA', 'LJUBO�INA', 'MACINEC', 'MA�AREVO', 'MAHI�NO', 'MAJUR', 'MAJUREC', 'MAKSIMIR', 
'MALA SUBOTICA', 'MANDALINA', 'MARKUSICA-ANTIN', 'MARTIJANEC', 'MASLENJA�A', 'MAVRA�I�I', 'MEDAK', 'ME�URI�', 
'MEJA', 'MELNICE', 'METKOVI�', 'MIHALJEVCI', 'MIKLEU�', 'MIRKOVCI', 'MI�ULINOVAC', 'MORAVICE', 'MOSLAVA�KA GRA�ENICA', 
'MRACLIN', 'MRZLO POLJE', 'MU�NA REKA', 'MURSKO SREDI��E', 'NADIN', 'NA�ICE', 'NA�ICE GRAD', 'NA�I�KA BREZNICA', 
'NIZA', 'NORMANCI', 'NOVA BUKOVICA', 'NOVA GRADI�KA', 'NOVA KAPELA-BATRINA', 'NOVAKI', 'NOVAKOVEC', 'NOVI DALJ', 
'NOVI DVORI', 'NOVI MAROF', 'NOVIGRAD PODRAVSKI', 'NOVO SELO ROK', 'NOVOSELCI', 'NOVOSELEC', 'NOVSKA', 'NUGLA', 
'NU�TAR STAJALI�TE', 'O�ESTOVO', 'ODRA', 'OGULIN', 'OGULINSKI HRELJIN', 'OKU�ANI', 'OPATIJA-MATULJI', 'OPUZEN', 
'ORIOVAC', 'OROLIK', 'OROSLAVJE', 'OSIJEK', 'OSIJEK DONJI GRAD', 'OSIJEK DRAVSKI MOST', 'OSIJEK LUKA', 'OSIJEK OLT', 
'OSTRNA', 'OSTROVO', 'O�TARIJE', 'O�TARIJE RAVNICE', 'OTOK', 'OZALJ', 'PAKRAC', 'PAKRAC GRAD', 'PAPI�I', 'PAULOVAC', 
'PAZIN', 'P�ELI�', 'PEPELANA', 'PERKOVCI', 'PERKOVI�', 'PERMANI', 'PERU�I�', 'PE��ENICA', 'PETROVE GORE', 'PITOMA�A', 
'PIVNICA', 'PLANJANE', 'PLASE', 'PLA�KI', 'PLAV�A DRAGA', 'PLAVNO', 'PLETERNICA', 'PLO�E', 'PODRAVSKA BISTRICA', 
'PODRUTE', 'PODSUSED STAJALI�TE', 'PODSUSED TVORNICA', 'POJATNO', 'POLJANA', 'POLJANKA', 'POPOVA�A', 'POTO�ANI-KATINAC', 
'POZNANOVEC', 'PO�EGA', 'PRE�EC STAJALI�TE', 'PRESLO', 'PRGOMET', 'PRIMORSKI DOLAC', 'PRIMORSKI SV. JURAJ', 
'PRIMORSKO VRPOLJE', 'PRIVLAKA', 'PRISTAV-KRAPINSKI-ST', 'PRKOS', 'PULA', 'RADU�I�', 'RAJI�', 'RASINJA', 'RA�TEVI�', 
'RATKOVICA', 'RA�INE', 'REMETINEC', 'REPINEC', 'REPU�NICA', 'RIJEKA', 'RIPI�TE', 'RO�', 'RO�KO POLJE', 'ROGOTIN', 'ROKOVCI', 
'ROVI��E', 'RUDOPOLJE', 'RUKAVAC', 'SADINE', 'SAMATOVCI', 'SARVA�', 'SAVI�ENTA', 'SAVSKI MAROF', 'SEDRAMI�', 'SEMELJCI', 
'SESVETE', 'SESVETSKI KRALJEVEC', 'SIBINJ', 'SIKIREVCI', 'SIRA�', 'SIROVA KATALENA', 'SISAK', 'SISAK CAPRAG', 'SIVERI�', 
'SKRAD', 'SLADOJEVCI', 'SLAKOVCI', 'SLATINA', 'SLAVONSKI BROD', 'SLAVONSKI �AMAC', 'SLOBODNICA', 'SMOLJANCI', 'SOKOLOVAC', 
'SOLIN', 'SPA�VA', 'SPLIT', 'SPLIT PREDGRA�E', 'SREMSKE LAZE', 'STABLINA', 'STANDARD', 'STARA SUBOCKA', 'STARE PLAVNICE', 
'STARI MIKANOVCI', 'STARI SLATINIK', 'STARO PETROVO SELO', 'STARO TOPOLJE', 'STAZA', 'STA�NJEVEC', 'STRIZIVOJNA VRPOLJE', 
'STUBI�KE TOPLICE', 'STUPNO', 'SUHOPOLJE', 'SUKO�AN', 'SULKOVCI', 'SUNJA', 'SU�AK PE�INE', 'SUTLA', 'SV. IVAN �ABNO', 
'SV. KRI� ZA�RETJE', 'SVETI ILIJA', 'SVETI PETAR U �UMI', '�APJANE', '�A�', '�IBENIK', '�IDSKI BANOVCI', '�IJANA', 
'�IRINEC', '�KABRNJE', '�KODINOVAC', '�KRINJARI', '�KRLJEVO', '�OPOT', '�PI�KOVINA', '�PI�I� BUKOVICA', '�TRUCLJEVO', 
'�U�NJEVO SELO', 'TENJSKI-ANTUNOVAC', 'TEPLJUH', 'TOUNJ', 'TOVARNIK', 'TRENKOVO', 'TRNAVA', 'TUR�IN', 'TUROPOLJE', 
'UNE�I�', 'VARA�DIN', 'VELIKA', 'VELIKA GORICA', 'VELIKA VES', 'VELIKO TRGOVI��E', 'VELIKO TROJSTVO', 'VELIMIROVAC', 
'VIDOVEC', 'VINKOVA�KI BANOVCI', 'VINKOVA�KO NOVO SELO', 'VINKOVCI', 'VINKOVCI BOLNICA', 'VIRJE', 'VIROVITICA', 
'VIROVITICA GRAD', 'VI�KOVCI', 'VI�NJEVAC', 'VI�NJEVAC IPK', 'VI�NJICA', 'VLADISLAVCI', 'VODNJAN', 'VODNJAN STAJALI�TE', 
'VODOVOD', 'VO�INCI', 'VOJAKOVA�KI KLO�TAR', 'VOJNOVAC', 'VOLINJA', 'VOLODER', 'VRAP�E', 'VRATA', 'VRATI�INEC', 
'VRBANJA', 'VRBOVA', 'VRBOVEC', 'VRBOVSKO', 'VRHOVINE', 'VUJASINOVI�I', 'VUKOSAVLJEVICA', 'VUKOVAR', 'VUKOVAR-BOROVO NAS.', 
'VUKOVJE', 'ZABOK', 'ZADAR', 'ZADUBRAVLJE', 'ZAGREB GL. KOL.', 'ZAGREB KLARA', 'ZAGREB ZAP. KOL.', 'ZALESINA', 
'ZALUKA', 'ZAPOLJE', 'ZAPRE�I�', 'ZAPRE�I�-SAVSKA', 'ZARILAC', 'ZBELAVA', 'ZDENCI-ORAHOVICA', 'ZDEN�INA', 
'ZLATAR-BISTRICA', 'ZLOBIN', 'ZOLJAN', 'ZORKOVAC', 'ZRMANJA', 'ZVE�AJ', '�ABJAK', '�EINCI', '�ITNI�', '�IVAJA', 
'�MINJ', '�RNOVAC', '�UPANJA', '�UTNICA')
        
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

        