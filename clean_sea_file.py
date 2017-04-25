import xlrd
import csv
import glob
import pandas as pd

def clean_tag_column():
	#slno,queid,que_userid,que_score,que_time,tags,no_of_views,no_of_ans,ans_ID,ans_userid,ans_score,resp_time
	dataFrame = pd.read_csv('Stack_Exchange_answers.csv', header=None)
	#Spliting the columns for cleaning column data
	list_slno = dataFrame[0]
	list_queid = dataFrame[1]
	list_que_userid = dataFrame[2]
	list_que_score = dataFrame[3]
	list_que_time = dataFrame[4]
	list_tags = dataFrame[5]
	list_no_of_views = dataFrame[6]
	list_no_of_ans = dataFrame[7]
	list_ans_ID = dataFrame[8]
	list_ans_userid = dataFrame[9]
	list_ans_score = dataFrame[10]
	list_resp_time = dataFrame[11]
	#Create DataFrame with required columns only
	CleanedDataFrame = pd.DataFrame({'slno':list_slno,'queid':list_queid, 'tags':list_tags, 'que_time':list_que_time, 'resp_time':list_resp_time})
	#Create the csv file using required columns
	CleanedDataFrame.to_csv('cleaned_sea.csv', index=None)

def Process_File():
	print 'Started Processing files..'
	clean_tag_column()

Process_File()




























