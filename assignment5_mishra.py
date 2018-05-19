import os
import shutil
import random
import re

#---------------------------Folder Division Starts------------------------------------
# Division of arxiv
my_arxiv_src = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\articles\\arxiv"
my_arxiv_src_train = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Training\\arxiv"
my_arxiv_src_test = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Testing\\arxiv"

if not os.path.exists(my_arxiv_src_train):
    os.makedirs(my_arxiv_src_train)
if not os.path.exists(my_arxiv_src_test):
    os.makedirs(my_arxiv_src_test)

for item in os.listdir(my_arxiv_src):
	if (random.uniform(0,1) >= 0.5):
		full_file_name = os.path.join(my_arxiv_src, item)
		shutil.copy(full_file_name,my_arxiv_src_train)
	else:
		full_file_name = os.path.join(my_arxiv_src, item)
		shutil.copy(full_file_name,my_arxiv_src_test)

# Division of jdm
my_jdm_src = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\articles\\jdm"
my_jdm_src_train = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Training\\jdm"
my_jdm_src_test = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Testing\\jdm"

if not os.path.exists(my_jdm_src_train):
    os.makedirs(my_jdm_src_train)
if not os.path.exists(my_jdm_src_test):
    os.makedirs(my_jdm_src_test)

for item in os.listdir(my_jdm_src):
	if (random.uniform(0,1) >= 0.5):
		full_file_name = os.path.join(my_jdm_src, item)
		shutil.copy(full_file_name,my_jdm_src_train)
	else:
		full_file_name = os.path.join(my_jdm_src, item)
		shutil.copy(full_file_name,my_jdm_src_test)

# Division of plos
my_plos_src = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\articles\\plos"
my_plos_src_train = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Training\\plos"
my_plos_src_test = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Testing\\plos"

if not os.path.exists(my_plos_src_train):
    os.makedirs(my_plos_src_train)
if not os.path.exists(my_plos_src_test):
    os.makedirs(my_plos_src_test)

for item in os.listdir(my_plos_src):
	if (random.uniform(0,1) >= 0.5):
		full_file_name = os.path.join(my_plos_src, item)
		shutil.copy(full_file_name,my_plos_src_train)
	else:
		full_file_name = os.path.join(my_plos_src, item)
		shutil.copy(full_file_name,my_plos_src_test)

# ----------------------Folder Division Complete -------------------------------
stoplist = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Pramod\\stoplist.txt"

path_train = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Training"
path_test = "D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 05\\Assignment5_Final\\new_articles\\Testing"

train_list = [f for f in os.listdir(path_train)]
test_list = [f for f in os.listdir(path_test)]

vocab = []
for f in range (len(train_list)):
	path_article = path_train + "\\" + train_list[f]
	texts_article = [f for f in os.listdir(path_article)]
	for f in range (len(texts_article)):
		path_text = path_article + "\\" +texts_article[f]
		with open(path_text, encoding="Latin-1") as h:
			words = h.read().split()
			vocab = vocab + words
		h.close()
		path_text = ""
	texts_article = []
	path_article = ""

#converting to lowercase
lower_vocab=[]
for f in vocab:
        a = f.lower()
        lower_vocab.append(a)
        a=""

#removing special characters
sp_vocab=[]
for f in range(len(lower_vocab)):
        a = re.sub(r'[^a-zA-Z0-9 ]',r'',lower_vocab[f])
        sp_vocab.append(a)
        a = ""

#Deleting all the duplicate elements from the list [vocab]
unique_vocab = list(set(sp_vocab))

#removing stop words
with open(stoplist) as i:
        stop_words = i.read().split()
i.close()
stop_words = stop_words + ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","=","+","{","}","[","]",";",":","<",">",",",".","?","/"]
for f in range (len(stop_words)):
        if stop_words[f] in unique_vocab:
                unique_vocab.remove(stop_words[f])

#Removing blank spaces
unique_vocab = list(filter(None,unique_vocab))

#Finally sorting according to alphabet
unique_vocab.sort()

#removing digits
bag = [item for item in unique_vocab if not item.isdigit()]

#Preprosessing step B - Converting training data into set of features :

uni_voc = []
sp_voc = []
f_list = []
train_feature = []
countA = 0
countJ = 0
countP = 0
for a in range(len(train_list)):
        path_article = path_train+"\\"+train_list[a]
        texts_article = [f for f in os.listdir(path_article)]
        for b in range (len(texts_article)):
                path_text = path_article+"\\"+texts_article[b]
                with open(path_text, encoding="Latin-1") as c:
                        words = c.read().lower().split()
                        for d in range (len(words)):
                                i = re.sub(r'[^a-zA-Z0-9 ]',r'',words[d])
                                sp_voc.append(i)
                                i = ""
                                uni_voc = list(set(sp_voc))
                        for e in range (len(bag)):
                                if bag[e] in uni_voc:
                                        f_list.append("1")
                                else:
                                        f_list.append("0")
                        if (train_list[a] == 'arxiv'):
                                f_list.append("A")
                                countA = countA + 1
                        if (train_list[a] == 'plos'):
                                f_list.append("P")
                                countP = countP + 1
                        if (train_list[a] == 'jdm'):
                                f_list.append("J")
                                countJ = countJ + 1
                c.close()
                train_feature.append(f_list)
                f_list = []
                uni_voc = []
                sp_voc = []
                path_text = ""
        texts_article = []
        path_article = []

#Classification Step (Testing Phase)

test_feature = []
for a in range(len(test_list)):
        path_article = path_test+"\\"+test_list[a]
        texts_article = [f for f in os.listdir(path_article)]
        for b in range (len(texts_article)):
                path_text = path_article+"\\"+texts_article[b]
                with open(path_text,encoding="Latin-1") as c: #************************** Used the "Latin-1" encoding
                        words = c.read().lower().split()
                        for d in range (len(words)):
                                i = re.sub(r'[^a-zA-Z0-9 ]',r'',words[d])
                                sp_voc.append(i)
                                i = ""
                                uni_voc = list(set(sp_voc))
                        for e in range (len(bag)):
                                if bag[e] in uni_voc:
                                        f_list.append("1")
                                else:
                                        f_list.append("0")
                c.close()
                        
                test_feature.append(f_list)
                f_list = []
                uni_voc = []
                sp_voc = []
                path_text = ""
        texts_article = []
        path_article = []

#Reading testing data for comparison with output

uni_voc = []
sp_voc = []
f_list = []
test_op_feature = []
for a in range(len(test_list)):
        path_article = path_test+"\\"+test_list[a]
        texts_article = [f for f in os.listdir(path_article)]
        for b in range (len(texts_article)):
                path_text = path_article+"\\"+texts_article[b]
                with open(path_text, encoding="Latin-1") as c:
                        words = c.read().lower().split()
                        for d in range (len(words)):
                                i = re.sub(r'[^a-zA-Z0-9 ]',r'',words[d])
                                sp_voc.append(i)
                                i = ""
                                uni_voc = list(set(sp_voc))
                        for e in range (len(bag)):
                                if bag[e] in uni_voc:
                                        f_list.append("1")
                                else:
                                        f_list.append("0")
                        if (train_list[a] == 'arxiv'):
                                f_list.append("A")
                        if (train_list[a] == 'plos'):
                                f_list.append("P")
                        if (train_list[a] == 'jdm'):
                                f_list.append("J")
                c.close()
                test_op_feature.append(f_list)
                f_list = []
                uni_voc = []
                sp_voc = []
                path_text = ""
        texts_article = []
        path_article = []

length = min(len(test_feature),len(train_feature))

countA1 = 0
countJ1 = 0
countP1 = 0

PofA=0.0
PofJ=0.0
PofP=0.0

multA=1.0
multJ=1.0
multP=1.0

for i in range(length):
    for j in range(len(test_feature[0])):
        if (test_feature[i][j] == train_feature [i][j]):
            if ((train_feature[i][len(train_feature[i])-1]) == "A"):
                countA1 = countA1 + 1
                break
            if ((train_feature[i][len(train_feature[i])-1]) == "J"):
                countJ1 = countJ1 + 1
                break
            if ((train_feature[i][len(train_feature[i])-1]) == "P"):
                countP1 = countP1 + 1
                break
            
            PofA = countA1 / length
            PofJ = countJ1 / length
            PofP = countP1 / length
            
            if (PofA != 0):
                    multA = multA * PofA
            if (PofJ != 0):
                    multJ = multJ * PofJ
            if (PofP != 0):
                    multP = multP * PofP
            
            countA1=0
            countJ1=0
            countP1=0
            
    val = max(multA,multJ,multP)
    if (val == multA):
            test_feature[i].append("A")
    if (val == multJ):
            test_feature[i].append("J")
    if (val == multP):
            test_feature[i].append("P")
    multA=1.0
    multJ=1.0
    multP=1.0


a_count = 0
j_count = 0
p_count = 0

length_new = min(len(test_feature),len(test_op_feature))
for j in range (length_new):
        if(test_op_feature[j][len(test_op_feature[j])-1] == "A"):
            class_str = "ARXIV"
        elif(test_op_feature[j][len(test_op_feature[j])-1] == "J"):
            class_str = "JDM"
        else:
            class_str = "PLOS"
        
        if(test_feature[j][len(test_feature[j])-1] == "A"):
            cc_class_str = "ARXIV"
        elif(test_feature[j][len(test_feature[j])-1] == "J"):
            cc_class_str = "JDM"
        else:
            cc_class_str = "PLOS"

        
        print("Actual Class: " +class_str)
        print("Classified Class: " +cc_class_str)
        print("--------------------------------")
        if(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                a_count = a_count + 1         
        elif(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                j_count = j_count + 1                
        elif(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                p_count = p_count + 1

for j in range (0,countA):
        
        print("Actual Class: " +cc_class_str)
        print("Classified Class: " +class_str)
        print("--------------------------------")
        if(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                a_count = a_count + 1

for j in range (countA,countA+countJ):
        
        print("Actual Class: " +class_str)
        print("Classified Class: " +cc_class_str)
        print("--------------------------------")
        if(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                j_count = j_count + 1
for j in range (countA+countJ,len(test_feature)):
        
        print("Actual Class: " +class_str)
        print("Classified Class: " +cc_class_str)
        print("--------------------------------")
        if(test_op_feature[j][len(test_op_feature[j])-1] == test_feature[j][len(test_feature[j])-1]):
                p_count = p_count + 1
               

print("Accuracy ->")
print("ARXIV : "+str(round(a_count/countA * 100,2)))
print("JDM : "+str(round(a_count/countJ * 100,2)))
print("PLOS : "+str(round(p_count/countP * 100,2)))




            
            




