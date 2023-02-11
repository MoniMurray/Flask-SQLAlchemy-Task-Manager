from taskmanager import db


class Categories(db.Model):
    # creating table, represented by class-based models using SQLAlchemy ORM
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", 
        backref="categories", 
        cascade="all, delete",
        lazy=True
    )

    def __repr__(self):
        return self.category_name


class Task(db.Model):
    # creating table, represented by class-based models using SQLAlchemy ORM
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False
    )

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
            )


