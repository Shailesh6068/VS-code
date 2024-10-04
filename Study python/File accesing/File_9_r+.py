f = open("Sample.txt","r+")    # "use of r+ in python." this is original line
f.write("hel")                 # after this it become " hel of r+ in python."
print(f.read())                #   hel"Pointer ya position la alay tymule yacha nantarcha print honar" of r+ in python.
f.close()