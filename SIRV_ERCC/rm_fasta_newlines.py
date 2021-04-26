import argparse

def get_args():

    desc = ('Remove newlines in seq entries from fasta file')
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-f', dest='fasta',
        help='FASTA file')
    args = parser.parse_args()
    return args


def main():
	args = get_args()
	fasta = args.fasta

	infile = open(fasta, 'r')
	outfile = open(fasta[:-6]+'_2line.fasta', 'w')

	start = True
	for line in infile:
		if line.startswith('>'):
			if not start:
				outfile.write(seq_buf+'\n')
			start = False
			seq_buf = ''
			outfile.write(line)
		else:
			seq_buf += line.strip()


	outfile.write(seq_buf+'\n')
	infile.close()
	outfile.close()

if __name__ == '__main__':
	main()