# Your task is to implement a simulation of a change directory command. This command changes the current working directory to the specified one. 
# The initial working directory is root i.e. /. You are given a list of cd commands. There are multiple options for command arguments. cd / - changes the working directory to the root directory. 
# cd . - stays in the current directory. cd .. - moves the working directory one level up. In the root directory, cd .. does nothing. 
# cd <subdirectory> - moves to the specified subdirectory within the current working directory. <subdirectory> is a string consisting of only lowercase English letters. 
# All specified directories exist. Return the absolute path from the root to the working directory after executing all cd commands in the given order. / should be used as separators. Note: You are not expected 
# to provide the most optimal solution, but a solution with time complexity not worse than O(commands.length * max(commands[i].length)) will fit within the execution time limit.


cmds=[line.strip() for line in sys.stdin.readlines()]
ans=[]
for c in cmds:
	c=c[3:]
	if c=='.':
		continue
	elif c=='/':
		ans.clear()
	elif len(ans)==0 and c=="..":
		continue
	elif c=="..":
		ans.pop()
	else:
		ans.append(c)
print("/"+"/".join(ans))



-------------java-----------

import java.util.*;

public class cd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // consume the newline

        String[] arr = new String[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextLine();
        }

        Stack<String> s = new Stack<>();

        for(int i=0;i<n;i++){
            String[] parts = arr[i].split(" ");
            String command = parts[1];

            if(command.equals("/")){
                s.clear();
            }
            else if(command.equals("..")){
                if(!s.isEmpty()){
                    s.pop();
                }
            }
            else if(command.equals(".")){
                continue;
            }
            else{
                s.push(command);
            }
        }

        if(s.isEmpty()){
            System.out.println("/");
        }
        else{
            StringBuilder sb = new StringBuilder();
            for(String dir : s){
                sb.append("/").append(dir);
            }
            System.out.println(sb.toString());
        }
        
    }
}
