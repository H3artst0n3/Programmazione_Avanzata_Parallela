# Angelica Rota SM3201142

# custom exception for missing variable
class MissingVariableException(Exception):
    pass

# custom exception for value exception
class ValueException(Exception):
    pass

# custom exception for an empty stack
class EmptyStackException(Exception):
    pass

# custom exception for operation not found in the dictionary 
class OperationNotFound(Exception):
    pass

# custom exception for dividing by zero 
class DivisionByZero(Exception):
    pass

# custom exception for missing one or more required expressions 
class ExprException(Exception):
    pass

# custom exception for index exception
class IndexException(Exception):
    pass

# custom exception for type exception
class TypeException(Exception):
    pass