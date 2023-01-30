class Post():
    """Class that defines the properties for a post object"""

    # Write the __init__ method here
    def __init__(self, id, user_id, category_id, title, publication_date, image_url, content, approved):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
        self.user = None
        self.category = None


class PostDetails():
    def __init__(self, title, first_name, last_name, label, publication_date, content):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.label = label
        self.publication_date = publication_date
        self.content = content