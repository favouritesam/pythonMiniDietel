counter = 0

while counter < 10:
    try:

        counter += 1
        if counter == 5:
            raise RuntimeWarning("counter should not be 5")
    # except RuntimeWarning as err:
    #     print("Wahala cast:", err)
    finally:
        print("Bye bye") 
    # else:
    #     print(else block)
