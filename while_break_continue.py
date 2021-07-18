def main():
    counter = 5000
    
    while counter < 10000000:
        print(counter)
        counter *= 2
        if counter == 1000000:
            break
        # if counter % 2 != 0:
        #     continue 
        
    
    


if __name__ == '__main__':
    main()