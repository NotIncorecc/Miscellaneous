codon_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def sp3(m):
    if len(m)%3!=0:
        m=0
        g=''
    else:
        v=0
        g=''
        for i in m:
            if v==3:
                g+=' '
                v=0
            g+=i
            v+=1
    return g

dna = input('Enter dna strand from 5\' to 3\':')
dna = dna.upper()

def dtemplate(a):
    t=''
    s1 = ['A','G']
    s2 = ['T','C'] 
    for i in a:
        if i in s1:
            t+=s2[s1.index(i)]
        elif i in s2:
            t+=s1[s2.index(i)]
        else:
            break
    return t

def mRna_tRna(a):
    t=''
    s1 = ['A','G']
    s2 = ['U','C'] 
    for i in a:
        if i in s1:
            t+=s2[s1.index(i)]
        elif i in s2:
            t+=s1[s2.index(i)]
        elif i == 'T':
            t+='A'
        else:
            break
    return t

def detect_prot(f):
    protein = ''
    for i in f.split():
        protein+=codon_map[i]+' '
    return protein

temp_str = dtemplate(dna)
mRna = mRna_tRna(temp_str)
tRna = mRna_tRna(mRna)


if len(dna)==len(temp_str) and len(dna)%3==0:
    print('Coding Strand:','5\' '+sp3(dna)+' 3\'')
    print('Temp.  Strand:','3\' '+sp3(temp_str)+' 5\'')
    #Transcription
    print('mRna   Strand:','5\' '+sp3(mRna)+' 3\'')#codon
    print('tRna   Strand:','   '+sp3(tRna)+'    \n')#anticodon
    print('Proteins:',detect_prot(sp3(mRna)))
else:
    print('you did somethin wrong')
    if len(dna)%3!=0:
        print('incomplete strand')

        
