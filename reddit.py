#!/usr/bin/python3

import argparse
import sys
import json
import requests
		
def get_response():
		
		url = "https://www.reddit.com/r/" + sys.argv[1] + '/'
		response = requests.get(url+'.json',headers = {'User-agent':'bot'})
		
		if not response.ok:
			print ("Error ", response.status_code)
			exit(response.status_code)
        
		data = response.json()
		subtitles = list()
		for i in range(0,2):
		 subtitles.append(data['data']['children'][i]['data']['title'])
		return subtitles

def main():

		output_filehandle = open("posts.txt",
                             mode = 'w',
                             encoding = 'utf8')
		subreddit_titles = get_response()
		output_text = 'r/'+sys.argv[1]+'\n\n'+'\n\n'.join(subreddit_titles)
		output_filehandle.write(output_text)
		output_filehandle.write('\n')

if __name__ == '__main__':
		main()

