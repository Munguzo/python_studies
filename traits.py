class Character:
  def __init__(self, name, traits):
    self.name = name
    self.traits = traits

  def describe (self):
    print(f"{self.name} is a character with the following traits:")
    for trait in self.traits:
      print(f"- {trait}")

# Example usage:

character = Character("Alice", ["kind", "intelligent", "determined"])
character.describe()


