#!/usr/bin/python
"""
(c) Copyright 2013 Bjoern Schiessle <bjoern@schiessle.org>

This program is free software released under the MIT License, for more details
see LICENSE.txt or http://opensource.org/licenses/MIT

This program was written for personal usage. So don't expect any active
development beside adjustments to my own needs. Feel free to reuse it and
adjust it to your own needs.

This small program allows you to specify a 'path' where your backups
are located and a 'number' of backups you want to keep. The program will read
the directory 'path' and delete all files beside the latest 'number' of files.
The list of files will be sorted alphabetically, the program assumes that the
oldest file is at the top of the list and the newest file is at the bottom of
the list.
"""

import os, sys, getopt

class BackupRotate:

	def __init__(self, path="/mnt/backup/databases", number=120, dryRun=False):
		self.path = path
		self.number = number
		self.dryRun = dryRun

	def setPath(self, path):
		self.path = path

	def setNumber(self, number):
		self.number = number

	def setDryRun(self, dryRun):
		self.dryRun = dryRun

	def delOldBackups(self):
		filesList = sorted(os.listdir(self.path))
		numberOfDeletedFiles = len(filesList) - self.number
		if (numberOfDeletedFiles > 0):
			for file in filesList[0: numberOfDeletedFiles]:
				if (self.dryRun):
					print "I would delete:", file
				else:
                                        print "Delete:", file
					os.remove(self.path + '/' + file)
		else:
			print "Nothing to do!"

def printHelp():
	print 'optional parameters: '
	print '-h, --help            show help'
	print '-d, --dryRun          don\'t delete any files'
	print '-p, --path=PATH       specifiy the path of the backup files'
	print '-n, --number=NUMBER   specifiy the number of kept backups'

def main(argv):

	backupRotate = BackupRotate()

	try:
		opts, args = getopt.getopt(argv,"hdp:n:",["help","dryRun", "path=", "number="])
	except getopt.GetoptError:
		printHelp()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			printHelp()
			sys.exit()
		elif opt in ("-p", "--path"):
			backupRotate.setPath(arg)
		elif opt in ("-d", "--dryRun"):
			backupRotate.setDryRun(True)
		elif opt in ("-n", "--number"):
			backupRotate.setNumber(int(arg))

	backupRotate.delOldBackups()

if __name__ == "__main__":
	main(sys.argv[1:])
