class ASTree:
    def __init__(self):
        self.instructionType = None
        self.operator = None
        self.children = None
        self.value = None

    def _innerBuildAST(self, instruction, operator, args, value=None):
        if args is None and value is None:
            raise Exception('У узла должно быть значение или дочерние узлы')
        if (args is None and instruction != 'ARGUMENT') or (value is None and instruction == 'ARGUMENT'):
            raise Exception('У узла указан некорректный тип')

        self.operator = operator
        self.instructionType = instruction
        if self.instructionType != 'ARGUMENT':
            self.value = None
            if self.instructionType == 'UNARY':
                self.children = ASTree.buildAST(args)
            if self.instructionType == 'MULTIPLE':
                self.children = []
                for elem in args:
                    self.children.append(ASTree.buildAST(elem))
        else:
            self.children = None
            self.value = value
        return self

    @staticmethod
    def buildAST(node):
        result = ASTree()

        if isinstance(node, list):
            operator = node[0]
            args = node[1]
            instruction = 'MULTIPLE' if isinstance(args, list) else 'UNARY'
            return result._innerBuildAST(instruction, operator, args)

        return result._innerBuildAST('ARGUMENT', None, None, node)
