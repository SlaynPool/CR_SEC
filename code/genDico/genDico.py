def gen():
    dico = open("dico.txt", "w")
    #dico.write("")
    for a in range(0,10):
        for z in range(0,10):
            if z != a:
                for e in range(0,10):
                    if e !=a and e!=z:
                        for r in range(0,10):
                            if r!=a and r!=z and r!=e:
                                for t in range(0,10):
                                    if t!=a and t!=z and t!=e and t!=r:
                                        for y in range(0,10):
                                            if y!=a and y!=z and y!=e and y!=r and y!=t:
                                                for u in range(0,10):
                                                    if u!=a and u!=z and u!=e and u!=r and u!=t and u!=y:
                                                        for i in range(0,10):
                                                            if i!=a and i!=z and i!=e and i!=r and i!=t and i!=y and i!=u:
                                                                dico.write(str(a)+str(z)+str(e)+str(r)+str(t)+str(y)+str(u)+str(i)+"\n")
    dico.close()
gen()


