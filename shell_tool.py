from langchain_community.tools import ShellTool

# Initialize the shell tool
shell_tool = ShellTool()

try:
    # Execute the shell command safely
    command = "ls"
    results = shell_tool.invoke(command)

    # Print results only if not empty
    if results:
        print("Command executed successfully:\n", results)
    else:
        print("No output from command.")

except Exception as e:
    print("Error while executing shell command:", str(e))
