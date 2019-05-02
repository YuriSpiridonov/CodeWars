# https://www.codewars.com/kata/human-readable-duration-format/train/python
# python 2.7 accidentally 

def format_duration(seconds):
    if type(seconds) != int or seconds == 0:
        return 'now'
    years = seconds//31536000
    days = (seconds - years*31536000)//86400
    hours = (seconds - years*31536000 - days*86400)//3600
    minutes = (seconds - years*31536000 - days*86400 - hours*3600)//60
    secs = seconds - years*31536000 - days*86400 - hours*3600 - minutes*60
    timeList = []
    timeListOfTuples = [('years' , years), ('days' , days), ('hours' , hours), ('minutes' , minutes), ('seconds' , secs)]
    for i in range(len(timeListOfTuples)):    
        if timeListOfTuples[i][1] > 0:
            if timeListOfTuples[i][1] == 1:
                timeList.append(str(timeListOfTuples[i][1])+' '+str(timeListOfTuples[i][0][:-1]))
            else:    
                timeList.append(str(timeListOfTuples[i][1])+' '+str(timeListOfTuples[i][0])) 
    if len(timeList) > 1:
        timeList.append(timeList.pop(-2)+' and '+timeList.pop(-1))
    return ', '.join(timeList)
                
print(format_duration(6786731536000))
print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds") 
