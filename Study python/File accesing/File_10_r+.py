f = open("Sample1.txt","r+")    # "use of r+ in python." this is original line
print(f.read())                 # When we use read at that time pointer go to end of file
f.write("hel")                 # after this it become " use of r+ in python.hel"  hel pointer chya position pasun lihayala chalu honar
print(f.read())                #   hel"Pointer ya position la alay tymule yacha nantarcha print honar" of r+ in python.
f.close()                       