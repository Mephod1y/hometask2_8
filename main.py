from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9")
db = client.web9


def find_quote_by_name(fullname):
    res = []
    authors = db.authors.find({"fullname": fullname})
    for a in authors:
        author = a['_id']
        quotes = db.quotes.find()
        for quote in quotes:
            if quote['author'] == author:
                res.append(quote['quote'])
    print(res)

def find_quote_by_tag(tags):
    res = []
    quotes = db.quotes.find()
    for q in quotes:
        tags_ = q['tags']
        for tag in tags_:
            if tag in tags:
                if q['quote'] not in res:
                    res.append(q['quote'])
    print(res)

def main():
    while True:
        command = input('Type command: "Name:author", "tag:tag1,tag2..." or exit: ' )
        if command.startswith('name:'):
            find_quote_by_name(command.split(":")[1])
        elif command.startswith('tag:'):
            list_tags = command.strip().replace(" ","").split(":")[1].split(",")
            find_quote_by_tag(list_tags)
        elif command == 'exit':
            print("Good buy!")
            break
        else:
            print("Wrong command!")


if __name__ == '__main__':
    main()

