from app import create_app


def init_db():
    from app import db
    app = create_app('DEV')
    app.app_context().push()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    init_db()
    pass
