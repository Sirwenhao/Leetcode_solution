# 2023/1/19  author:WH

class Solution:
    def strongPasswordCheckII(self, password):
        if len(password) < 8:
            return False
        
        hasDigit = hasUpper = hasLower = hasSpecial = 0
        specials = set("!@#$%^&*()-+")
        
        for i, ch in enumerate(password):
            if i != len(password)-1 and password[i] == password[i+1]:
                return False
            if ch.isdigit():
                hasDigit = True
            elif ch.islower():
                hasLower = True
            elif ch.isupper():
                hasUpper = True
            elif ch in specials:
                hasSpecial = True

        return hasDigit and hasLower and hasUpper and hasSpecial

if __name__ == "__main__":
    password = "IloveLe3tcode!"
    result = Solution().strongPasswordCheckII(password)
    print(result)
