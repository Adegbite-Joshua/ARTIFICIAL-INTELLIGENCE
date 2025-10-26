import os

print(os.getcwd())

new_folder = r"C:\Users\USA\ARTIFICIAL INTELLIGENCE\Python\JB_folder"

# if not os.path.exists(new_folder):
#     os.makedirs(new_folder)
#     print("Directory created successfukly")
# else:
#     print("Directory already exists")
    
# file_path = os.path.join(new_folder, "example.txt")
# try:
#     with open(file_path, "x") as file:
#         file.write("This is the new contetnt") 
#         print("File created")
# except FileExistsError:
#     print("File already exists")




# print(os.listdir())
contents = os.listdir()
files_path = []
# for content in contents:
#     if os.path.isfile(content):
#         # print(f"{content} is a file")
#         files_path.append(os.path.join(os.getcwd(), content))
#     # else:
#         # print(f"{content} is a folder")
        
# for path in files_path:
#     print(path)


# Basic usage
for root, dirs, files in os.walk('.'):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 50)
    
    
