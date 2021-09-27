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

temp_str = dtemplate(dna)
mRna = mRna_tRna(temp_str)
tRna = mRna_tRna(mRna)


if len(dna)==len(temp_str):
    print('Coding Strand:','5\' '+dna+' 3\'')
    print('Temp.  Strand:','3\' '+temp_str+' 5\'')
    #Transcription
    print('mRna   Strand:','5\' '+mRna+' 3\'')#codon
    print('tRna   Strand:','   '+tRna+'    ')#anticodon
else:
    print('you did somethin wrong')

