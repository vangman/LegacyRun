__author__ = 'vangelis'

import web
import subprocess

from ApplicationClass import Application

urls = (
    '/', 'application',
    '/(\d+)', 'application'
)

def call_command(command):
    process = subprocess.Popen(command, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return process.communicate()

class application:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="textbox" name="myapp" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def PUT(self):
        return 'Ok'


    def POST(self):
        form = web.input(myapp={})
        #web.debug(appPath['myapp'])
        application = Application()
        application.execCommand = form['myapp']
        process=application.run()
        #(stdout,stderr) = call_command(appPath['myapp'])
        (stdout,stderr) = process.communicate()
        return stdout
        #raise web.seeother('/application')

    def DELETE(self):
        return 'Just deleted'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
