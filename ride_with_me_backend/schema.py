import graphene

import rides.schema


class Query(rides.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
