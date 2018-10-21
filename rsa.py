from Crypto.Util.number import *

import gmpy2




p = 169524110085046954319747170465105648233168702937955683889447853815898670069828343980818367807171215202643149176857117014826791242142210124521380573480143683660195568906553119683192470329413953411905742074448392816913467035316596822218317488903257069007949137629543010054246885909276872349326142152285347048927
q = 170780128973387404254550233211898468299200117082734909936129463191969072080198908267381169837578188594808676174446856901962451707859231958269401958672950141944679827844646158659922175597068183903642473161665782065958249304202759597168259072368123700040163659262941978786363797334903233540121308223989457248267
e = 65537
c = 4531850464036745618300770366164614386495084945985129111541252641569745463086472656370005978297267807299415858324820149933137259813719550825795569865301790252501254180057121806754411506817019631341846094836070057184169015820234429382145019281935017707994070217705460907511942438972962653164287761695982230728969508370400854478181107445003385579261993625770566932506870421547033934140554009090766102575218045185956824020910463996496543098753308927618692783836021742365910050093343747616861660744940014683025321538719970946739880943167282065095406465354971096477229669290277771547093476011147370441338501427786766482964

t = (p-1)*(q-1)
n = p*q

# returns d value such that e * d == 1 modulo t, or 0 if no such y exists.
d = gmpy2.invert(e,t)

# Decryption
decimalmessage = pow(c,d,n)
print(long_to_bytes(decimalmessage))




