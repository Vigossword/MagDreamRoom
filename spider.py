# 我想直接开始， 所以这是爬虫的最初的样子。
# 
##########################################
import argparse
import requests
import bs4
from pprint import pprint


def debug_print(debug_info):
	DEBUG = True
	if DEBUG:
		pprint("DEBUG: {}".format(debug_info))

def main_loop(first_url):

	url = first_url

	while True:

		#...下次写

		#我希望这个程序是多线程的， 不然太慢了！
		#所以这个主循环中不应该有任何实际的爬取网页的代码
		#这个主循环应该是负责调度所有子线程的
		#可以使用 threadpool，开出 n_t 个线程
		#主循环检查到当前有线程数小于 n_t 个线程的时候， 就创建一个线程
		#并且交予这个线程一个 url， 让它去获取网页上的信息。
		#可以将这个过程想象成女王和工蜂
		#女王调度任务， 工蜂执行任务， 并反馈任务结果

		# if threadpool.cur_num_thread < n_t:
		# 	createThread(url)
		#
		# for e in threadpool.all_thread:
		# 	if e.alreadyComplete():
		# 		bs = bs.BeautifulSoup(e.web_content)
		
		#将获取的结果存入数据队列中
		#========================================
		#这里我预想一个对象叫做数据队列，可以用于放置获取到的信息，并且
		#可以按顺序取出其中的数据， 队列会负责保证按url被顺序取出，也保证url被存入
		#数据库
		#=========================================
		#这里存在一个问题，进入重复的网址，爬虫在几个网址间循环！
		#如果每次让爬虫前进前，都检查一遍所有爬过的网址，这显然不现实
		#因为，预期这个爬虫将会爬上百万个网站（当然可能更多），而且将大量数据从数据库中调出也不现实
		#比较好的办法， 就是让数据队列缓存 m 个最近爬过的网址， 爬虫只检查这几个网址。
		
		#url = power_queue.push(bs.findall('a'))
		#url = power_queue.next_url()

		break


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='你只需要指定爬虫的起始位置，它就会沿着网站之间的链接，爬遍互联网!（但愿如此~）')
	parser.add_argument('first_url',help='爬虫从这个网址开始爬起')
	args = parser.parse_args()

	debug_print("爬虫的起点是：{}".format(args.first_url))

	#始めますよ!
	main_loop(args.first_url)