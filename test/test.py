import os
import shutil
import sys
import tarfile
import tempfile

import genomicsdb

def run_test():
	genomicsdb.version()

	gdb = genomicsdb.connect("ws", "callset_t0_1_2.json", "vid.json", "chr1_10MB.fasta.gz", ["DP"], 40)
	try:
		gdb.query_variant_calls()
	except Exception as e:
		print(e)

	gdb = genomicsdb.connect("ws", "callset_t0_1_2.json", "vid.json", "chr1_10MB.fasta.gz", ["DP"], 40)
	list = gdb.query_variant_calls("t0_1_2", [(0,1000000000)], [(0,3)])
	print(list)

	list = gdb.query_variant_calls("t0_1_2", [(0,13000), (13000, 1000000000)], [(0,3)])
	print(list)

	gdb.query_variant_calls("t0_1_2", [(0,1000000000)])
	gdb.query_variant_calls("t0_1_2")

tmp_dir = tempfile.TemporaryDirectory().name

if not os.path.exists(tmp_dir):
	os.makedirs(tmp_dir)
else:
	sys.exit("Aborting as temporary directory seems to exist!")

tar = tarfile.open("test/inputs/sanity.test.tgz")
tar.extractall(tmp_dir)

os.chdir(tmp_dir)

run_test()

shutil.rmtree(tmp_dir)

