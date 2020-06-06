import requests
import json

ACCESS_TOKEN = "o.K5jHFfBbFJtsjfFzshYDuXnseVjPHku1"


class Pushbullet_utils:

    @staticmethod
    def send_notification_via_pushbullet(title, body):
        """ Sending notification via pushbullet.

        :param: title (str) : title of text.
        :param: body (str) : Body of text.
        """

        print(title)
        data_send = {"type": "note", "title": title, "body": body}

        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                             headers={'Authorization': 'Bearer ' + ACCESS_TOKEN,
                                      'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Something wrong')
        else:
            print('complete sending')
