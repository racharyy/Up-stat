import re
import csv

with open('../../data/KROC_daily.csv') as fin:
    with open('../../data/KROC_daily_edited.csv','wb') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout,reader.fieldnames)
        writer.writeheader()
        for arow in reader:
            txt = re.sub('^Friday, |^Monday, |^Tuesday, |^Sunday, |^Wednesday, |^Thursday, |^Saturday, ','',arow['Date'])
            txt1 = re.sub('^January (\d*), ','\g<1>/1/',txt)
            txt1 = re.sub('^February (\d*), ','\g<1>/2/',txt1)
            txt1 = re.sub('^March (\d*), ','\g<1>/3/',txt1)
            txt1 = re.sub('^April (\d*), ','\g<1>/4/',txt1)
            txt1 = re.sub('^May (\d*), ','\g<1>/5/',txt1)
            txt1 = re.sub('^June (\d*), ','\g<1>/6/',txt1)
            txt1 = re.sub('^July (\d*), ','\g<1>/7/',txt1)
            txt1 = re.sub('^August (\d*), ','\g<1>/8/',txt1)
            txt1 = re.sub('^September (\d*), ','\g<1>/9/',txt1)
            txt1 = re.sub('^October (\d*), ','\g<1>/10/',txt1)
            txt1 = re.sub('^November (\d*), ','\g<1>/11/',txt1)
            txt1 = re.sub('^December (\d*), ','\g<1>/12/',txt1)
            txt1 = re.sub(' 0:00:00','',txt1).strip()
            if re.search('201[1-8]$',txt1):
                arow['Date']=txt1
                writer.writerow(arow)
