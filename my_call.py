class Call:
    def __init__(self, c):
        self.call_time = c[1]
        self.src = c[2]
        self.dest = c[3]
        self.elvstatus = c[4]

    def isDone(self) -> bool:
        return (self.elvstatus != -1)

    def get_src(self):
        return self.src

    def get_dst(self):
        return self.dest

    def allocate(self, elev_id):
        self._el = elev_id

    def get_row(self):
        Row = ['Elevator call', self.call_time, self.src, self.dest, self.elvstatus, self._el]
        return Row
