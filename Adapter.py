 # Legacy Class
class LegacyClass:
    def legacy_method(self):
        print("Legacy method called")

# Target Interface
class Target:
    def new_method(self):
        pass

# Adapter Class
class Adapter(Target):
    def __init__(self):
        self.legacy_object = LegacyClass()

    def new_method(self):
        self.legacy_object.legacy_method()

# Usage
adapter = Adapter()
adapter.new_method()

