import pathlib
import sqlite3
import tempfile
import unittest
from provac import build, write_bundle, safe_csv

class IntegrationTest(unittest.TestCase):
    def test_roles_branches_annotations_and_search(self):
        fixture=[{'id':'C','title':'Caso','current_node':'u','mapping':{
            'u':{'parent':None,'message':{'id':'u','author':{'role':'user'},'content':{'parts':['nulidad']}}},
            'a':{'parent':'u','message':{'id':'a','author':{'role':'assistant'},'content':{'parts':['p7m']}}}}}]
        data=build(fixture,[],[],{'C:u':{'accepted_tags':'NULIDAD','review_status':'REVISADO'}})
        self.assertEqual(data['messages'][0]['role'],'user')
        self.assertTrue(data['messages'][0]['on_current_path'])
        self.assertFalse(data['messages'][1]['on_current_path'])
        self.assertEqual(data['messages'][0]['accepted_tags'],'NULIDAD')
        with tempfile.TemporaryDirectory() as path:
            out=pathlib.Path(path)
            write_bundle(data,out)
            with sqlite3.connect(':memory:') as db:
                db.deserialize((out/'provac.sqlite').read_bytes())
                self.assertEqual(db.execute('pragma integrity_check').fetchone()[0],'ok')
                self.assertEqual(db.execute('select count(*) from records').fetchone()[0],3)
                self.assertEqual(db.execute('select count(*) from search where search match ?',('nulidad',)).fetchone()[0],1)

    def test_repeated_code_keeps_both_sources(self):
        matrices=[{'id':i,'title':i,'url':'https://example.invalid','text':'PROVAC,CITA_TEXTO\nAC-01,Texto\n'} for i in ['A','B']]
        data=build([],[],matrices)
        self.assertEqual(len(data['matrix_rows']),2)
        self.assertNotEqual(data['matrix_rows'][0]['id'],data['matrix_rows'][1]['id'])
        self.assertEqual(data['matrix_rows'][0]['code_occurrences'],2)

    def test_csv_literal_text(self):
        self.assertEqual(safe_csv('=1+1'),"'=1+1")

if __name__=='__main__':
    unittest.main()
