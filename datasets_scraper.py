

original = open('/home/radice/neuralNetworks/RobotCarDataset-Scraper/datasets_original.csv', 'r')
new = open('/home/radice/neuralNetworks/RobotCarDataset-Scraper/datasets.csv', 'w')

lines = original.readlines()

for line in lines:
    line = line.split(',')
    dictionary = ['stereo_centre', 'mono_left', 'mono_right', 'mono_rear', 'lms_rear']
    to_remove = []
    for s in line:
        for i in dictionary:
            if i in s:
                to_remove.append(s)
    for i in to_remove:
        line.remove(i)
    formatted = ''
    for index, i in enumerate(line):
        if not index == len(line) - 1:
            formatted = formatted + i + ','
        else:
            formatted = formatted + i
    new.write(formatted)

new.close()
original.close()
