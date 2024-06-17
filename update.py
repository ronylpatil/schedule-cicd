import datetime

def update_readme(file_path, marker, new_content):
     with open(file_path, 'r') as file:
          lines = file.readlines()
     
     with open(file_path, 'w') as file:
          for line in lines:
               if marker in line:
                    file.write(f" {new_content}\n")
               else:
                    file.write(line)

if __name__ == "__main__":
    readme_path = "README.md"
    marker = "<b>CI/CD Last Execution Time:</b>"
    execution_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_content = f"{marker} {execution_time}"
    
    update_readme(readme_path, marker, new_content)
