from fhan.fhirpath.generated.FhirPathListener import FhirPathListener


class Listener(FhirPathListener):
    def enterIdentifier(self, ctx):
        print("tetx: ", ctx.getText())
        print("ctx: ", ctx)
        print("__dict__: ", ctx.__dict__)
        print("__dir__: ", ctx.__dir__())
