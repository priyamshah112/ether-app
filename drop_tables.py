from main import db


if __name__ == '__main__':
    print('Deleting all database tables...')
    db.drop_all()
    print('Done!')
# [END all]
