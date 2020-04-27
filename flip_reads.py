
from optparse import OptionParser

def getOptions():
    parser = OptionParser()
    parser.add_option("--f", dest = "infile", help = "Input file",
                      metavar = "FILE", type = "string", default = "")
    parser.add_option("--o", dest = "outfile",
                      help = "output file", metavar = "FILE", type = "string")
    (options, args) = parser.parse_args()
    return options


def reverseComplement(seq):
    """ Returns the reverse complement of a DNA sequence, 
        retaining the case of each letter"""
    complement = ""

    for base in seq:
        if base == "A": complement += "T"
        elif base == "T": complement += "A" 
        elif base == "G": complement += "C"
        elif base == "C": complement += "G"
        elif base == "N": complement += "N"
        elif base == "a": complement += "t"
        elif base == "t": complement += "a" 
        elif base == "g": complement += "c"
        elif base == "c": complement += "g"
        elif base == "n": complement += "n"
        elif base == "*": complement += "*"
        else:
            complement += base
            print "Warning: reverse complement function encountered unknown base " + "'" + base + "'"

    reverseComplement = complement[::-1]

    return reverseComplement

def main():
    options = getOptions()

    o = open(options.outfile, 'w')    
    with open(options.infile, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("@"):
                o.write(line + "\n")
            else:
                line = line.split("\t")
                seq = line[9]
                qual = line[10]  

                polyA = "AAAAAAAAAAAAAAAAAAAA"
                polyT = "TTTTTTTTTTTTTTTTTTTT"

                #if polyA in seq[-50:]:
                if polyT in seq[0:50]:
                    line[9] = reverseComplement(seq)
                    line[10] = qual[::-1]
                o.write("\t".join(line) + "\n")

    o.close()

if __name__ == '__main__':
    main()
