import unittest

class Note(object):
    def __init__(self, name, note):
        #Pole name nie może być None, w przeciwnym wypadku wyrzucić ma wyjątek;
        #Pole name nie może być puste, w przeciwnym wypadku wyrzucić ma wyjątek;
        #Pole note ma być w przedziale zamkniętym od 2 do 6, w przeciwnym przypadku ma wyrzucić wyjątek;
        if (isinstance(name,str)==False):
            raise Exception("\"name\" must be string")
        elif(name==""):
            raise Exception("\"name\" can't be empty, name==\"\"")
        elif(name==None):
            raise Exception("\"name\" can't be equal to None, name==None")
        else:
            self.name = name
        if (isinstance(note,float)==False):
            raise Exception("\"note\" must be float")
        elif(note<2 or note>6):
            raise Exception("\"note\" must be in range from 2 to 6, note>=2 and note<=6")
        else:
            self.note = note
    def get_name(self):
        return self.name
    def get_note(self):
        return self.note


class NoteTest(unittest.TestCase):

    def test_get_name_true(self):
        self.assertEqual("Nazwa", Note("Nazwa",6.0).get_name())
    def test_get_note_true(self):
        self.assertEqual(6, Note("Nazwa",6.0).get_note())

    #wyjatki note'a
    def test_note_is_not_float_exception(self):
        self.assertRaises(Exception, Note, "Nazwa",7)
    def test_note_above_range_exception(self):
        self.assertRaises(Exception, Note, "Nazwa",7.0)
    def test_note_below_range_exception(self):
        self.assertRaises(Exception, Note, "Nazwa",1.0)

    #wyjatki name'a
    def test_name_is_not_string_exception(self):
        self.assertRaises(Exception, Note, 777,7.0)
    def test_name_is_empty_exception(self):
        self.assertRaises(Exception, Note, "",7.0)
    def test_name_is_None_exception(self):
        self.assertRaises(Exception, Note, None,7.0)


class NotesStorage(object):
    def __init__(self, notes=[]):
        self.notes=notes
    def add(self,note):
        self.notes.append(note)
        return self.notes
    def clear(self):
        self.notes=[]
        return self.notes
    def getAllNotesOf(self,name):
        notesToReturn=[]
        for i in self.notes:
            if(i.get_name()==name):
                print("Oceny tego pana: "+str(i.get_name())+" | "+str(i.get_note()))
                notesToReturn.append(Note(i.get_name(),i.get_note()))
        return notesToReturn
#storage=NotesStorage([Note("bob",5.0),Note("bob",6.0),Note("jan",2.0),Note("dzban",2.0)])
#print(storage.getAllNotesOf("bob"))
#print(storage.getAllNotesOf("jan"))
#storage.clear()
#print(storage.getAllNotesOf("bob"))#juz nie wypisuje
#storage.add(Note("bob",4.0))#dodalo
#print(storage.getAllNotesOf("bob"))#wypisalo


class NotesService(NotesStorage):
    def __init__(self, notes):
        NotesStorage.__init__(self, notes)
    def averageOf(self,name):
        suma=0
        ilosc=0
        for i in self.notes:
            suma=suma+i.get_note()
            ilosc=ilosc+1
        return suma/ilosc
service=NotesService([Note("bob",5.0),Note("bob",6.0),Note("jan",2.0),Note("dzban",2.0)])
#print(service.averageOf("bob"))

class NoteServiceTest(unittest.TestCase):

    def test_add_note(self):
        self.assertEqual(NotesService([]).add(Note("bob",6.0))[0].get_name(), [Note("bob",6.0)][0].get_name())
    def test_clear(self):
        self.assertEqual(NotesService([Note("bob",6.0)]).clear(), [])
    def test_getAllNotesOf(self):
        self.assertEqual(NotesService([Note("bob",5.0),Note("bob",6.0),Note("jan",2.0),Note("dzban",2.0)]).getAllNotesOf("dzban")[0].get_name(), [Note("dzban",2.0)][0].get_name())



