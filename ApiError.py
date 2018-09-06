class ApiError(Exception):
    result = None
    errcode = None
    errtext = None

    def __init__(self, errcode, errtext):
        Exception.__init__(self)
        self.result = 'err'
        self.errcode = errcode
        self.errtext = errtext

    def get_error(self):
        return {'result': self.result, 'errcode': self.errcode, 'errtext': self.errtext}

    def __str__(self):
        return str(self.get_error())
