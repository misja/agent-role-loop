from boekenplank import Boekenplank as P
p=P(); p.toevoegen('Zee'); p.toevoegen('Atlas','Noor'); p.toevoegen('Bos')
assert [b.nummer for b in p.lijst(alleen_beschikbaar=False)] == [b.nummer for b in p.lijst()] == [1,2,3]
print('M1 True')
p=P(); p.toevoegen('Zee'); p.toevoegen('Atlas','Noor'); r=p.lijst(); r.clear(); s=p.lijst(alleen_beschikbaar=True); s.append(None)
assert [b.nummer for b in p.lijst()] == [1,2]
assert [b.nummer for b in p.lijst(alleen_beschikbaar=True)] == [1]
print('M2 True True')
