class Solution:
    def reverseBits(self, n: int) -> int:
        
        # Step 1: 轉換成二進位字串

    
        binary = bin(n)
        binary = binary[2:] 
        

        # Step 2: 補滿 32 個 bits
        binary = binary.zfill(32)
        print(binary)

        # Step 3: 反轉字串
        reverse = binary[::-1]
        print(reverse)

        # Step 4: 轉回十進位並 return
        number = int(reverse, 2) # 2 是在跟py說 這是2進位 我要轉成數字

        print(number)

        return number