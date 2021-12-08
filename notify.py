import urllib3
import json
from socket import timeout


class TeamsWebhookException(Exception):
    """custom exception for failed webhook call"""
    pass


class ConnectorCard:
    def __init__(self, hookurl, http_timeout=60):
        self.http = urllib3.PoolManager()
        self.payload = {"@type":"MessageCard","@context":"https://schema.org/extensions","summary":"Registration Card","themeColor":"0078D7","title":"SpinnakerBot","sections":[{"facts":[{"name":"ApplicationName","value":"Sample"},{"name":"ExecutionName:","value":"Sample-pipeline"},{"name":"ExecutionStatus:","value":"Started"}]}]}
        self.hookurl = hookurl
        self.http_timeout = http_timeout

    def text(self, mtext):
        self.payload["text"] = mtext
        return self

    def send(self):
        headers = {"Content-Type":"application/json"}
        r = self.http.request(
                'POST',
                f'{self.hookurl}',
                body=json.dumps(self.payload).encode('utf-8'),
                headers=headers, timeout=self.http_timeout)
        if r.status == 200: 
            return True
        else:
            raise TeamsWebhookException(r.reason)


if __name__ == "__main__":
    myTeamsMessage = ConnectorCard("https://digitaldotsinc.webhook.office.com/webhookb2/2f223a55-bdde-48fc-9e13-c73d7d49b3e0@09d9df66-37d7-493b-8823-4af2c12a1af5/IncomingWebhook/1be998ad3dba47f38aeb200806539156/ce8eeaf0-149a-4996-9472-194a926ace9b")
    myTeamsMessage.text("")
    myTeamsMessage.send()
