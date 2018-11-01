import unittest
import d3q4 as f

class MyTest(unittest.TestCase):
    def test_prepare_paquet(self):
        self.assertEqual(f.prepare_paquet(13), [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413])
        self.assertEqual(f.prepare_paquet(4), [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404])
    
    def test_shuffle_paquet(self):
        pass # should test shuffle deck (how?)

    def test_donne_cartes_initiales(self):
        p = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(f.donne_cartes_initiales(p), [3,4,5,6,7,8,9])

    def test_donne_nouvelles_cartes(self):
        paquet=[201, 303, 210, 407, 213, 313]
        joueur=[302, 304, 404]
        f.donne_nouvelles_cartes(paquet, joueur, 4)
        self.assertEqual(joueur, [302, 304, 404, 313, 213, 407, 210])
        self.assertEqual(paquet, [201, 303])

        paquet=[201, 303]
        joueur=[302, 304, 404]
        f.donne_nouvelles_cartes(paquet, joueur, 4)
        self.assertEqual(joueur, [302, 304, 404, 303, 201])
        self.assertEqual(paquet, [])

    def test_print_paquet_deux_fois(self):
        pass # need to test output (should be working)

    def test_est_valide(self):
        self.assertEqual(f.est_valide([210,310],[201, 201, 210, 302, 311]), False)
        self.assertEqual(f.est_valide([210,310],[201, 201, 210, 302, 310, 401]), True)

    def test_est_valide_meme_valeur(self):
        self.assertEqual(f.est_valide_meme_valeur([207, 107, 407]), True)
        self.assertEqual(f.est_valide_meme_valeur([207]), False)

    def test_est_valide_seq(self):
        self.assertEqual(f.est_valide_seq([313, 311, 312]), True)
        self.assertEqual(f.est_valide_seq([311, 312, 313, 414]), False)
        self.assertEqual(f.est_valide_seq([201, 202]), False)
        self.assertEqual(f.est_valide_seq([]), False)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
