#-*- coding: utf-8 -*-
# Edited on 5th june 2018

# packages

import sys,os,py2neo,csv
from py2neo import *



# Neo4j database connexion

ID = sys.argv[1]
password = sys.argv[2]
data = sys.argv[3]

py2neo.authenticate("localhost:7474",ID,password)

graph = Graph()


def create_tf_nodes(f):
	
	with open(f) as csvfile:
		tx = graph.begin()
		reader = csv.reader(csvfile, delimiter="\t")
		for row in reader:
			gene = graph.find_one("Gene", "Entrez_id", row[0])			
			if gene != None:
				gene.add_label("GOI")
				gene.push()

				
	tx.commit()	


			
def main():
	create_tf_nodes(data)
	
	


if __name__ == "__main__":
	main()
