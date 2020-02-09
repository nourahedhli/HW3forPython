class Addition:

    @staticmethod
    def sum(augend, addend=None):
        if isinstance(augend, list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(Valuelist):
        result = 0
        for value in Valuelist:
            result = Addition.sum(result, value)

        return result
