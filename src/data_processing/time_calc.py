from datetime import datetime, time, timedelta 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-e', '--edf_startTime', required=True, help = 'edf_start_time')
ap.add_argument('-a', '--annot_startTime', required=True, help = 'annot_start_time')
args = vars(ap.parse_args())

annot_time = datetime.strptime(args['annot_startTime'], '%H:%M:%S') -timedelta(0,30)
edf_start = datetime.strptime(args['edf_startTime'],'%H:%M:%S')

time_diff = annot_time - edf_start
print('diff of the times are {}'.format(time_diff))