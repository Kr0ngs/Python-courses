class Commet:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


first_comment = Commet("First comment ")

print(first_comment.votes_qty)  # 0
print(first_comment.text)
# First comment
