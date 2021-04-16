import re
from playsound import playsound


# Main return is emailBatch[] from  batchEmails()
class Email:
    def __init__(self, service):
        self.service = service

    def getEmails(self, service, label, query):
        ids = []
        headerList = []
        
        results = service.users().messages().list(userId='me', labelIds=label, q=query).execute()
        messages = results.get('messages')
        
        if not results or not messages:
            return headerList

        for message in messages: 
            ids.append(message['id'])

        for iid in ids: 
            email = service.users().messages().get(userId='me', id=iid, format='full').execute()
            payload = email['payload']
            headers = payload.get("headers")
            headerList.append(headers)
        
        return headerList

    def getContent(self, content):
        emails = []
        subject = None
        sender = None
        date = None
        count = 0

        for x in range(len(content)):
            subject = None
            sender = None
            date = None
            for y in content[x]:
                count += 1
                if list(y.items())[:1] == [(u'name', u'From')]:
                    sender = y.get(u'value')
                    sender = sender.replace('"', "").strip("/\"\"\\[]!@#$%^*()+=").split(" <")[0]
                if list(y.items())[:1] == [(u'name', u'Date')]:
                    date = y.get(u'value')
                    date = date.replace('"', "").split(", ", 1)
                    if len(date) == 1:
                        date = str(date)
                    else: 
                        date = date[1]
                    date = date.split(" ")
                    datefilter = filter(str.isdigit, date[0])
                    datestring = "".join(datefilter)
                    date[0] = datestring
                    date[1] += " " + date[0]
                    date[1] += " " + date[2]
                    date = date[1]
                if list(y.items())[:1] == [(u'name', u'Subject')]:
                    subject = y.get(u'value')
                    subject = subject.replace('"', "").strip("/\"\\[]!@#$%^*()+=").split(" <")[0]
                if sender and date and subject:
                    email = [sender, date, subject]
                    emails.append(email)
                    break
            continue
        return emails

    def batchEmails():
        emailBatch = []

        personal = self.getEmails(service, "CATEGORY_PERSONAL", 'in:inbox')
        emailBatch.append(self.getContent(personal))
        
        social = self.getEmails(service, "CATEGORY_SOCIAL", 'in:inbox')
        emailBatch.append(self.getContent(social))
        
        promos = self.getEmails(service, "CATEGORY_PROMOTIONS", 'in:inbox')
        emailBatch.append(self.getContent(promos))
        
        updates = self.getEmails(service, "CATEGORY_UPDATES", 'in:inbox')
        emailBatch.append(self.getContent(updates))

        forums = self.getEmails(service, "CATEGORY_FORUMS", 'in:inbox')
        emailBatch.append(self.getContent(forums))

        return emailBatch