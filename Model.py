from uuid import UUID, uuid4

class Courses:
    def __init__(self,
                 title: str,
                 description: str,
                 mentor: str,
                 duration: str,
                 price: float,
                 finished: str,
                 id: UUID = None):
        self.title = title
        self.description = description
        self.mentor = mentor
        self.duration = duration
        self.price = price
        self.finished = finished
        self.id = id or uuid4()

    def __str__(self):
        return f"""ID: {self.id}
                    Title: {self.title}
                    Description: {self.description}
                    Mentor: {self.menot}
                    Duration: {self.duration}
                    Price: {self.price}
                    Is Finished: {self.finished}"""