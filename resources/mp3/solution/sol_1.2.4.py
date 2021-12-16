from pymd5 import padding, md5
import sys
import os

NUM_ROUND = 6
MESSAGE = 'chuench1 and chuench2 guesses {0}'

def read_file(filename):
	ret = ''
	with open(filename, 'rb') as f:
		ret = f.read()
	return ret

def write_file(filename, content):
	with open(filename, 'wb') as f:
		f.write(content)

def compute_md5(filename):
	file_content = read_file(filename)
	return md5(file_content).hexdigest()


def blob_valid(filename, first=False):		
	blob = read_file(filename)
	if first:
		if blob.count('(') > 1 or blob.count(')') > 0:
			return False
	else:
		if '(' in blob or ')' in blob:
			return False
	return True

def add_padding(r):
	num_file = 2**r
	for i in range(num_file):
		filename = str(r)+'_'+str(i)
		file_content = read_file(filename)
		file_content += padding(len(file_content)*8)
		write_file(filename, file_content)

def generate_next_round(r):
	num_file = 2**r
	msg1_content = read_file('./msg1.bin')
	msg2_content = read_file('./msg2.bin')
	for i in range(num_file):
		filename = str(r)+'_'+str(i)
		new_filename_1 = str(r+1)+'_'+str(i)
		new_filename_2 = str(r+1)+'_'+str(num_file+i)
		file_content = read_file(filename)
		new_content_1 = file_content + msg1_content
		new_content_2 = file_content + msg2_content
		write_file(new_filename_1, new_content_1)
		write_file(new_filename_2, new_content_2)

def extract_blob(filename):
	file_content = read_file(filename)
	file_content = file_content[file_content.find('('):]
	file_content = file_content[file_content.find('(')+1:]
	return file_content

def main():
	if(len(sys.argv) < 3):
		print 'usage fastcoll prefix'
		exit(0)

	# setup working directory
	fastcoll_path = sys.argv[1]
	prefix_path = sys.argv[2]
	os.system('mkdir tmp')
	os.chdir('./tmp')
	# first round: generate two files
	while(True):
		os.system(fastcoll_path + ' -p ' + prefix_path + ' -o 1_0 1_1')
		if blob_valid('./1_0', first=True) and blob_valid('./1_1', first=True):
			break

	# got first two blobs
	r = 1
	while(r < NUM_ROUND):
		print 'Starting round {0}'.format(r+1)
		num_prefixes = 2**r
		last_md5 = compute_md5(str(r)+'_0')
		add_padding(r)

		while(True):
			os.system(fastcoll_path + ' -i ' + last_md5)
			if blob_valid('./msg1.bin') and blob_valid('./msg2.bin'):
				break
		generate_next_round(r)
		r+=1

	# at this point, we got the required number of blobs
	add_padding(NUM_ROUND)
	blobs = []
	num_file = 2**NUM_ROUND
	for i in range(num_file):
		filename = str(NUM_ROUND)+'_'+str(i)
		blob = extract_blob(filename)
		blobs.append(blob)

	suffix = ')\n\n'
	for i in range(len(blobs)):
		suffix += 'dup\n('+blobs[i]+')\neq {('+MESSAGE.format(i)+') show} if\n\n'
	
	for i in range(num_file):
		filename = str(NUM_ROUND)+'_'+str(i)
		file_content = read_file(filename)
		write_file(filename+'.ps', file_content+suffix)

if __name__ == '__main__':
	main()