words = "helloworld".split()
spinning_words = [word[::-1] if len(word) >= 5 else word 
            for word in words]#翻转长度大于五的单词
result = " ".join(spinning_words)
print(result)
    