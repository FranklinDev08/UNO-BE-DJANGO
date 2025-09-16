import graphene
from infrastructure.graphql.mutation import Mutation as MutationRoot

''''
from infrastructure.graphql.queries.role_query import RolesQuery
from infrastructure.graphql.queries.faculty_query import FacultiesQuery
from infrastructure.graphql.queries.user_query import UsersQuery
from infrastructure.graphql.queries.career_query import CareersQuery
from infrastructure.graphql.queries.student_query import StudentsQuery
from infrastructure.graphql.queries.teacher_query import TeachersQuery
from infrastructure.graphql.queries.materia_query import MateriasQuery
'''

class Query(
    
    #RolesQuery,
    #UsersQuery,
    #FacultiesQuery,
    #CareersQuery,
    #StudentsQuery,
    #TeachersQuery,
    #MateriasQuery,
            graphene.ObjectType):
    hello = graphene.String(default_value="Hola mundo")

schema = graphene.Schema(query=Query, mutation=MutationRoot)
