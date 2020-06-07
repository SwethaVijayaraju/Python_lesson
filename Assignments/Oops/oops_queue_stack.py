# 7a. Create a class called Queue(which mimics the behavior of an actual queue - First In First Out behavior)
# q = Queue()
# join(name)
# - Use any data structure to keep track of who are in the queue
# q.join("vishnu") # currently vishnu is in the queue
# q.join("swetha") # swetha is also in the queue
# next()
# - Remove the person in front of the queue. (That is how queues in real life work).
# People join the queue in the end and leave from the front.
# q.next() # returns "vishnu"
# q.next() # returns "swetha"
# q.join("sukrut")
# q.next() # "mary"
# q.next() # "sukrut"
# q.next() # error since no body is in the queue

# 7b. As an extension, add a capacity to the queue(Only these many number of people can be in the queue)
# q = Queue(3)
# q.join("vishnu") # currently vishnu is in the queue
# q.join("swetha") # swetha is also in the queue
# q.join("mary")
# q.join("sukrut") # error since there are already 3 people in the queue

# q.next() # "vishnu"
# q.join("sukrut") # now this is fine because vishnu was removed from the queue.

# 7c. Use inheritance to implement Stack from Queue. Since the join logic is the same Stack shouldn't have to
# implement the join method(or init). It should basically have a different logic for selecting the next member.
# Stack has the behavior of Last In First Out(Compare with First in First out)

# s = Stack(capacity)
# s.join("vishnu")
# s.join("sukrut")
# s.next() # "sukrut"
# s.join("swetha")
# s.next() # "swetha"
# s.next() # "vishnu"

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.cap = capacity

    def join(self, person):
        if len(self.queue) < self.cap:
            if person not in self.queue:
                self.queue.append(person)
                print(self.queue)
            else:
                position = self.queue.index(person) + 1
                if position == 1:
                    suffix = "st"
                elif position == 2:
                    suffix = "nd"
                elif position == 3:
                    suffix = "rd"
                else:
                    suffix = "th"
                print("Error -", person, "is already in the queue -", position, suffix, "person")
        else:
            print("Error - Queue is full")

    def next(self):
        if len(self.queue) != 0:
            r = self.queue[0]
            self.queue.remove(self.queue[0])
            return r
            # print(self.queue)
        else:
            print("Error - Nobody is in the queue")


class Stack(Queue):
    def next(self):
        if len(self.queue) != 0:
            r = self.queue[-1]
            self.queue.remove(self.queue[-1])
            return r
            # print(self.queue)
        else:
            print("Error - Nobody is in the queue")


q1 = Queue(3)
q1.join("vishnu")
q1.join("swetha")
q1.next()
q1.next()
q1.next()
q1.join("sukrut")
q1.next()
q1.join("vishnu")
q1.join("swetha")
q1.join("mary")
q1.join("sukrut")
q1.next()
q1.join("sukrut")
print(q1.next())
q1.join("vishnu")
q2 = Queue(6)
q2.join("vinodh")
q2.join("nivetha")
q2.join("chitra")
q2.join("rengz")
q2.join("naveen")
q2.join("rengz")
q2.join("manisekar")
s = Stack(4)
s.join("harry")
s.join("ron")
s.join("hermoine")
s.join("ginny")
s.join("draco")
print(s.next())
