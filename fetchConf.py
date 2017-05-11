import presentCats
import argparse
import gcalendar

def main_func():
	baseUrl = "http://www.confsearch.org"
	parser = argparse.ArgumentParser(description='Conference search tool')
	parser.add_argument('--list', action='store_true', help='get the list of categories')
	parser.add_argument('--cat', dest='cat', help='Category of conference use --list to get the list')

	args = parser.parse_args()
	if args.cat:
	    print args.cat
	if args.list:
	    for l in presentCats.presentCats():
	        print l
	    return


	catUrl= presentCats.getCatUrl(args.cat)
	print catUrl
	info = presentCats.getConfs(baseUrl+catUrl.replace("graphicView=1","graphicView=0"))

	print info
      
        calendar.addEvents(info)

main_func()
