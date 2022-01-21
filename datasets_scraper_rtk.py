
import random

def main():

    original = open('/home/ubuntu/RobotCarDataset-Scraper/datasets_original.csv', 'r')
    lines = original.readlines()
    original.close()

    runs_file = open('/home/ubuntu/RobotCarDataset-Scraper/rtk_datasets.csv', 'r')
    runs = runs_file.readlines()
    runs_file.close()

    # Rimuovo le run:
    # - neve
    # - notte
    # - pioggia
    unwanted = ['2014-11-25-09-18-32', '2014-12-05-11-09-10', '2015-05-29-09-36-29', '2015-07-24-14-36-47',
                '2015-10-29-10-55-43', '2015-10-29-12-18-17']

    for i in range(0, len(runs)):
        runs[i] = runs[i].rstrip()

    r = runs.copy()
    for run in runs:
        if run in unwanted:
            r.remove(run)

    datasets = open('/home/ubuntu/RobotCarDataset-Scraper/datasets.csv', 'w')

    tags = ['stereo_centre', 'mono_left', 'mono_right', 'mono_rear', 'lms_rear', 'lms_front', 'ldmrs', 'gps', 'vo', 'tags']

    ds = []

    for line in lines:
        line = line.split(',')
        tags_to_remove = []
        # Select tags to remove
        for s in line:
            for i in tags:
                if i in s:
                    tags_to_remove.append(s)
        # Remove tags
        for i in tags_to_remove:
            line.remove(i)

        '''
        ['2015-08-13-10-29-44', '2015-10-30-11-31-23', '2015-08-18-14-07-43', '2015-08-17-13-23-50', '2015-08-20-11-48-34']
        Non vengono considerate perchè non ci sono su https://robotcar-dataset.robots.ox.ac.uk/datasets/
        '''
        if line[0] in r:
            ds.append(line)

    for line in ds:
        stereo_files = int((len(line)-1) / 2)
        if stereo_files < 3:
            continue
        tmp = []
        tmp.append(line[0])
        idx = random.randint(2, stereo_files-1)
        tmp.append(line[idx])
        tmp.append(line[stereo_files+idx])

        formatted = '{},{},{}\n'.format(tmp[0], tmp[1], tmp[2])
        datasets.write(formatted)

    datasets.close()


if __name__ == '__main__':
    main()