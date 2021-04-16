from canvasapi import Canvas
import requests
import json
import datetime
from datetime import date
from datetime import timedelta
from dateutil.parser import parse
import maya


# Main return is todo[] from getAssignments()
class School:
    classList = {''}
    def getFavorites(self):
        url = 'https://psu.instructure.com/api/v1/users/self/favorites/courses'
        favorites = requests.get(url, headers={'Authorization' : 'Bearer API-TOKEN-HERE'})
        favorites = favorites.json()
        courses = {}
        for x in favorites:
            value = x['name']
            key = int(x['id'])
            courses[key] = value
        return courses

    def getDate(self, inputDate):
        self.inputDate = inputDate
        newDate = maya.parse(inputDate).datetime(to_timezone='America/New_York', naive=False)
        return newDate

    def getAssignments(self):
        API_URL = "https://psu.instructure.com/"
        API_TOKEN = ""                                    #API TOKEN HERE
        canvas = Canvas(API_URL, API_TOKEN)
        results = canvas.get_todo_items()
        dashboard = []
        todo = []
        for i in results:
            dashboard.append(i)

        favorites = self.getFavorites()

        compareDate = date.today() - timedelta(days=3)
        for x in dashboard:
            hold = []
            if(self.getDate(x['assignment']['due_at']).date() >= compareDate):
                course = favorites.get(x['course_id'])
                name = x['assignment']['name']
                dueDate = datetime.datetime.strftime(self.getDate(x['assignment']['due_at']), "%A, %B %d")
                dueTime = datetime.datetime.strftime(self.getDate(x['assignment']['due_at']), "%I:%M %p")
                hold.append(course)
                hold.append(name)
                hold.append(dueDate)
                hold.append(dueTime)
                todo.append(hold)
            else: 
                continue
        return todo