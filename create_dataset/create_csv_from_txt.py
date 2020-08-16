

files_list = ["poezii1_alecsandri.txt", "poezii1_blaga.txt", "poezii1_blandiana.txt", "poezii1_eminescu.txt", "poezii1_toparceanu.txt"]
# files_list = ["poezii1_alecsandri.txt"]


import pandas as pd 
  
data = [] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Title', 'Text', 'Author']) 
print(df.head())


def save_poem_to_csv(title, poem_text, author):
	global df
	print("Save to csv, title:", title, "text:", poem_text, "author:", author)
	data_new = [[title, poem_text, author]] 
	  
	# Create the pandas DataFrame 
	df_new = pd.DataFrame(data_new, columns = ['Title', 'Text', 'Author']) 
	df = df.append(df_new, ignore_index=True)

	print(df_new.head())
	print("***8")




for filename in files_list:
	f = open(filename, "r")
	next_is_author = False
	last_line_is_separator = False
	cnt = 0
	author = "unknown"
	poem_text = ""

	for line in f.readlines():


		if line == "-----------\n" and next_is_author == False:
			next_is_author = True
			last_line_is_separator = True

		elif line == "-----------\n" and last_line_is_separator == True:
			next_is_author = False
			print("POEM:", poem_text)

			save_poem_to_csv(title, poem_text, author)
			poem_text = ""


		elif next_is_author == True:
			print("###AUTHOR: " + line)
			author = line.strip()
			last_line_is_separator = False
			next_is_author = False
			cnt += 1

		elif '<font size="+1">' in line:
			title = line.strip().replace('<font size="+1">', '').replace('</font>','')
			print("$TITLE:", title)
			
		elif line != "\n" and line !="-----------\n":
			# print(line)
			last_line_is_separator = False
			poem_text += line


	print("*****Nr poezii pentru autorul", author,": *****" ,cnt)

	f.close()




print("Final data:")
print(df.head())

df.to_csv("Poezii1.csv", index=False)