def handling_exception():
    print('==== handling exception')
    lst = []
    try:
        lst[0] = 1
    except Exception as e:
        print('Exception occured:', e)
    else:
        print('No exception')
    finally:
        print('Finally block executed')
    print('End of program')


def raise_exception():
    def beware_dog(animal):
        if animal == 'Dog':
            raise RuntimeError('개는 안돼요...')
        else:
            print('어서오세용')
    
    try:
        beware_dog(animal='Cat')
        beware_dog(animal='Dog')
    except Exception as e:
        print('Exception occured:', e)
    else:
        print('No exception')



if __name__ == '__main__':
    # handling_exception()
    raise_exception()