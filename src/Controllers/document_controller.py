class DocumentController:

    _id = 0
    filename = ""

    #creates degree document when the doctors signs up
    def upload_medical_degree(self, _id, filename):
        self._id = _id
        self.filename = filename