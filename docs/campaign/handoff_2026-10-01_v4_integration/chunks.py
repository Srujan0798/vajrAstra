import sys
LIM=int(sys.argv[1]); 
for p in sys.argv[2:]:
    lines=open(p,encoding='utf-8',errors='replace').read().split('\n')
    out=[];start=1;acc=0
    for i,l in enumerate(lines,1):
        b=len(l.encode())+1
        if acc+b>LIM and acc>0:
            out.append((start,i-start)); start=i; acc=0
        acc+=b
    out.append((start,len(lines)-start+1))
    print(p, ' '.join(f'{o}:{n}' for o,n in out))
