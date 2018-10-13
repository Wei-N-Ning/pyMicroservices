"""
source
https://medium.com/@ssola/building-microservices-with-python-part-i-5240a8dcc2fb

end point:
http://127.0.0.1:9090/v1.0/items

swagger doc:
http://127.0.0.1:9090/v1.0/ui
"""


from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    app.run(port=9090)
