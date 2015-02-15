from models import Content, Article, Picture
import json

def to_json():
    ''' Write Content.existing_content using json into dump.txt 
        for retrieval later.
    '''
    myfile = open('dump.txt', 'a')

    # do for every existing Content object
    for obj in Content.existing_content:

        if type(obj) == Article:
            # put all the attributes into a dictionary
            d = {
                'type': 'Article',
                'year': obj.creation_date.year,
                'month': obj.creation_date.month,
                'day': obj.creation_date.day,
                'headline': obj.headline,
                'content': obj.content,
                'contributors': obj.contributors
            }

            # string representing the json dump of the obj
            dump = json.dumps(d)

            # append it to the file on newline
            myfile.write(dump + '\n')

        elif type(obj) == Picture:
            # put all the attributes into a dictionary
            d = {
                'type': 'Picture',
                'year': obj.creation_date.year,
                'month': obj.creation_date.month,
                'day': obj.creation_date.day,
                'title': obj.title,
                'caption': obj.caption,
                'path': obj.path,
                'contributors': obj.contributors
            }

            # string representing the json dump of the obj
            dump = json.dumps(d)

            # append it to the file on newline
            myfile.write(dump + '\n')

        else:
            # if it's not either of these, continue quietly.
            pass

    # close the file
    myfile.close()


def from_json():
    ''' Load all content from dump.txt into Content.existing_content
    '''
    myfile = open('dump.txt', 'r')

    # loop over file
    for line in myfile:
        # read the next line and remove the trailing '\n'
        dump = line[:-1]

        # turn string into a dictionary of values
        dic = json.loads(dump)

        if dic['type'] == 'Article':
            # this automatically logs the Article in Content.existing_content
            Article(dic['year'], dic['month'], dic['day'], dic['headline'], 
                    dic['content'], dic['contributors'])

        elif dic['type'] == 'Picture':
            Picture(dic['year'], dic['month'], dic['day'], dic['title'], 
                    dic['caption'], dic['path'], dic['contributors'])
        else:
            # pass quietly
            pass 

    myfile.close()

