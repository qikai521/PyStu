file = open('/Users/qikai/Desktop/text2.txt','r')
boyFileName = '/Users/qikai/Desktop/boy_1.txt'
boyFile = open(boyFileName,'w')
girlFileName = '/Users/qikai/Desktop/girl_1.txt'
girlFile = open(girlFileName,'w')
index = 1
for each_line in file.readlines():
    if each_line.startswith('oldSeven:'):
        # print(each_line)
        saveStr = each_line[9:len(each_line)]
        print(saveStr)
        boyFile.write(saveStr)
    elif each_line.startswith('Okay:'):
        saveStr = each_line[5:len(each_line)]
        girlFile.write(saveStr)
    elif each_line.startswith("======="):
        index += 1
        boyFile.close()
        girlFile.close()
        boyFile = open(str('/Users/qikai/Desktop/boy_%d.txt'%(index)),'w')
        girlFile = open(str('/Users/qikai/Desktop/girl_%d.txt'%(index)),'w')
        continue;
    else:
        print(each_line)
boyFile.close()
girlFile.close()
print("分割结束")
