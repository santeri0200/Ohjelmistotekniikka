import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_toimii_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_riittaa_edullisesti(self):
        self.assertEqual(500 - 240, self.kassapaate.syo_edullisesti_kateisella(500))

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_riittaa_maukkaasti(self):
        self.assertEqual(500 - 400, self.kassapaate.syo_maukkaasti_kateisella(500))

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_ei_riita_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_ei_riita_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_riittaa_edullisesti(self):
        maksukortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(maksukortti))

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_riittaa_maukkaasti(self):
        maksukortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_ei_riita_edullisesti(self):
        maksukortti = Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_riita_maukkaasti(self):
        maksukortti = Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_kassa_ei_tayty_kortilla(self):
        maksukortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(maksukortti))

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortti_ottaa(self):
        maksukortti = Maksukortti(500)

        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(maksukortti.saldo_euroina(), 10.00)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.00)
