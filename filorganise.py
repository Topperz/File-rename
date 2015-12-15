import os, re

def removeDbFiles(all_files):
	delcount = 0
	for i in range(len(all_files)):
		if all_files[i - delcount].endswith(".db") or all_files[i - delcount].endswith(".txt") \
		or all_files[i - delcount].endswith(".nfo") or all_files[i - delcount].endswith(".dat") \
		or all_files[i - delcount].endswith(".srt") or all_files[i - delcount].endswith(".jpg") \
		or all_files[i - delcount].endswith(".pdf") or all_files[i - delcount].endswith(".png") \
		or all_files[i - delcount].endswith(".ico") or all_files[i - delcount].endswith(".docx") \
		or all_files[i - delcount].endswith(".doc") or all_files[i - delcount].endswith(".smi") \
		or all_files[i - delcount].endswith(".torrent"):
			del all_files[i - delcount]
			delcount += 1

def rename(mappe):

	afsnit = os.listdir(mappe)

	removeDbFiles(afsnit)

	years = ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011",
"2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000", 
"1999", "1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991",
"1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981",
"1980", "1979", "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971",
"1970", "1969", "1968", "1967", "1966", "1965", "1964", "1963", "1962", "1961",
"1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951", "720p", "1080p"]

	for i in afsnit:
		is_folder = False
		filtype = None
		newname = None
		checkend = i.lower()
		if checkend.endswith("mp4") or checkend.endswith("avi") or checkend.endswith("mkv") or checkend.endswith("mpg"):
			filtype = i[-4:]
		else:
			is_folder = True
			
		split = re.findall(r"[\w']+", i)

		#split = re.split(r"[,.  -]+", i)
		try:
			if re.match(r"\D\d\d\D\d\d", split[1])  or (re.match(r"\d{3,5}", split[1]) and split[1] not in years):

				titel1 = split[0]
				episode = split[1]
				
				if filtype:
					newname = " ".join([titel1, episode]) + filtype
				else:
					newname = " ".join([titel1, episode])
				
				os.rename(mappe+i, mappe+newname)
				print "1rename " + i + " succesful to " + newname
		except:
			pass

		try:
			if re.match(r"\D\d\d\D\d\d", split[2]) or (re.match(r"\d{3,5}", split[2]) and split[2] not in years):

				titel1 = split[0]
				titel2 = split[1]
				episode = split[2]
				if filtype:
					newname = " ".join([titel1, titel2, episode]) + filtype
				else:
					newname = " ".join([titel1, titel2, episode])
				
				os.rename(mappe+i, mappe+newname)
				print "2rename " + i + " succesful to " + newname
		except:
			pass

		try:
			if re.match(r"\D\d\d\D\d\d", split[3]) or (re.match(r"\d{3,5}", split[3]) and split[3] not in years):

				titel1 = split[0]
				titel2 = split[1]
				title3 = split[2]
				episode = split[3]
				if filtype:
					newname = " ".join([titel1, titel2, title3, episode]) + filtype
				else:
					newname = " ".join([titel1, titel2, title3, episode])
				
				os.rename(mappe+i, mappe+newname)
				print "3rename " + i + " succesful to " + newname
		except:
			pass


		if is_folder:
			if newname:
				subfolder = mappe + newname + "\\"
			else:
				subfolder = mappe + i + "\\"

			rename(subfolder)

def main():
	workdir = os.getcwd()
	workdir = workdir + "\\"
	rename(workdir)


if __name__ == "__main__":
    main()