import unittest
from unittest.mock import patch
import main

class TestDNAInverter(unittest.TestCase):

    def test_inverter(self):
        """Test converting DNA to reverse complement"""
        dna = 'AGACCTTGATTCGTGCTGTTTCTTCTCCTCAA'
        expected = 'TTGAGGAGAAGAAACAGCACGAATCAAGGTCT'
        
        actual = main.invert_dna(dna)  
        self.assertEqual(actual, expected)

class TestPAMFinder(unittest.TestCase):

    @patch('main.get_dna') 
    def test_find_pams(self, mock_get_dna):  
        """Test finding PAM sites in sequence""" 
        
        mock_dna = "TACTATTAGCTGAATTGCCACTGCTATCGTTGTTAGTGGCGTTAGTGCTTGCATTCAAAGACATGGAGGGCGTTATTACGCCGGAGCTCCTCGACAGCAGATCTGATGACTGGTCAATATATTTTTGCATTGAGGCTCTGTTTGGAATTATATTTTGAGATGACCCATCTAATGTACTGGTATCACCAGATTTCATGTCGTTTTTTAAAGCGGCTGCTTGAGTCTTAGCAATAGCGTCACCATCTGGTGAATCCTTTGAAGGAACCACTGACGAAGGTTTGGACAGTGACGAAGAGGATCTTTCCTGCTTTGAATTAGTCGCGCTGGGAGCAGATGACGAGTTGGTGGAGCTGGGGGCAGGATTGCTGGCCGTCGTGGGTCCTGAATGGGTCCTTGGCTGGTCCATCTCTATTCTGAAAACGGAAGAGGAGTAGGGAATATTACTGGCTGAAAATAAGTCTTGAATGAACGTATACGCGTATATTTCTACCAATCTCTCAACACTGAGTAATGGTAGTTATAAGAAAGAGACCGAGTTAGGGACAGTTAGAGGCGGTGGAGATATTCCTTATGGCATGTCTGGCGATGATAAAACTTTTCAAACGGCAGCCCCGATCTAAAAGAGCTGACAGGGAAATGGTCAGAAAAAGAAACGTGCACCCGCCCGTCTGGACGCGCCGCTCACCCGCACGGCAGAGACCAATCAGTAAAAATCAACGGTTAACGACATTACTATATATATAATATAGGAAGCATTTAATAGAACAGCATCGTAATATATGTGTACTTTGCAGTTATGACGCCAGATGGCAGTAGTGGAAGATATTCTTTATTGAAAAATAGCTTGTCACCTTACGTACAATCTTGATCCGGAGCTTTTCTTTTTTTGCCGATTAAGAATTCGGTCGAAAAAAGAAAAGGAGAGGGCCAAGAGGGAGGGCATTGGTGACTATTGAGCACGTGAGTATACGTGATTAAGCACACAAAGGCAGCTTGGAGTATGTCTGTTATTAATTTCACAGGTAGTTCTGGTCCATTGGTGAAAGTTTGCGGCTTGCAGAGCACAGAGGCCGCAGAATGTGCTCTAGATTCCGATGCTGACTTGCTGGGTATTATATGTGTGCCCAATAGAAAGAGAACAATTGACCCGGTTATTGCAAGGAAAATTTCAAGTCTTGTAAAAGCATATAAAAATAGTTCAGGCACTCCGAAATACTTGGTTGGCGTGTTTCGTAATCAACCTAAGGAGGATGTTTTGGCTCTGGTCAATGATTACGGCATTGATATCGTCCAACTGCATGGAGATGAGTCGTGGCAAGAATACCAAGAGTTCCTCGGTTTGCCAGTTATTAAAAGACTCGTATTTCCAAAAGACTGCAACATACTACTCAGTGCAGCTTCACAGAAACCTCATTCGTTTATTCCCTTGTTTGATTCAGAAGCAGGTGGGACAGGTGAACTTTTGGATTGGAACTCGATTTCTGACTGGGTTGGAAGGCAAGAGAGCCCCGAAAGCTTACATTTTATGTTAGCTGGTGGACTGACGCCAGAAAATGTTGGTGATGCGCTTAGATTAAATGGCGTTATTGGTGTTGATGTAAGCGGAGGTGTGGAGACAAATGGTGTAAAAGACTCTAACAAAATAGCAAATTTCGTCAAAAATGCTAAGAAATAGGTTATTACTGAGTAGTATTTATTTAAGTATTGTTTGTGCACTTGCCTGCAGGCCTTTTGAAAAGCAAGCATAAAAGATCTAAACATAAAATCTGTAAAATAACAAGATGTAAAGATAATGCTAAATCATTTGGCTTTTTGATTGATTGTACAGGAAAATATACATCGCAGGGGGTTGACTTTTACCATTTCACCGCAATGGAATCAAACTTGTTGAAGAGAATGTTCACAGGCGCATACGCTACAATGACCCGATTCTTGCTAGCCTTTTCTCGGTCTTGCAAACAACCGCCGGCAGCTTAGTATATAAATACACATGTACATACCTCTCTCCGTATCCTCGTAATCATTTTCTTGTATTTATCGTCTTTTCGCTGTAAAAACTTTATCACACTTATCTCAAATACACTTATTAACCGCTTTTACTATTATCTTCTACGCTGACAGTAATATCAAACAGTGACACATATTAAACACAGTGGTTTCTTTGCATAAACACCATCAGCCTCAAGTCGTCAAGTAAAGATTTCGTGTTCATGCAGATAGATAACAATCTATATGTTGATAATTAGCGTTGCCTCATCAATGCGAGATCCGTTTAACCGGACCCTAGTGCACTTACCCCACGTTCGGTCCACTGTGTGCCGAACATGCTCCTTCACTATTTTAACATGTGGAATTCTTGAAAGAATGAAATCGCCATGCCAAGCCATCACACGGTCTTTTATGCAATTGATTGACCGCCTGCAACACATAGGCAGTAAAATTTTTACTGAAACGTATATAATCATCATAAGCGACAAGTGAGGCAACACCTTTGTTACCACATTGACAACCCCAGGTATTCATACTTCCTATTAGCGGAATCAGGAGTGCAAAAAGAGAAAATAAAAGTAAAAAGGTAGGGCAACACATAGTATGAATACAAACGTTCCAATATTCAGTTCTCCGGTCAGAGATTTACCAAGGTCTTTCGAACAAAAACATTTAGCGGTTGTAGA"
        mock_get_dna.return_value = None, [mock_dna], None
        
        expected_pams = ['AGG', 'TGG', 'TGG', 'CGG', 'AGG', 'TGG', 'GGG', 'CGG', 'AGG', 'AGG', 'TGG', 'TGG', 'AGG', 'AGG', 
                         'TGG', 'TGG', 'CGG', 'TGG', 'TGG', 'CGG', 'AGG', 'TGG', 'GGG', 'AGG', 'TGG', 'TGG', 'TGG', 'GGG', 
                         'TGG', 'AGG', 'TGG', 'TGG', 'TGG', 'TGG', 'TGG', 'CGG', 'AGG', 'TGG', 'TGG']      
        actual_pams = [mock_dna[loc:loc+3] for loc in main.get_locations(mock_dna)[0]]
        
        self.assertEqual(actual_pams, expected_pams)

class TestMutations(unittest.TestCase):

    @patch('main.get_dna')
    def test_number_mutations(self, mock_get_dna):
        """Test correct number of mutations generated"""
        mock_dna = "TACTATTAGCTGAATTGCCACTGCTATCGTTGTTAGTGGCGTTAGTGCTTGCATTCAAAGACATGGAGGGCGTTATTACGCCGGAGCTCCTCGACAGCAGATCTGATGACTGGTCAATATATTTTTGCATTGAGGCTCTGTTTGGAATTATATTTTGAGATGACCCATCTAATGTACTGGTATCACCAGATTTCATGTCGTTTTTTAAAGCGGCTGCTTGAGTCTTAGCAATAGCGTCACCATCTGGTGAATCCTTTGAAGGAACCACTGACGAAGGTTTGGACAGTGACGAAGAGGATCTTTCCTGCTTTGAATTAGTCGCGCTGGGAGCAGATGACGAGTTGGTGGAGCTGGGGGCAGGATTGCTGGCCGTCGTGGGTCCTGAATGGGTCCTTGGCTGGTCCATCTCTATTCTGAAAACGGAAGAGGAGTAGGGAATATTACTGGCTGAAAATAAGTCTTGAATGAACGTATACGCGTATATTTCTACCAATCTCTCAACACTGAGTAATGGTAGTTATAAGAAAGAGACCGAGTTAGGGACAGTTAGAGGCGGTGGAGATATTCCTTATGGCATGTCTGGCGATGATAAAACTTTTCAAACGGCAGCCCCGATCTAAAAGAGCTGACAGGGAAATGGTCAGAAAAAGAAACGTGCACCCGCCCGTCTGGACGCGCCGCTCACCCGCACGGCAGAGACCAATCAGTAAAAATCAACGGTTAACGACATTACTATATATATAATATAGGAAGCATTTAATAGAACAGCATCGTAATATATGTGTACTTTGCAGTTATGACGCCAGATGGCAGTAGTGGAAGATATTCTTTATTGAAAAATAGCTTGTCACCTTACGTACAATCTTGATCCGGAGCTTTTCTTTTTTTGCCGATTAAGAATTCGGTCGAAAAAAGAAAAGGAGAGGGCCAAGAGGGAGGGCATTGGTGACTATTGAGCACGTGAGTATACGTGATTAAGCACACAAAGGCAGCTTGGAGTATGTCTGTTATTAATTTCACAGGTAGTTCTGGTCCATTGGTGAAAGTTTGCGGCTTGCAGAGCACAGAGGCCGCAGAATGTGCTCTAGATTCCGATGCTGACTTGCTGGGTATTATATGTGTGCCCAATAGAAAGAGAACAATTGACCCGGTTATTGCAAGGAAAATTTCAAGTCTTGTAAAAGCATATAAAAATAGTTCAGGCACTCCGAAATACTTGGTTGGCGTGTTTCGTAATCAACCTAAGGAGGATGTTTTGGCTCTGGTCAATGATTACGGCATTGATATCGTCCAACTGCATGGAGATGAGTCGTGGCAAGAATACCAAGAGTTCCTCGGTTTGCCAGTTATTAAAAGACTCGTATTTCCAAAAGACTGCAACATACTACTCAGTGCAGCTTCACAGAAACCTCATTCGTTTATTCCCTTGTTTGATTCAGAAGCAGGTGGGACAGGTGAACTTTTGGATTGGAACTCGATTTCTGACTGGGTTGGAAGGCAAGAGAGCCCCGAAAGCTTACATTTTATGTTAGCTGGTGGACTGACGCCAGAAAATGTTGGTGATGCGCTTAGATTAAATGGCGTTATTGGTGTTGATGTAAGCGGAGGTGTGGAGACAAATGGTGTAAAAGACTCTAACAAAATAGCAAATTTCGTCAAAAATGCTAAGAAATAGGTTATTACTGAGTAGTATTTATTTAAGTATTGTTTGTGCACTTGCCTGCAGGCCTTTTGAAAAGCAAGCATAAAAGATCTAAACATAAAATCTGTAAAATAACAAGATGTAAAGATAATGCTAAATCATTTGGCTTTTTGATTGATTGTACAGGAAAATATACATCGCAGGGGGTTGACTTTTACCATTTCACCGCAATGGAATCAAACTTGTTGAAGAGAATGTTCACAGGCGCATACGCTACAATGACCCGATTCTTGCTAGCCTTTTCTCGGTCTTGCAAACAACCGCCGGCAGCTTAGTATATAAATACACATGTACATACCTCTCTCCGTATCCTCGTAATCATTTTCTTGTATTTATCGTCTTTTCGCTGTAAAAACTTTATCACACTTATCTCAAATACACTTATTAACCGCTTTTACTATTATCTTCTACGCTGACAGTAATATCAAACAGTGACACATATTAAACACAGTGGTTTCTTTGCATAAACACCATCAGCCTCAAGTCGTCAAGTAAAGATTTCGTGTTCATGCAGATAGATAACAATCTATATGTTGATAATTAGCGTTGCCTCATCAATGCGAGATCCGTTTAACCGGACCCTAGTGCACTTACCCCACGTTCGGTCCACTGTGTGCCGAACATGCTCCTTCACTATTTTAACATGTGGAATTCTTGAAAGAATGAAATCGCCATGCCAAGCCATCACACGGTCTTTTATGCAATTGATTGACCGCCTGCAACACATAGGCAGTAAAATTTTTACTGAAACGTATATAATCATCATAAGCGACAAGTGAGGCAACACCTTTGTTACCACATTGACAACCCCAGGTATTCATACTTCCTATTAGCGGAATCAGGAGTGCAAAAAGAGAAAATAAAAGTAAAAAGGTAGGGCAACACATAGTATGAATACAAACGTTCCAATATTCAGTTCTCCGGTCAGAGATTTACCAAGGTCTTTCGAACAAAAACATTTAGCGGTTGTAGA"  
        mock_locs = [1020, 1029, 1037, 1050, 1067, 1106]
                    
        mock_get_dna.return_value = None, [mock_dna], None
        
        mutations = main.get_all_mutations(mock_locs, [], mock_dna, mock_dna)
        self.assertEqual(len(mutations), 2) 
          
if __name__ == '__main__':
    unittest.main()