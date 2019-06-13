# https://www.codewars.com/kata/grab-csv-columns/train/python

def csv_columns(csv, indices):
    try:
        results = str()
        csvList = csv.split('\n')
        for i in range(len(csvList)):
            csvList[i] = csvList[i].split(',')
        indices = list(sorted(set(indices)))
        for index in indices:
            if index >= len(max(csvList)):
                indices = indices[:indices.index(index)]
                break
        for i in range(len(csvList)):
            temp = list()
            for index in sorted(set(indices)):
                temp.append(csvList[i][index])
                string = ','.join(temp)
            results += string+'\n'         
    except:
        results = ''  
    return results.rstrip('\n')
