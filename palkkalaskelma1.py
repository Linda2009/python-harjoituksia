
    """
    Palkkalaskelma on lain mukaan vapaamuotoinen, mutta siitä pitää ilmetä ainakin seuraavat tiedot tässä koodissa:
    -bruttopalkka
    -työntekijoiden etunimi-sukunimi.
    -työntekijältä peritty työntekijän eläkemaksu ja työttömyysvakuutusmaksu.
    - ennakonpidätyksen_ lainen osa korvauksesta. 
    lopussa lasketaan nettopalkka
   
    """

class tyontekijoiden_palkka:

    def __init__(self, etunimi:str, sukunimi:str, tyontunti_maara_viikossa:int, palkka_tunnissa:float):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.tyontunti_maara_viikossa= tyontunti_maara_viikossa
        self.palkka_tunnissa = palkka_tunnissa
    def tulosta_nimi(self):
        print(self.etunimi, self.sukunimi,self.tyontunti_maara_viikossa, self.palkka_tunnissa)
#x = tyontekijoiden_palkka("Matti", "Laitinen", 25 , 15.25)
#x.tulosta_nimi()
class rakentajan_tuntipalkka(tyontekijoiden_palkka):
    def __init__(self, etunimi:str, sukunimi:str, tyontunti_maara_viikossa:int, palkka_tunnissa:float, 
                tyoajanlyhennys_prosenttina:float, ennakonpidatys_prosenttina:float,
                tyoelakemaksu_prosenttina=float, tyottomyys_vakuutusmaksu_prosenttina= float):
        
        super().__init__(etunimi, sukunimi, tyontunti_maara_viikossa, palkka_tunnissa)
       
        self.tyoajanlyhennys_prosenttina = tyoajanlyhennys_prosenttina
        self.ennakonpidatys_prosenttina = ennakonpidatys_prosenttina
        self.tyoelakemaksu_prosenttina = tyoelakemaksu_prosenttina
        self.tyottomyys_vakuutusmaksu_prosenttina = tyottomyys_vakuutusmaksu_prosenttina
    def netto_viikossa(self):
        brutto_viikon_palkka = self.tyontunti_maara_viikossa * self.palkka_tunnissa
        #print('brutto_viikon_palkka on:',round(brutto_viikon_palkka,2))
        tyoajanlyhennyskorvaus =  brutto_viikon_palkka * (self.tyoajanlyhennys_prosenttina * 0.01)
        #print('tyoajanlyhennyskorvaus on:' ,round(tyoajanlyhennyskorvaus,2))
        ennakonpidätyksen_alainen_osa_korvauksesta = brutto_viikon_palkka + tyoajanlyhennyskorvaus
        #print('ennakonpidätyksen_alainen_osa_korvauksesta:', round(ennakonpidätyksen_alainen_osa_korvauksesta,2))
        ennakonpidatys = ennakonpidätyksen_alainen_osa_korvauksesta * (self.ennakonpidatys_prosenttina * 0.01)
        #print('ennakonpidatys:', round(ennakonpidatys,2))
        tyoelakemaksu = ennakonpidätyksen_alainen_osa_korvauksesta * (self.tyoelakemaksu_prosenttina * 0.01)
        #print('tyoelakemaksu: ',round(tyoelakemaksu,2))
        tyottomyys_vakuutusmaksu = ennakonpidätyksen_alainen_osa_korvauksesta * (self.tyottomyys_vakuutusmaksu_prosenttina * 0.01)
        #print('tyottomyys_vakuutusmaksu:', round(tyottomyys_vakuutusmaksu,2))

        net_palkka = ennakonpidätyksen_alainen_osa_korvauksesta - ennakonpidatys- tyoelakemaksu - tyottomyys_vakuutusmaksu
        return net_palkka

#rakentajan_tuntipalkka1= rakentajan_tuntipalkka(etunimi= 'Matti', sukunimi = 'Laitinen' ,
                        #tyontunti_maara_viikossa= 87, palkka_tunnissa= 15.25, tyoajanlyhennys_prosenttina = 7.7,
                        #ennakonpidatys_prosenttina = 16, tyoelakemaksu_prosenttina = 8.25 , tyottomyys_vakuutusmaksu_prosenttina = 1.5)       
    
#rakentajan_tuntipalkka1.tulosta_nimi()
#print(rakentajan_tuntipalkka1.tyontunti_maara_viikossa)
#print(rakentajan_tuntipalkka1.palkka_tunnissa)
#print('rakentajan nettopalkka:', round(rakentajan_tuntipalkka1.netto_viikossa(),2))



import unittest
class SimpleTest(unittest.TestCase):
# Returns true if the string is stripped and
# matches the given output.
    def test_strip(self):
        rakentajan_tuntipalkka1= rakentajan_tuntipalkka(etunimi= 'Matti', sukunimi = 'Laitinen' ,
                        tyontunti_maara_viikossa= 87, palkka_tunnissa= 15.25, tyoajanlyhennys_prosenttina = 7.7,
                        ennakonpidatys_prosenttina = 16, tyoelakemaksu_prosenttina = 8.25 , tyottomyys_vakuutusmaksu_prosenttina = 1.5)
    
        a= rakentajan_tuntipalkka1.netto_viikossa()
        #self.assertEqual(rakentajan_tuntipalkka1.netto_viikossa(),12500)
        #self.assertEqual(('%.2f' % a),12500)
        self.assertEqual(('%.2f' % a),1060.97)
        #self.assertEqual((a),1060.965489375)

if __name__ == '__main__':
    unittest.main()   
