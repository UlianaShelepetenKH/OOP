from abc import ABC, abstractmethod

# --- Composite Pattern ---

class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"📄 {self.name}")

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def show(self, indent=0):
        print(" " * indent + f"📁 {self.name}/")
        for child in self.children:
            child.show(indent + 2)

# --- Facade Pattern ---

class FileSystemFacade:
    def __init__(self):
        self.root = Folder("root")

    def create_file(self, folder: Folder, filename: str):
        file = File(filename)
        folder.add(file)

    def create_folder(self, parent: Folder, foldername: str):
        folder = Folder(foldername)
        parent.add(folder)
        return folder

    def show_structure(self):
        self.root.show()

# --- Демонстрація ---

def main():
    fs = FileSystemFacade()

    docs = fs.create_folder(fs.root, "Documents")
    images = fs.create_folder(fs.root, "Images")
    
    fs.create_file(docs, "resume.pdf")
    fs.create_file(docs, "notes.txt")

    cats = fs.create_folder(images, "Cats")
    fs.create_file(cats, "fluffy.png")
    fs.create_file(images, "dog.jpg")
    fs.create_file(cats, "fl.png")

    print("\nСтруктура файлової системи:")
    fs.show_structure()

if __name__ == "__main__":
    main()
