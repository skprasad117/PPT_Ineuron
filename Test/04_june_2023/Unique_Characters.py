class NonRepeating:
    def find(self,string):
        for i in range(len(string)):
            if string[i] not in string[i+1:] and string[i] not in string[:i] :
                return i
        return -1
if __name__ =="__main__":
    obj = NonRepeating()
    print(obj.find(input("Enter a String : ")))