import json

def main():
    with open("/home/jimmy/shiyanlou_scrapy1/data.json", 'r') as f:
        allcourse = json.load(f)
    for course in allcourse:
        #print(course['name'])
        #print(course['description'])
        #print(course['type'])
        print(course['name'], course['students'])

if __name__ == '__main__':
    main()
