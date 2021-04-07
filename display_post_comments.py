import json
import requests


def main():
    try:
        post_response = requests.get('https://jsonplaceholder.typicode.com/posts')
        comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')
        post_data = json.loads(post_response.text)
        comments_data = json.loads(comments_response.text)
        dash = '-' * 200
        dot = '.' * 200

        for post in post_data:
            print(dash)
            print('{:>100} {:<100}'.format('Post', post['id']))
            print(dash)
            print('Title: {}'.format(post['title']))

            description_text = post['body'].replace('\n', ' ')
            print('Description: {}'.format(description_text))

            print('Comments: ')
            print('[Comment - Commented By]')
            print(dot)
            for comments in comments_data:
                if post['id'] == comments['postId']:
                    comments_text = comments['body'].replace('\n', ' ')
                    print('{} - {}'.format(comments_text, comments['email']))
        return True

    except Exception:
        print('Error in post/comments')


if __name__ == '__main__':
    main()

